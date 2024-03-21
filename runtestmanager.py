import subprocess
import time
import os
import re

def replace_tsfname_in_batch_script(batch_script_path, new_tsfname):
    try:
        # Read the contents of the batch script
        with open(batch_script_path, 'r') as file:
            batch_script_content = file.readlines()

        # Find and replace the value of TSFNAME
        for i, line in enumerate(batch_script_content):
            match = re.match(r'^(\s*SET\s+TSFNAME\s*=\s*)\s*(.*?)\s*$', line)
            if match:
                # Update the line with the new TSFNAME value while preserving formatting
                batch_script_content[i] = f"{match.group(1)}{new_tsfname}\n"
                time.sleep(20)
                break

        # Write the modified content back to the file
        with open(batch_script_path, 'w') as file:
            file.writelines(batch_script_content)

        print(f"Value of TSFNAME replaced with '{new_tsfname}' in the batch script.")
    except FileNotFoundError:
        print(f"Error: Batch script '{batch_script_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_batch_script(script_path):
    try:
        # Add delay of 1 minute before running the batch script
        print("Waiting for 30 sec before executing the batch script...")
        time.sleep(30)

        process = subprocess.Popen(script_path, shell=True)
        print("Batch script executed.")
        # Wait for the CM.exe process to finish
        while process.poll() is None:
            time.sleep(1)  # Sleep for 1 second
        print("CM.exe process has finished.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    batch_script_path = os.environ.get('BATCH_SCRIPT_PATH')
    test_series_folder_path = os.environ.get('TEST_SERIES_FOLDER_PATH')

    # Get a list of all .ts files in the directory
    ts_files = [filename for filename in os.listdir(test_series_folder_path) if filename.endswith(".ts")]

    for ts_file in ts_files:
        ts_file_path = os.path.join(test_series_folder_path, ts_file)

        # Replace TSFNAME in the batch script with the current ts file name
        replace_tsfname_in_batch_script(batch_script_path, ts_file)

        # Execute the modified batch script
        run_batch_script(batch_script_path)
