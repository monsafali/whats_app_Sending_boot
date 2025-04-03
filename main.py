import csv

# Read phone numbers
with open("contact.txt", "r") as f:
    phones = [line.strip() for line in f.readlines()]

# Read names
with open("names.txt", "r") as f:
    names = [line.strip() for line in f.readlines()]

# Read CNICs
with open("cnics.txt", "r") as f:
    cnics = [line.strip() for line in f.readlines()]

# Ensure all lists have the same length
if not (len(phones) == len(names) == len(cnics)):
    print("Error: The number of phone numbers, names, and CNICs do not match!")
    exit()

# Write to CSV file
with open("contacts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["phone", "name", "cnic"])  # Header row

    for phone, name, cnic in zip(phones, names, cnics):
        writer.writerow([phone, name, cnic])

print("CSV file 'contacts.csv' created successfully.")
