"""
Pytest Test Suite for Employee Data Analysis System & Pipeline.
"""
import os
import sys
import pytest
import pandas as pd
import numpy as np

# Add src directory to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from numpy_demo import run_numpy_demonstration
from pandas_demo import run_pandas_demonstration
from data_pipeline import EmployeeDataCleaner

@pytest.fixture
def raw_csv_path(tmp_path):
    """Fixture providing a temporary raw CSV dataset with missing values and duplicates."""
    csv_file = tmp_path / "test_raw_employees.csv"
    data = """Employee_ID,Full_Name,Department,Job_Title,Salary,Experience_Years,Hire_Date,Email
101,John Smith,  engineering  ,Developer,85000,5.0,2019-03-15,john@example.com
102,Jane Doe,Engineering,Lead,110000,8.0,2017-06-20,jane@example.com
101,John Smith,engineering,Developer,85000,5.0,2019-03-15,john@example.com
103,Bob Bad,Sales,Rep,-50000,2.0,2021-01-15,bob@example.com
104,Alice Missing,Marketing,Manager,,3.0,2020-08-10,alice@example.com
"""
    csv_file.write_text(data)
    return str(csv_file)


def test_numpy_demo_execution():
    """Verify NumPy demonstration function runs without errors and produces valid outputs."""
    results = run_numpy_demonstration()
    assert 'salaries_stats' in results
    assert results['salaries_stats']['total'] > 0
    assert results['weighted_scores'].shape == (4, 3)


def test_pandas_demo_execution():
    """Verify Pandas demonstration function runs without errors and produces valid outputs."""
    results = run_pandas_demonstration()
    assert 'df_created' in results
    assert len(results['df_created']) == 5


def test_pipeline_cleaning_and_deduplication(raw_csv_path, tmp_path):
    """Verify pipeline removes duplicates and cleans text formatting."""
    cleaner = EmployeeDataCleaner(raw_csv_path)
    cleaner.load_data().clean_column_names().remove_duplicates().clean_text_formatting()
    
    # 5 rows initial, 1 exact duplicate -> 4 unique Employee_IDs remaining
    assert len(cleaner.df_cleaned) == 4
    assert 'Engineering' in cleaner.df_cleaned['Department'].values


def test_pipeline_negative_salary_correction(raw_csv_path):
    """Verify negative salary values are converted to positive numbers."""
    cleaner = EmployeeDataCleaner(raw_csv_path)
    cleaner.load_data().fix_numerical_anomalies()
    
    # Non-null salaries should all be strictly positive
    valid_salaries = cleaner.df_cleaned['Salary'].dropna()
    assert (valid_salaries > 0).all()


def test_pipeline_missing_value_imputation(raw_csv_path):
    """Verify missing salary is imputed using department median."""
    cleaner = EmployeeDataCleaner(raw_csv_path)
    cleaner.load_data().clean_text_formatting().handle_missing_values()
    
    # Missing salary in row 5 should be filled
    assert cleaner.df_cleaned['Salary'].isna().sum() == 0


def test_full_pipeline_end_to_end(raw_csv_path, tmp_path):
    """Verify complete pipeline execution and file saving."""
    output_path = str(tmp_path / "final_clean_employees.csv")
    cleaner = EmployeeDataCleaner(raw_csv_path)
    cleaned_df, stats, logs = cleaner.run_pipeline(output_path)
    
    assert os.path.exists(output_path)
    assert len(cleaned_df) == 4
    assert cleaned_df.isna().sum().sum() == 0
    assert (cleaned_df['Salary'] > 0).all()
    assert 'department_statistics' in stats
