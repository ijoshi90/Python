def print_line_coverage(lcov_file):
    files = []
    total_lines = []
    covered_lines = []
    line_coverage = []

    with open(lcov_file, 'r') as f:
        file_coverage = {}
        for line in f:
            line = line.strip()
            if line.startswith('SF:'):
                # Extract the file name from the line
                file_name = line.split(':')[1].strip()
                file_coverage[file_name] = {'total_lines': 0, 'covered_lines': 0}
            elif line.startswith('DA:'):
                # Extract the line number and execution count
                line_data = line.split(',')
                if len(line_data) >= 2:
                    line_number = line_data[0].split(':')[1]
                    execution_count = int(line_data[1])
                    # Update the line coverage for the file
                    file_coverage[file_name]['total_lines'] += 1
                    if execution_count > 0:
                        file_coverage[file_name]['covered_lines'] += 1
                else:
                    print(f'Skipping line: {line}')
            elif line == 'end_of_record':
                pass

    # Print the line coverage for each file and append to lists
    for file_name, coverage in file_coverage.items():
        total = coverage['total_lines']
        covered = coverage['covered_lines']
        line_coverage_percentage = (covered / total) * 100 if total > 0 else 0

        files.append(file_name)
        total_lines.append(total)
        covered_lines.append(covered)
        line_coverage.append(line_coverage_percentage)

    return files, total_lines, covered_lines, line_coverage

# Example usage
lcov_info_file = 'lcov.info'
files, total_lines, covered_lines, line_coverage = print_line_coverage(lcov_info_file)

for count in range(len(files)):
    print("File : {}".format((files[count])))
    print("Total Lines : {}".format((total_lines[count])))
    print("Covered Lines : {}".format((covered_lines[count])))
    print("Line Coverage : {}\n".format((line_coverage[count])))