#!/usr/bin/env python3
"""
Litex Error Parser - Ready-to-use error extraction tool
Recursively extract the complete error chain from litex_verified.json

Usage:
    python3 parse_litex_error.py <litex_verified.json>
    
Example:
    python3 parse_litex_error.py solutions/problem_5/litex_verified.json

Output:
    - Verification status (success/failure)
    - Error type and line number
    - Failed goal
    - Complete recursively extracted error chain
    - Unknown result type
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List


def extract_previous_errors(err_obj: Dict[str, Any], depth: int = 1) -> List[str]:
    """
    Recursively extract information from every previous_error level
    
    Args:
        err_obj: Error object
        depth: Current recursion depth
        
    Returns:
        List of error messages
    """
    if "previous_error" not in err_obj:
        return []
    
    prev_errors = []
    prev = err_obj["previous_error"]
    
    # Extract information at this level
    if "message" in prev:
        prefix = "Detailed cause" if depth == 1 else f"Cause {depth}"
        prev_errors.append(f"\n{prefix}: {prev['message']}")
    
    if "failed_goal" in prev and "failed_goal" not in err_obj:
        prev_errors.append(f"\nFailed goal:\n{prev['failed_goal']}")
    
    if "unknown_result" in prev:
        unknown_prev = prev["unknown_result"]
        if isinstance(unknown_prev, dict):
            if "type" in unknown_prev:
                prev_errors.append(f"\nCause type: {unknown_prev['type']}")
            if "goal" in unknown_prev:
                prev_errors.append(f"\nUnknown goal: {unknown_prev['goal']}")
    
    # Recursively extract deeper levels
    prev_errors.extend(extract_previous_errors(prev, depth + 1))
    return prev_errors


def format_rollback_error(event: Dict[str, Any]) -> str:
    """
    Extract a readable error report from a Litex verification result
    
    Args:
        event: JSON object containing the Litex verification result
        
    Returns:
        Formatted error report
    """
    parts: List[str] = ["❌ Verification failed"]
    
    # Process the statement_results structure
    for stmt in event.get("statement_results") or []:
        result = stmt.get("result") or {}
        execution = result.get("execution") or {}
        
        # Extract the error object
        err = execution.get("error") or event.get("error") or {}
        
        if isinstance(err, dict):
            # Basic error information
            msg = err.get("message") or err.get("msg") or ""
            kind = err.get("kind") or err.get("error_type") or "error"
            line = err.get("line", "?")
            
            if msg:
                parts.append(f"\n({kind}, line {line}):\n{msg}")
            
            if "statement" in err:
                parts.append(f"\nFailed statement:\n{err['statement']}")
            
            if "failed_goal" in err:
                parts.append(f"\nFailed goal:\n{err['failed_goal']}")
            
            # Unknown result information
            unknown = err.get("unknown_result") or {}
            if isinstance(unknown, dict):
                if "type" in unknown:
                    parts.append(f"\nCause type: {unknown['type']}")
                if "goal" in unknown:
                    parts.append(f"\nUnknown goal: {unknown['goal']}")
            
            # Recursively extract all previous_error entries
            parts.extend(extract_previous_errors(err))
        
        # Support failed_goal directly on the result object
        if "failed_goal" in result and "failed_goal" not in (err or {}):
            parts.append(f"\nFailed goal:\n{result['failed_goal']}")
    
    # If no useful information was extracted, print the raw error
    if len(parts) == 1 and event.get("error"):
        parts.append(f"\nerror: {json.dumps(event['error'], ensure_ascii=False)[:800]}")
    
    # If information is still missing, print the first 1,200 characters of the full event
    if len(parts) == 1:
        parts.append(f"\nFull output:\n{json.dumps(event, ensure_ascii=False, indent=2)[:1200]}")
    
    return "".join(parts)


def is_success(event: Dict[str, Any]) -> bool:
    """
    Determine whether verification succeeded
    
    Args:
        event: JSON object containing the Litex verification result
        
    Returns:
        True on verification success, False on failure
    """
    # Check the top-level ok field
    if event.get("ok") is False:
        return False
    
    # Check statement_results
    results = event.get("statement_results") or []
    if not results:
        return bool(event.get("ok"))
    
    for stmt in results:
        result = stmt.get("result") or {}
        execution = result.get("execution") or {}
        kind = execution.get("kind")
        
        # RolledBack indicates failure
        if kind == "RolledBack":
            return False
        
        # Check error markers
        if stmt.get("outcome") == "error" or result.get("kind") == "error":
            return False
    
    return True


def parse_litex_output(json_path: str) -> None:
    """
    Parse Litex verification output and print a formatted report
    
    Args:
        json_path: Path to litex_verified.json
    """
    path = Path(json_path)
    
    if not path.exists():
        print(f"❌ Error: file not found: {json_path}")
        sys.exit(1)
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            
            # Handle an empty file
            if not content:
                print("❌ Error: file is empty")
                sys.exit(1)
            
            # Try to parse JSON
            data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"❌ Error: invalid JSON file")
        print(f"Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: failed to read file")
        print(f"Details: {e}")
        sys.exit(1)
    
    # Determine whether verification succeeded
    success = is_success(data)
    
    print("=" * 60)
    if success:
        print("✅ Verification succeeded!")
        print("=" * 60)
        
        # Print basic statistics
        stmt_results = data.get("statement_results") or []
        if stmt_results:
            print(f"\nStatements verified: {len(stmt_results)}")
    else:
        print("❌ Verification failed")
        print("=" * 60)
        
        # Print the detailed error report
        error_report = format_rollback_error(data)
        print(error_report)
    
    print("\n" + "=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 parse_litex_error.py <litex_verified.json>")
        print("\nExample:")
        print("  python3 parse_litex_error.py solutions/problem_5/litex_verified.json")
        sys.exit(1)
    
    json_path = sys.argv[1]
    parse_litex_output(json_path)


if __name__ == "__main__":
    main()
