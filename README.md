# Student Grade Analyzer

A Python program that analyzes student performance using NumPy — calculates 
class statistics, ranks students, assigns letter grades, and flags students 
who failed, all using vectorized NumPy operations instead of manual loops.

## Features
- Calculates average, median, and standard deviation of class scores
- Identifies the highest and lowest scoring student
- Flags students who scored below the passing threshold
- Assigns letter grades (A/B/C/D/F) based on score ranges
- Ranks and displays all students from highest to lowest score

## Tech Stack
- Python
- NumPy

## How to Run

**1. Clone this repository**
`````
git clone https://github.com/Vaibhavi1007/student-grade-analyzer.git
cd student-grade-analyzer
``````

**2. Create and activate a virtual environment**
```````
python -m venv venv
venv\Scripts\activate
````````

**3. Install dependencies**
`````````
pip install -r requirements.txt
``````````

**4. Run the program**
`````````
python gradeanalyzer.py
``````````

**5. Enter the number of students, then their names and marks when prompted**

## Sample Output
Highest Marks: vai = 98

Lowest Marks: shri = 23

Failed Students:

['sam' 'shri'] = [39 23]
---Class Report---

Average: 67.33

Highest: 98

Lowest: 23
--Final Report--

vai:98 Grade: A

om:89 Grade: B

san:88 Grade: B

sai:67 Grade: C

sam:39 Grade: F

shri:23 Grade: F

## What I Learned
Converted an original plain-Python version (using dictionaries, manual loops, 
and `sorted()`) into a NumPy-based version using vectorized operations: 
`np.argmax`/`np.argmin` for finding top/bottom scorers, boolean masking for 
filtering failed students, and `np.argsort` for ranking — eliminating manual 
loops in favor of array-based logic.
