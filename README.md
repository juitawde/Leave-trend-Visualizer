# 📊 Employee Leave Trend Visualizer

## 📌 Project Overview

The **Leave Management Analyzer** is a Python-based mini project that records employee leave data, analyzes absence patterns, predicts peak leave periods using basic analytics, and visualizes trends across months and departments.

This project demonstrates the practical use of **Python fundamentals, file handling, data analysis, visualization, and automation concepts**.

---

## 🎯 Objectives

* Record employee leave data in a structured format
* Analyze historical leave patterns
* Identify peak leave months
* Visualize department-wise leave trends
* Generate summary reports automatically

---

## 🧩 Features

* 📥 Store leave records in CSV format
* ✅ Validate leave entries using a **decorator**
* 📈 Monthly leave trend visualization (Histogram)
* 🏢 Department-wise leave analysis (Bar chart)
* 🔍 Identify frequent leave takers
* 🧮 Peak leave month detection using **lambda**
* 📄 Summary report generation in **JSON format**

---

## 🛠️ Technologies Used

* **Python**
* **CSV File Handling**
* **Matplotlib**
* **Collections Module**
* **JSON**
* **VS Code**

---

## 📂 Project Structure

```
leave_project/
│
├── leave_visualizer_main.py   # Main execution file
├── leave_record.py            # LeaveRecord class
├── leave_utils.py             # Utility functions (CSV handling)
├── leave_records.csv          # Stored leave data
├── leave_summary.json         # Auto-generated summary
└── README.md                  # Project documentation
```

---

## ▶️ How to Run the Project

1. Open the project folder in **VS Code**
2. Make sure Python is installed
3. Run the main file:

   ```bash
   python leave_visualizer_main.py
   ```
4. Enter employee leave details when prompted
5. View generated graphs and summary output

---

## 📊 Visualizations

* **Monthly Leave Trend** – Histogram showing leave distribution by month
* **Department-wise Leaves** – Bar graph showing total leaves per department

---

## ⚙️ Automation Concepts Used

* **Decorator** → Validates leave data before saving
* **Lambda Function** → Calculates peak leave month
* **List Comprehension** → Identifies frequent leave takers

---

## 📈 Sample Output

* Peak Leave Month
* Total Leaves Recorded
* Department-wise Leave Count
* JSON Summary File

---

## ⚠️ Limitations

* No authentication or login system
* No concurrency handling (single-user system)
* Uses CSV instead of database
* No machine learning-based prediction (future scope)

---

## 🚀 Future Enhancements

* Add login & authentication
* Use database instead of CSV
* Add machine learning for leave prediction
* Web-based interface
* Role-based access (Admin / Employee)

---

## 📚 Learning Outcomes

* Understanding Python file handling
* Working with decorators and lambda functions
* Data visualization using matplotlib
* Modular project design
* Real-world data analysis workflow

---

## 👩‍💻 Author

**Jui Sudhir Tawde**

---

## ✅ Conclusion

This project successfully demonstrates how Python can be used to build a simple yet effective leave management analyzer that provides meaningful insights through data analysis and visualization.
