"""Utils for csv operations
"""
import csv


def check_headers(csv_content, expected_headers):
    """ Check that CSV contains expected headers

    Args:
        csv_content:
        expected_headers:

    Returns:

    """
    # create csv reader
    csv_reader = csv.reader(csv_content.splitlines())
    # get first row: headers
    csv_headers = csv_reader.next()

    return csv_headers == expected_headers


def filter_rows(csv_content, column_index, allowed_values):
    """Filter rows of a csv string

    Args:
        csv_content:
        column_index:
        allowed_values:

    Returns:

    """
    # create csv reader
    csv_reader = csv.reader(csv_content.splitlines())
    # get first row: headers
    header = csv_reader.next()
    # filter accessible rows
    accessible_rows = filter(lambda row: row[column_index] in allowed_values, csv_reader)
    # add headers back
    accessible_rows.insert(0, header)
    # build csv from lists of accessible rows
    filtered_csv_content = '\n'.join(map(','.join, accessible_rows))

    return filtered_csv_content
