import pandas as pd
from openpyxl import Workbook

# Load employee data
file_path = r"C:\Users\naman\OneDrive\Desktop\employees.csv"
employees = pd.read_csv(file_path)

# Define tax slabs and rates
def calculate_tax(salary):
    if salary <= 400000:
        return 0
    elif salary <= 800000:
        return salary * 0.05
    elif salary <= 1200000:
        return salary * 0.10
    elif salary <= 1600000:
        return salary * 0.15
    elif salary <= 2000000:
        return salary * 0.20
    elif salary <= 2400000:
        return salary * 0.25
    else:
        return salary * 0.30

# Define Provident Fund Rate
PF_RATE = 0.08  # 8% PF

# Ensure 'Salary' column is numeric
employees["Salary"] = pd.to_numeric(employees["Salary"], errors='coerce')

# Apply tax and deductions
employees["Annual Salary"] = employees["Salary"] * 12
employees["Annual Salary"] = pd.to_numeric(employees["Annual Salary"], errors='coerce')  # Convert to numeric
employees["Tax"] = employees["Annual Salary"].apply(calculate_tax)
employees["PF"] = employees["Annual Salary"] * PF_RATE
employees["Net Annual Salary"] = employees["Annual Salary"] - (employees["Tax"] + employees["PF"])
employees["Monthly Net Salary"] = employees["Net Annual Salary"] / 12

# Save payroll report to Excel
output_file = "payroll_report.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    employees.to_excel(writer, sheet_name='Payroll Report', index=False)

print(" Payroll processing complete! Payslips saved in 'payroll_report.xlsx'.")
