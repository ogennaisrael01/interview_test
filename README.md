## Overview
This project performs several operations including:

- Extracting and processing colour data from an HTML table
- Counting colour frequencies
- Computing statistical values (mean, median, mode, variance)
- Generating Fibonacci numbers
- Converting random binary numbers to base 10
- Searching numbers within a list
- Saving processed data into a PostgreSQL database

---

## 🛠 Features

### **1. HTML Table Extraction**
The `extract_html()` function loads an HTML file, extracts the first table, and retrieves all colour values.

### **2. Colour Analysis**
The following functions process colour frequency:
- `colour_counts()` – counts how many times each colour appears  
- `colours_mode()` – finds the most frequent colour  
- `colours_median()` – computes median position  
- `calculate_variance()` – computes variance of colour frequencies  

### **3. Fibonacci Sequence**
`sum_fibonacci(number)` generates Fibonacci numbers up to a given maximum and returns both the sequence and its sum.

### **4. Binary Utilities**
`random_number()` generates a random 4-bit binary number and converts it to base-10.

### **5. Number Search**
`search()` recursively searches for user-provided input in a list of numbers.

### **6. PostgreSQL Database Storage**
`save_to_db()` inserts calculated colour frequencies into a PostgreSQL table.

---

## Requirements

Ensure these Python packages are installed:

pandas
psycopg2
random
time

Copy code

---

## Project Structure

project/
│
├── python_class_question.py
├── python_class_question.html
└── README.md

yaml
Copy code

---

## Running the Project

Run the main script:

```bash
python3 python_class_question.py