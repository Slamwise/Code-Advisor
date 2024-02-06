import subprocess
import os

# 1. Linting the file
def lint_code(file_path):
    result = subprocess.run(['pylint', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8') + "\n" + result.stderr.decode('utf-8')

# 2. Checking file execution
def check_execution(file_path):
    try:
        subprocess.run(['python', file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, "Execution successful"
    except subprocess.CalledProcessError as e:
        return False, e.stderr.decode('utf-8')

# 3. Profiling the file
def profile_script(file_path):
    profile_output = file_path.replace('.py', '_profile.lprof')
    subprocess.run(['kernprof', '-l', '-v', file_path], stdout=subprocess.PIPE)
    result = subprocess.run(['python', '-m', 'line_profiler', profile_output], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

# Add this function to your wrapper
def prepare_for_profiling(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in content:
            if 'def ' in line and line.strip().startswith('def '):  # Simple check to add @profile
                file.write('@profile\n')
            file.write(line)

# Wrapper function to lint, check execution, and profile a .py file
def process_file(file_path):
    # Linting
    lint_results = lint_code(file_path)
    print("Linting Results:\n", lint_results)
    
    # Execution Check
    exec_success, exec_message = check_execution(file_path)
    if not exec_success:
        print("Execution Failed:\n", exec_message)
        return  # Stop the process if the file doesn't execute successfully
    
    # Prepare the script for profiling
    prepare_for_profiling(file_path)

    # Profiling
    profile_results = profile_script(file_path)
    print("Profiling Results:\n", profile_results)
    
# Test the functions with a .py file path
file_path = 'test.py'  # Replace with your file path
process_file(file_path)
