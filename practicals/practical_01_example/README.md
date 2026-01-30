# Practical 01: Introduction to Data Analysis with Pandas

## Objective
Learn the basics of data loading, exploration, and simple analysis using Pandas.

## Problem Statement
You are given a sample dataset containing information about students and their grades. Your task is to:
1. Load the dataset into a Pandas DataFrame
2. Display basic information about the dataset
3. Calculate summary statistics
4. Answer specific questions about the data

## Tasks

### Task 1: Load and Explore Data
- Load the CSV file from the `data/` directory
- Display the first 10 rows
- Show the data types and null values
- Get basic statistics

### Task 2: Data Analysis
- Find the average grade for each subject
- Identify the top 5 students by overall average
- Count students by grade category (A, B, C, etc.)

### Task 3: Simple Visualization
- Create a bar chart showing average grades by subject
- Create a histogram of the overall grade distribution

## Dataset
The dataset `students.csv` contains:
- `student_id`: Unique identifier
- `name`: Student name
- `math`: Math grade (0-100)
- `science`: Science grade (0-100)
- `english`: English grade (0-100)

## Expected Output
Your solution should print:
1. Dataset summary
2. Answers to each analysis question
3. Generated visualizations saved as PNG files

## How to Run
```bash
python solution.py
```

Or use Jupyter Notebook:
```bash
jupyter notebook solution.ipynb
```

## Learning Outcomes
- Understand Pandas DataFrame operations
- Perform basic statistical analysis
- Create simple visualizations with Matplotlib

## Time Estimate
30-45 minutes
