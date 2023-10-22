#!/usr/bin/python3
"""
log parsing
"""

import sys
import re
from collections import defaultdict

# Regular expression to match the input format
log_format = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

total_size = 0
status_code_count = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_format.match(line)
        if match:
            ip, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            status_code_count[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print(f'Total file size: {total_size}')
                for code in sorted(status_code_count.keys()):
                    print(f'{code}: {status_code_count[code]}')

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("Keyboard interruption detected. Printing statistics:")
    print(f'Total file size: {total_size}')
    for code in sorted(status_code_count.keys()):
        print(f'{code}: {status_code_count[code}')
