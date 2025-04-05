def create_sample_log_file():

    sample_logs = """[INFO] Server started at 10:00 AM
[WARNING] High memory usage detected
[INFO] User login successful
[ERROR] Database connection failed
[ERROR] Timeout occurred
[INFO] Job completed
[WARNING] Disk space low
"""
    with open("sample_log.txt", "w") as file:
        file.write(sample_logs)
    print("Sample log file 'sample_log.txt' created.\n")


def analyze_log_file(file_path):
    error_count = 0
    warning_count = 0
    total_lines = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                total_lines += 1
                if "ERROR" in line:
                    error_count += 1
                if "WARNING" in line:
                    warning_count += 1

        print("Log Analysis Report:")
        print(f"Total Lines     : {total_lines}")
        print(f"Error Entries   : {error_count}")
        print(f"Warning Entries : {warning_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the path.")


if __name__ == "__main__":
    print("Log File Analyzer Tool\n")
    create_sample_log_file()
    analyze_log_file("sample_log.txt")
