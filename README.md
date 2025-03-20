# Payroll Processing Automation with Python

## Overview
This Python program automates payroll processing by reading employee salary data from an Excel file, applying tax slabs and provident fund deductions, and generating a final payroll report. It eliminates the need for complex IF functions in Excel, making payroll calculations more efficient and error-free.

## Features
- Reads employee salary data from an Excel file
- Applies income tax deductions based on predefined tax slabs
- Calculates provident fund contributions
- Computes net annual and monthly salaries
- Exports the processed payroll data to a structured Excel report

## Tax Slabs Used
| Annual Income Range      | Tax Rate |
|-------------------------|---------|
| Up to Rs. 4,00,000     | NIL     |
| Rs. 4,00,001 - Rs. 8,00,000 | 5%  |
| Rs. 8,00,001 - Rs. 12,00,000 | 10% |
| Rs. 12,00,001 - Rs. 16,00,000 | 15% |
| Rs. 16,00,001 - Rs. 20,00,000 | 20% |
| Rs. 20,00,001 - Rs. 24,00,000 | 25% |
| Above Rs. 24,00,000 | 30% |

## Requirements
Make sure you have the following dependencies installed:
```bash
pip install pandas openpyxl
```

## Usage
1. Place your employee salary data in an Excel file (e.g., `employees.xlsx`).
2. Ensure the file contains a column named `Salary` with the monthly salary of each employee.
3. Run the Python script:
   ```bash
   python payroll_processing.py
   ```
4. The program will generate a new Excel file (`payroll_report.xlsx`) with:
   - Annual Salary
   - Tax Deduction
   - Provident Fund Contribution
   - Net Annual Salary
   - Monthly Net Salary

## Code Explanation
The script:
1. Reads the employee salary data from an Excel file.
2. Defines tax slabs and applies the correct tax rate based on salary.
3. Calculates provident fund deductions at a fixed rate (8%).
4. Computes net salaries after all deductions.
5. Exports the results to a structured Excel report.

## Example Output
| Employee Name | Salary | Annual Salary | Tax | Provident Fund | Net Annual Salary | Monthly Net Salary |
|--------------|--------|--------------|-----|---------------|----------------|----------------|
| John Doe     | 50,000 | 600,000      | 30,000 | 48,000 | 522,000 | 43,500 |
| Jane Smith   | 100,000 | 1,200,000    | 120,000 | 96,000 | 984,000 | 82,000 |

## Future Improvements
- Add support for bonuses and other allowances.
- Implement a GUI for easier data entry and report generation.
- Integrate with payroll software for direct salary disbursement.

## Contributions
Feel free to fork this repository and contribute by adding new features or optimizing the existing code. Pull requests are welcome!

## License
This project is licensed under the MIT License.

