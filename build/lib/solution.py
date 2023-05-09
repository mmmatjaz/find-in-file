import os
import re
import sys


def get_last_line(file):
    with open(file, "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        return file.readline().decode()


def proc_file(fname):
    search_term = get_last_line(fname)
    solution = []
    with open(fname, 'r') as f:
        num_lines = sum(1 for _ in f)

    with open(fname, 'r') as f:
        for i,line in enumerate(f):
            if i==num_lines-1:
                break
            #print(line.strip())
            if search_term in line.strip():
                words = [w for w in re.split('[^a-zA-Z]', line) if len(w)>0]
                solution.append("[" + " ".join(words) + "]")
    return solution


def main():
    print("\n".join(proc_file(sys.argv[1])))
    #return )


if __name__ == "__main__":
    main()
