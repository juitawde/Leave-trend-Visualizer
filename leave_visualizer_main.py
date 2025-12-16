import json
import leave_record
import leave_utils
import matplotlib.pyplot as plt
import collections


#DECORATOR for validation
def validate_leave(func):
    def wrapper(rec):
        if rec.emp_id and rec.dept and rec.date:
            return func(rec)
        else:
            print("Invalid Leave Entry")
    return wrapper


# decorate save_record inside this file
save_record = validate_leave(leave_utils.save_record)



# === record a leave ===
emp = input("Enter Employee ID: ")
dept = input("Enter Department: ")
date = input("Enter Date (YYYY-MM-DD): ")

rec = leave_record.LeaveRecord(emp, dept, date)
save_record(rec)

print("\nLeave saved!")



# ANALYSIS

records = leave_utils.read_records()


# ---- EXTRACT MONTHS ----
months = [
    int(r[2].split("-")[1])
    for r in records 
    if len(r) >=3 and r[2] and "-" in r[2]
]


# ===== Lambda to find peak month =====
peak_month = max(set(months), key=lambda m: months.count(m))
print("Peak leave month:", peak_month)



# ---- Monthly Plot ----
plt.figure(figsize=(6,4))
plt.hist(months, bins=range(1,14), edgecolor='black')
plt.xticks(range(1,13))
plt.xlabel("Month")
plt.ylabel("Leaves")
plt.title("Leave Trend")
plt.show()

 
# ===== Department plot =====

depts = [r[1] for r in records]
dept_counts = collections.Counter(depts)

plt.figure(figsize=(6,4))
plt.bar(dept_counts.keys(), dept_counts.values(), color='orange')
plt.xlabel("Department")
plt.ylabel("Leave Count")
plt.title("Leaves per Department")
plt.show()


summary = {
    "total_leaves": len(records),
    "peak_month": peak_month,
    "department": dict(dept_counts)
}

with open("leave_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("\nSummary saved in leave_summary.json")


# ===== Frequent Leave Takers =====
employees = [r[0] for r in records]

freq = {emp: employees.count(emp) for emp in set(employees)}  

frequent = [emp for emp, count in freq.items() if count >= 2]  

print("\nFrequent leave takers:", frequent)
