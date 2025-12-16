import csv

# save a record into CSV file
def save_record(rec):
    with open("leave_records.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([rec.emp_id, rec.dept, rec.date])

# read all records from CSV
def read_records():
    try:
        with open("leave_records.csv", "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except:
        return []
