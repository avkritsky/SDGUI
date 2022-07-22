

def format_logs_data_for_output(data: str, selected_range: int) -> dict:
    logs_rows_count = 40
    logs_lines = data.split('\n')[::-1]

    ranged_logs_lines = [logs_lines[i: i + logs_rows_count] for i in range(0, len(logs_lines), logs_rows_count)]

    data = {
        'col': [page_index for page_index in range(0, len(ranged_logs_lines), 10)],
        'max_col': len(ranged_logs_lines),
        'logs': ranged_logs_lines[selected_range - 1],
    }

    return data
