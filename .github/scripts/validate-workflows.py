#!/usr/bin/env python3
"""
Validate all GitHub Actions workflow YAML files.
This script ensures workflow files are valid YAML and checks for common issues.
"""

import os
import sys
import yaml
import json
from pathlib import Path

def validate_yaml_file(filepath):
    """Validate a single YAML file."""
    errors = []
    warnings = []
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            data = yaml.safe_load(content)
            
        # Check for common issues
        if data is None:
            errors.append(f"Empty or invalid YAML structure")
            return errors, warnings
            
        # Check for required top-level keys
        if 'name' not in data:
            warnings.append("Missing 'name' field")
        if 'on' not in data:
            errors.append("Missing 'on' trigger field")
        if 'jobs' not in data:
            errors.append("Missing 'jobs' field")
            
        # Check for problematic patterns
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            # Check for template literals in body fields (potential YAML parsing issues)
            if 'body: `' in line:
                warnings.append(f"Line {i}: Template literal in body field - consider using array.join() format")
            
            # Check for unescaped conditionals
            if line.strip().startswith('if:') and 'github.' in line and '${{' not in line:
                warnings.append(f"Line {i}: Unescaped conditional - wrap with ${{{{ }}}} for safety")
                
        # Additional validation for jobs
        if 'jobs' in data and isinstance(data['jobs'], dict):
            for job_name, job_config in data['jobs'].items():
                if not isinstance(job_config, dict):
                    errors.append(f"Job '{job_name}' has invalid configuration")
                elif 'runs-on' not in job_config:
                    errors.append(f"Job '{job_name}' missing 'runs-on' field")
                    
    except yaml.YAMLError as e:
        errors.append(f"YAML parsing error: {e}")
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            errors.append(f"  at line {mark.line + 1}, column {mark.column + 1}")
    except Exception as e:
        errors.append(f"Unexpected error: {e}")
        
    return errors, warnings

def validate_all_workflows(workflow_dir=".github/workflows"):
    """Validate all workflow files in the directory."""
    workflow_path = Path(workflow_dir)
    
    if not workflow_path.exists():
        print(f"❌ Workflow directory '{workflow_dir}' does not exist")
        return False
        
    workflow_files = list(workflow_path.glob("*.yml")) + list(workflow_path.glob("*.yaml"))
    
    if not workflow_files:
        print(f"⚠️  No workflow files found in '{workflow_dir}'")
        return True
        
    print(f"🔍 Validating {len(workflow_files)} workflow files...\n")
    
    total_errors = 0
    total_warnings = 0
    failed_files = []
    
    for filepath in sorted(workflow_files):
        relative_path = filepath
        errors, warnings = validate_yaml_file(filepath)
        
        if errors:
            print(f"❌ {relative_path}")
            for error in errors:
                print(f"   ERROR: {error}")
            failed_files.append(str(relative_path))
            total_errors += len(errors)
        elif warnings:
            print(f"⚠️  {relative_path}")
            for warning in warnings:
                print(f"   WARNING: {warning}")
            total_warnings += len(warnings)
        else:
            print(f"✅ {relative_path}")
            
    print(f"\n{'='*50}")
    print(f"📊 Validation Summary:")
    print(f"   Files checked: {len(workflow_files)}")
    print(f"   Errors: {total_errors}")
    print(f"   Warnings: {total_warnings}")
    print(f"   Failed files: {len(failed_files)}")
    
    if failed_files:
        print(f"\n❌ Validation FAILED for:")
        for file in failed_files:
            print(f"   - {file}")
        return False
    else:
        print(f"\n✅ All workflow files are valid!")
        return True

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate GitHub Actions workflow YAML files")
    parser.add_argument('--dir', default='.github/workflows', 
                        help='Directory containing workflow files (default: .github/workflows)')
    parser.add_argument('--strict', action='store_true',
                        help='Treat warnings as errors')
    parser.add_argument('--json', action='store_true',
                        help='Output results in JSON format')
    
    args = parser.parse_args()
    
    if args.json:
        # JSON output for CI integration
        results = []
        workflow_path = Path(args.dir)
        if workflow_path.exists():
            for filepath in sorted(workflow_path.glob("*.yml")) + sorted(workflow_path.glob("*.yaml")):
                errors, warnings = validate_yaml_file(filepath)
                results.append({
                    'file': str(filepath.relative_to(Path.cwd())),
                    'errors': errors,
                    'warnings': warnings,
                    'valid': len(errors) == 0
                })
        print(json.dumps(results, indent=2))
        success = all(r['valid'] for r in results)
        if args.strict:
            success = success and all(len(r['warnings']) == 0 for r in results)
        sys.exit(0 if success else 1)
    else:
        # Regular output
        success = validate_all_workflows(args.dir)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()