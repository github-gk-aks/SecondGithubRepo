import openpyxl
import sys
import os
import glob

def replace_strings(excel_path, repo_path):
    # Load Excel file
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb.active

    # Get list of YML files
    yml_files = glob.glob(os.path.join(repo_path, '.github/workflows/*.yml'))
   
    # Iterate through YML files
    for yml_file in yml_files:
        with open(yml_file, 'r') as f:
            content = f.read()

        # Iterate through Excel rows
        for row in sheet.iter_rows(min_row=2, values_only=True):
            original_string = row[0]
            replacement_string = row[1]

            # Replace strings in YML content
            content = content.replace(original_string, replacement_string)

        # Write back to the YML file
        with open(yml_file, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    excel_file = sys.argv[1] if len(sys.argv) > 1 else 'files/File-Replacement.xlsx'
    github_workspace = sys.argv[2] if len(sys.argv) > 2 else '.'

    replace_strings(excel_file, github_workspace)
