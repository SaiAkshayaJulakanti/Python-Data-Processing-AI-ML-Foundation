"""
NumPy Core Concepts, Multi-dimensional Operations, Slicing & Broadcasting Demonstration.
Fulfills Evaluation Area: NumPy (20 Marks).
"""
import numpy as np

def run_numpy_demonstration():
    """
    Executes a comprehensive demonstration of NumPy fundamentals:
    1. Array Creation & Attribute Inspection
    2. Dimensions, Reshaping & Data Types
    3. Mathematical & Statistical Operations
    4. Indexing, Slicing & Boolean Masking
    5. Broadcasting Rules & Practical Applications
    """
    results = {}
    print("=" * 70)
    print("🧠 NUMPY FUNDAMENTALS & BROADCASTING DEMONSTRATION")
    print("=" * 70)

    # ---------------------------------------------------------
    # 1. Array Creation & Dimensions
    # ---------------------------------------------------------
    print("\n1️⃣ ARRAY CREATION & DIMENSIONS")
    arr_1d = np.array([10, 20, 30, 40, 50])
    arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
    arr_zeros = np.zeros((3, 4))
    arr_ones = np.ones((2, 3), dtype=np.int32)
    arr_range = np.arange(10, 50, 5)
    arr_linspace = np.linspace(0, 1, 5)

    print(f"• 1D Array: {arr_1d} | Shape: {arr_1d.shape} | Dim: {arr_1d.ndim}")
    print(f"• 2D Array:\n{arr_2d}\n  Shape: {arr_2d.shape} | Dim: {arr_2d.ndim} | Dtype: {arr_2d.dtype}")
    print(f"• Zeros (3x4):\n{arr_zeros}")
    print(f"• Range (10 to 50, step 5): {arr_range}")

    results['arr_1d'] = arr_1d
    results['arr_2d'] = arr_2d

    # ---------------------------------------------------------
    # 2. Reshaping & Data Types
    # ---------------------------------------------------------
    print("\n2️⃣ RESHAPING & DATA TYPES")
    arr_flat = np.arange(12)
    arr_reshaped = arr_flat.reshape(3, 4)
    print(f"• Original Flat (12 elements): {arr_flat}")
    print(f"• Reshaped to (3, 4):\n{arr_reshaped}")
    
    results['arr_reshaped'] = arr_reshaped

    # ---------------------------------------------------------
    # 3. Mathematical & Statistical Operations
    # ---------------------------------------------------------
    print("\n3️⃣ MATHEMATICAL & STATISTICAL OPERATIONS")
    salaries = np.array([65000, 85000, 110000, 55000, 95000, 125000])
    
    # Element-wise operations
    tax_deductions = salaries * 0.20
    net_salaries = salaries - tax_deductions
    
    # Statistical Summary
    total_payroll = np.sum(salaries)
    mean_salary = np.mean(salaries)
    std_salary = np.std(salaries)
    min_sal = np.min(salaries)
    max_sal = np.max(salaries)

    print(f"• Base Salaries: {salaries}")
    print(f"• Tax Deductions (20%): {tax_deductions}")
    print(f"• Net Salaries: {net_salaries}")
    print(f"• Total Payroll: ${total_payroll:,.2f}")
    print(f"• Mean Salary: ${mean_salary:,.2f} | Std Dev: ${std_salary:,.2f}")
    print(f"• Min Salary: ${min_sal:,.2f} | Max Salary: ${max_sal:,.2f}")

    results['salaries_stats'] = {
        'total': total_payroll,
        'mean': mean_salary,
        'std': std_salary,
        'min': min_sal,
        'max': max_sal
    }

    # ---------------------------------------------------------
    # 4. Indexing, Slicing & Boolean Masking
    # ---------------------------------------------------------
    print("\n4️⃣ INDEXING, SLICING & BOOLEAN MASKING")
    matrix = np.array([
        [10, 15, 20, 25],
        [30, 35, 40, 45],
        [50, 55, 60, 65]
    ])
    
    sub_slice = matrix[0:2, 1:3]  # Row 0 to 1, Col 1 to 2
    high_value_mask = matrix > 35
    filtered_values = matrix[high_value_mask]

    print(f"• Full Matrix:\n{matrix}")
    print(f"• Slice matrix[0:2, 1:3]:\n{sub_slice}")
    print(f"• Boolean Mask (elements > 35):\n{high_value_mask}")
    print(f"• Filtered Elements (> 35): {filtered_values}")

    results['filtered_values'] = filtered_values

    # ---------------------------------------------------------
    # 5. Broadcasting Rules & Practical Application
    # ---------------------------------------------------------
    print("\n5️⃣ BROADCASTING CONCEPTS & PRACTICAL EXAMPLE")
    # Scenario: 4 Employees across 3 Quarters (4x3 matrix)
    quarterly_performance_scores = np.array([
        [85, 90, 92],  # Emp 1
        [70, 75, 80],  # Emp 2
        [95, 98, 96],  # Emp 3
        [60, 65, 70]   # Emp 4
    ])
    
    # Department adjustment multiplier for each quarter (1x3 vector)
    quarter_weight_multipliers = np.array([1.05, 1.10, 1.15])
    
    # Broadcasting: (4, 3) * (3,) -> (4, 3)
    weighted_scores = quarterly_performance_scores * quarter_weight_multipliers

    print(f"• Original Performance Matrix (4x3):\n{quarterly_performance_scores}")
    print(f"• Quarter Multipliers (1x3): {quarter_weight_multipliers}")
    print(f"• Weighted Performance after Broadcasting (4x3):\n{weighted_scores}")

    results['weighted_scores'] = weighted_scores
    print("=" * 70)
    return results

if __name__ == '__main__':
    run_numpy_demonstration()
