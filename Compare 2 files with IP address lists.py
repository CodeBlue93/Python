file1 = 'file1.txt'
file2 = 'file2.txt'

outfile  = 'outfile.txt'

# Read the contents of file1 into a list
with open(file1, 'r') as f:
    file1_contents = f.readlines()

# Read the contents of file2 into a list
with open(file2, 'r') as f:
    file2_contents = f.readlines()

# Create dictionaries to store the contents of each file
file1_counts = {}
file2_counts = {}

# Count the number of occurrences of each IP in file1
for item in file1_contents:
    item = item.strip()
    if item in file1_counts:
        file1_counts[item] += 1
    else:
        file1_counts[item] = 1

# Count the number of occurrences of each IP in file2
for item in file2_contents:
    item = item.strip()
    if item in file2_counts:
        file2_counts[item] += 1
    else:
        file2_counts[item] = 1

# Find the duplicates between the two files
duplicates = set(file1_counts.keys()).intersection(file2_counts.keys())

# Write the duplicates and their count for each file to the output file
with open(outfile, 'w') as f:
    if len(duplicates) == 0:
        f.write("There are no duplicates between the two files.")
    else:
        f.write("The following duplicates were found between the two files:\n")
        for duplicate in duplicates:
            f.write(f"{duplicate} was found {file1_counts[duplicate]} time(s) in {file1} and {file2_counts[duplicate]} time(s) in {file2}\n")
        f.write(f"Total duplicates: {len(duplicates)}")
