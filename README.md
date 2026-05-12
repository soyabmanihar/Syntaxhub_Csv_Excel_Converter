# 🚀 CSV to Excel Converter

Transform raw CSV files into clean, structured Excel reports with ease.  
This Python-powered CLI tool automates data cleaning, formatting, and Excel conversion in just one command.

---

# ✨ Key Features

- 📂 Import CSV files quickly and efficiently
- 📊 Generate professional Excel (`.xlsx`) reports
- 🧹 Automatically clean and standardize column names
- ⚡ Detect and handle missing values intelligently
- 📅 Safely parse and format date columns
- 🗂 Remove duplicate records automatically
- 📝 Rename columns for cleaner datasets and reporting
- 📌 Simple and beginner-friendly command-line interface
- 📁 Built-in logging system for tracking operations
- ❌ Reliable error handling for invalid or corrupted files

---

# 🛠 Built With

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core development |
| 📊 pandas | Data analysis & transformation |
| 📗 openpyxl | Excel file generation |
| ⚙ argparse | Command-line argument handling |
| 📝 logging | Activity & error logging |
| 📂 os | File and directory management |

---

# 📁 Project Structure

```text
Syntaxhub_Csv_Excel_Converter/
│
├── converter.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── samplecsv/
│   ├── customers.csv
│   ├── employees.csv
│   ├── inventory.csv
│   ├── sales.csv
│   └── students.csv
│
├── output/
│
├── logs/
│   └── converter.log
```

---

# ⚡ Quick Setup

## 📥 Clone the Repository

```bash
git clone https://github.com/soyabmanihar/Syntaxhub_Csv_Excel_Converter.git
```

## 📂 Navigate to the Project

```bash
cd Syntaxhub_Csv_Excel_Converter
```

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Converter

## 🔹 Basic Conversion

```bash
python converter.py -i samplecsv/employees.csv -o output/output.xlsx
```

---

## 🔹 Rename Columns While Converting

```bash
python converter.py -i samplecsv/employees.csv -o output/output.xlsx -r "name=employee_name,salary=monthly_salary"
```

---

# 📈 What This Tool Automates

✅ CSV to Excel conversion  
✅ Data cleaning and normalization  
✅ Missing value handling  
✅ Date formatting and parsing  
✅ Duplicate row removal  
✅ Logging and reporting  
✅ Automated Excel export  

---

# 📝 Logging System

All processing activities are automatically recorded inside:

```text
logs/converter.log
```

### 📌 Example Log Output

```text
INFO - Reading CSV file...
INFO - Cleaning dataset...
INFO - Parsing date columns...
INFO - Exporting to Excel...
INFO - Conversion completed successfully.
```

---

# 📚 Required Libraries

```text
pandas
openpyxl
```

---

# 📦 Included Sample Datasets

- 📄 customers.csv
- 📄 employees.csv
- 📄 inventory.csv
- 📄 sales.csv
- 📄 students.csv

---

# 🌐 Repository

https://github.com/soyabmanihar/Syntaxhub_Csv_Excel_Converter

---

# 👨‍💻 Developer

### Soyab Manihar

💡 Passionate about Python automation, data processing, and developer tools.

---

# 📜 License

🆓 Open-source project available under the **MIT License**.
