import os
import re
import sys


def get_last_line(file_path: str) -> str:
    """
    Returns the contents of the last line
    :param file_path:
    :return:
    """
    with open(file_path, "rb") as file_path:
        try:
            file_path.seek(-2, os.SEEK_END)
            while file_path.read(1) != b'\n':
                file_path.seek(-2, os.SEEK_CUR)
        except OSError:
            file_path.seek(0)
        return file_path.readline().decode().strip()


def process_file(file_path: str) -> list:
    num_lines = 0
    with open(file_path, 'r') as f:
        for _ in f:
            num_lines += 1
    if num_lines < 2:
        raise ValueError("At least two lines required")

    last_line_raw = get_last_line(file_path)
    if len(last_line_raw) == 0:
        raise ValueError("Empty search term")

    search_words = dirty_line_to_words(last_line_raw)
    if len(search_words) != 1:
        raise ValueError("Invalid search term")

    search_term = search_words[0].lower()
    solution = []

    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if i == num_lines - 1:
                break
            # print(line.strip())
            if search_term in line.lower():
                words = dirty_line_to_words(line.strip())
                solution.append("[" + " ".join(words) + "]")
    return solution


def dirty_line_to_words(line: str) -> list:
    """
    Split line into words. Any character that is not a letter is considered a delimiter.
    :param line:
    :return:
    """
    return [w for w in re.split('[^a-zA-Z]', line) if len(w) > 0]


def main():
    if len(sys.argv) != 1:
        print("No file path provided")
        return
    elif len(sys.argv) > 2:
        print("Too many arguments provided")
        return

    path = sys.argv[1]
    if not os.path.exists(path):
        print("File doesn't exist")
        return

    try:
        res = process_file(path)
    except ValueError as e:
        print(e)
    else:
        print("\n".join(res))
    # return )


if __name__ == "__main__":
    main()
