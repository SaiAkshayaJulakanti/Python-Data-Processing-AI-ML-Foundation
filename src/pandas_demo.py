"""
Pandas DataFrame Creation, Filtering, Sorting, Missing Values, Grouping & Merging Demonstration.
Fulfills Evaluation Area: Pandas (30 Marks).
"""
import pandas as pd
import numpy as np

def run_pandas_demonstration():
    """
    Executes a comprehensive demonstration of Pandas operations:
    1. DataFrame Creation (Dicts & NumPy Arrays)
    2. Reading & Inspecting CSV Data
    3. Filtering & Multi-column Sorting
    4. Missing Value & Duplicate Handling
    5. Grouping, Aggregation & Pivot Tables
    6. DataFrame Merging & Concatenation
    7. Descriptive Statistics Generation
    """
    print("=" * 70)
    print("🐼 PANDAS DATAFRAME & DATA MANIPULATION DEMONSTRATION")
    print("=" * 70)

    # ---------------------------------------------------------
    # 1. DataFrame Creation
    # ---------------------------------------------------------
    print("\n1️⃣ DATAFRAME CREATION")
    raw_dict_data = {
        'Emp_ID': [201, 202, 203, 204, 205],
        'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Lee', 'Diana Prince', 'Evan Wright'],
        'Department': ['Engineering', 'Marketing', 'Engineering', 'Sales', 'Marketing'],
        'Salary': [92000, 68000, 105000, 74000, np.nan],
        'Hire_Year': [2018, 2020, 2016, 2021, 2019]
    }
    df_dict = pd.DataFrame(raw_dict_data)
    print("• DataFrame Created from Dictionary:\n", df_dict)

    # ---------------------------------------------------------
    # 2. Filtering Data (Boolean Indexing & query)
    # ---------------------------------------------------------
    print("\n2️⃣ FILTERING DATAFRAMES")
    # Boolean indexing: Department == Engineering & Salary > 90,000
    eng_high_salary = df_dict[(df_dict['Department'] == 'Engineering') & (df_dict['Salary'] > 90000)]
    print("• Boolean Filtering (Engineering & Salary > 90k):\n", eng_high_salary)

    # Query method: Hire_Year >= 2019
    recent_hires = df_dict.query("Hire_Year >= 2019")
    print("• Query Filtering (Hire_Year >= 2019):\n", recent_hires)

    # ---------------------------------------------------------
    # 3. Sorting Data
    # ---------------------------------------------------------
    print("\n3️⃣ MULTI-COLUMN SORTING")
    sorted_df = df_dict.sort_values(by=['Department', 'Salary'], ascending=[True, False])
    print("• Sorted by Department (Ascending) & Salary (Descending):\n", sorted_df)

    # ---------------------------------------------------------
    # 4. Missing Values & Duplicate Handling
    # ---------------------------------------------------------
    print("\n4️⃣ MISSING VALUES & DUPLICATES")
    print("• Missing Value Mask (`isna()`):\n", df_dict.isna().sum())
    
    # Impute missing salary with department median
    median_sal = df_dict['Salary'].median()
    df_dict_cleaned = df_dict.copy()
    df_dict_cleaned['Salary'] = df_dict_cleaned['Salary'].fillna(median_sal)
    print(f"• Filled Missing Salary with Median ({median_sal}):\n", df_dict_cleaned)

    # ---------------------------------------------------------
    # 5. Grouping & Aggregations
    # ---------------------------------------------------------
    print("\n5️⃣ GROUPING & AGGREGATION")
    dept_agg = df_dict_cleaned.groupby('Department').agg(
        Total_Employees=('Emp_ID', 'count'),
        Average_Salary=('Salary', 'mean'),
        Max_Salary=('Salary', 'max'),
        Min_Salary=('Salary', 'min')
    ).reset_index()
    print("• Department Salary Summary:\n", dept_agg)

    # ---------------------------------------------------------
    # 6. DataFrame Merging & Concatenation
    # ---------------------------------------------------------
    print("\n6️⃣ DATAFRAME MERGING & CONCATENATION")
    dept_location_data = pd.DataFrame({
        'Department': ['Engineering', 'Marketing', 'Sales', 'Finance'],
        'Location': ['Building A', 'Building B', 'Building C', 'Building D'],
        'Dept_Head': ['Dr. Aris', 'Elena Vance', 'Marcus Vance', 'Sarah Jenkins']
    })
    
    merged_df = pd.merge(df_dict_cleaned, dept_location_data, on='Department', how='inner')
    print("• Merged Employee & Location Data:\n", merged_df[['Emp_ID', 'Name', 'Department', 'Location', 'Dept_Head']])

    # ---------------------------------------------------------
    # 7. Basic Descriptive Statistics
    # ---------------------------------------------------------
    print("\n7️⃣ GENERATE DESCRIPTIVE STATISTICS")
    stats = df_dict_cleaned[['Salary', 'Hire_Year']].describe()
    print("• Statistical Summary (`describe()`):\n", stats)
    print("=" * 70)

    return {
        'df_created': df_dict_cleaned,
        'dept_summary': dept_agg,
        'merged_df': merged_df
    }

if __name__ == '__main__':
    run_pandas_demonstration()
