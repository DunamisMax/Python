#!/usr/bin/env python3


def parse_file_without_strip(filepath):
    with open(filepath, "r") as f:
        for line in f:
            columns = line.split()  # Splitting on a single space
            print(repr(line), columns, len(columns))


def parse_file_with_strip(filepath):
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespace
            columns = line.split(" ")  # Splitting on a single space
            print(repr(line), columns, len(columns))


def main():
    print("Without using strip():")
    parse_file_without_strip("data.txt")

    print("\nWith using strip():")
    parse_file_with_strip("data.txt")


if __name__ == "__main__":
    main()
