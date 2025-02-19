import sys
from pathlib import Path
from collections import deque

# Function to parse a log line
def parse_log_line(line: str) -> dict[str: str]:
    """
    Parses a log line

    Parameters:
        line (str): a string with log data
    
    Returns:
        dict[str: str]: a dictionary with parsed data
    """
    log_dict = {}
    log_list = deque(line.split())
    log_dict["date"] = log_list.popleft()
    log_dict["time"] = log_list.popleft()
    log_dict["level"] = log_list.popleft()
    log_dict["message"] = " ".join(list(log_list))
    return log_dict

# Function to load and parse log data
def load_logs(file_path: str) -> list[dict[str: str]]:
    """
    Loads and parses log data

    Parameters:
        file_path (str): a string with path to file with log data
    
    Returns:
        list[dict[str: str]]: a list of dictionaries with parsed data
    """
    try:
        with open(file_path, "r", encoding="utf-8") as log_file:
            log_list = []
            for line in log_file:
                log_list.append(parse_log_line(line))
            return log_list
    # File not found
    except FileNotFoundError:
        print("File not found")
        return []
    # File contains data that cannot be processed
    except IndexError:
        print("Data cannot be processed")
        return []
    # Wrong path to file
    except OSError:
        print("Wrong path to file")
        return []

# Function to filter logs by level
def filter_logs_by_level(logs: list[dict[str: str]], level: str) -> list[dict[str: str]]:
    """
    Filters logs by levels

    Parameters:
        logs (list[dict[str: str]]): list of dictionaries with log data
        level (str): level by which logs must be filtered 
    
    Returns:
        list[dict[str: str]]: list of dictionaries filtered by level
    """
    return list(filter(lambda elem: elem["level"] == level, logs))

# Function to count logs for each level
def count_logs_by_level(logs: list[dict[str: str]]) -> dict[str: int]:
    """
    Counts logs for each level

    Parameters:
        logs (list[dict[str: str]]): list of dictionaries with log data
    
    Returns:
        dict[str: int]: a dictionary with number of logs for each level
    """
    count_dict = {}
    for log in logs:
        if log["level"] in count_dict:
            count_dict[log["level"]] += 1
        else:
            count_dict[log["level"]] = 1
    return count_dict

# Function to display log counts
def display_log_counts(counts: dict[str: int]):
    """
    Displays number of logs for each level

    Parameters:
        counts (dict[str: int]): dictionary with number of logs for each level
    """
    level_column_width = 11
    number_column_width = 8
    print("\n" + "Log level:".ljust(level_column_width) + "| " + "Number:".ljust(number_column_width))
    print("-" * level_column_width + "|-" + "-" * number_column_width)
    for level, number in counts.items():
        print(f"{level}".ljust(level_column_width) + "| " + f"{number}".ljust(number_column_width))
    print()

# Function to display log details for a given level
def display_log_details(logs: list[dict[str: str]], level: str):
    """
    Displays log details for a given level

    Parameters:
        logs (list[dict[str: str]]): list of dictionaries with log data
        level (str): level for which log details must be displayed
    """
    normalized_level = level.upper()
    if normalized_level in count_logs_by_level(logs):
        print(f"Logs for {normalized_level}:\n")
        for log in filter_logs_by_level(logs, normalized_level):
            print(f"{log["date"]} {log["time"]} - {log["message"]}")
    else:
        print(f"No data found for \"{level}\"")
    print()

# Main function
def main():
    """
    Reads log data and displays relevant information
    """
    args = sys.argv
    file_path = Path(args[1])
    logs = load_logs(file_path)
    if logs:
        counts = count_logs_by_level(logs)
        # print(filter_logs_by_level(logs, "INFO"), end="\n\n")
        # print(counts, end="\n\n")
        display_log_counts(counts)
        if len(args) >= 3:
            display_log_details(logs, args[2])

if __name__ == "__main__":
    main()
