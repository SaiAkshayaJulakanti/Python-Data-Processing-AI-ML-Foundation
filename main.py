"""
Master Execution Script for Employee Data Analysis System.
"""
import os
import sys

# Try importing tabulate for pretty tables, fallback to pandas default printing
try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

# Add src directory to module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from numpy_demo import run_numpy_demonstration
from pandas_demo import run_pandas_demonstration
from data_pipeline import EmployeeDataCleaner

def print_table(df, showindex=False):
    """Prints a DataFrame using tabulate if available, else standard pandas display."""
    if HAS_TABULATE:
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=showindex))
    else:
        print(df.to_string(index=showindex))

def main():
    print("=" * 70)
    print("🚀 EMPLOYEE DATA ANALYSIS SYSTEM & AI/ML FOUNDATION TASKS")
    print("=" * 70)

    # 1. Run NumPy Demonstration
    print("\nExecuting NumPy Foundations...")
    run_numpy_demonstration()

    # 2. Run Pandas Demonstration
    print("\nExecuting Pandas Data Handling...")
    run_pandas_demonstration()

    # 3. Execute End-to-End Employee Data Pipeline
    print("\nExecuting Automated Data Cleaning & Transformation Pipeline...")
    raw_csv = os.path.join('data', 'employees.csv')
    clean_csv = os.path.join('data', 'cleaned_employees.csv')

    cleaner = EmployeeDataCleaner(raw_csv)
    cleaned_df, stats, logs = cleaner.run_pipeline(clean_csv)

    print("\n=== PIPELINE EXECUTION SUMMARY LOGS ===")
    for log in logs:
        print(f"✓ {log}")

    print("\n=== CLEANED DATASET (FIRST 10 ROWS) ===")
    print_table(cleaned_df.head(10), showindex=False)

    print("\n=== DEPARTMENTAL SALARY & EXPERIENCE AGGREGATIONS ===")
    print_table(stats['department_statistics'], showindex=False)

    print("\n=== OVERALL COMPANY METRICS ===")
    for k, v in stats['overall_statistics'].items():
        if isinstance(v, float):
            print(f"  • {k:<25}: ${v:,.2f}" if 'Salary' in k or 'Payroll' in k else f"  • {k:<25}: {v:,.2f}")
        else:
            print(f"  • {k:<25}: {v}")

    print("\n=" * 70)
    print(f"✨ Processing Complete! Clean dataset generated at: {clean_csv}")
    print("=" * 70)

if __name__ == '__main__':
    main()
