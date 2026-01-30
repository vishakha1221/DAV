"""
Practical 01: Introduction to Data Analysis with Pandas
Solution Template

Author: [Your Name]
Date: [Date]
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(filepath):
    """Load the dataset from CSV file"""
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def explore_data(df):
    """Display basic information about the dataset"""
    print("\n=== Dataset Overview ===")
    print(f"Shape: {df.shape}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    print(f"\nData types:")
    print(df.dtypes)
    print(f"\nNull values:")
    print(df.isnull().sum())
    print(f"\nBasic statistics:")
    print(df.describe())

def analyze_data(df):
    """Perform data analysis tasks"""
    print("\n=== Data Analysis ===")
    
    # Task 1: Average grade for each subject
    print("\n1. Average grades by subject:")
    avg_grades = df[['math', 'science', 'english']].mean()
    print(avg_grades)
    
    # Task 2: Calculate overall average for each student
    df['overall_avg'] = df[['math', 'science', 'english']].mean(axis=1)
    print("\n2. Top 5 students by overall average:")
    top_students = df.nlargest(5, 'overall_avg')[['name', 'overall_avg']]
    print(top_students)
    
    # Task 3: Grade categories
    def categorize_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    df['grade_category'] = df['overall_avg'].apply(categorize_grade)
    print("\n3. Students by grade category:")
    print(df['grade_category'].value_counts().sort_index())
    
    return df

def visualize_data(df):
    """Create visualizations"""
    print("\n=== Creating Visualizations ===")
    
    # Visualization 1: Bar chart of average grades by subject
    plt.figure(figsize=(10, 6))
    avg_grades = df[['math', 'science', 'english']].mean()
    avg_grades.plot(kind='bar', color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    plt.title('Average Grades by Subject', fontsize=14, fontweight='bold')
    plt.xlabel('Subject')
    plt.ylabel('Average Grade')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('average_grades_by_subject.png', dpi=300, bbox_inches='tight')
    print("Saved: average_grades_by_subject.png")
    plt.close()
    
    # Visualization 2: Histogram of overall grade distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['overall_avg'], bins=20, color='#95E1D3', edgecolor='black')
    plt.title('Distribution of Overall Grades', fontsize=14, fontweight='bold')
    plt.xlabel('Overall Average Grade')
    plt.ylabel('Number of Students')
    plt.axvline(df['overall_avg'].mean(), color='red', linestyle='--', 
                label=f'Mean: {df["overall_avg"].mean():.2f}')
    plt.legend()
    plt.tight_layout()
    plt.savefig('grade_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: grade_distribution.png")
    plt.close()

def main():
    """Main function to run the practical"""
    print("=" * 50)
    print("Practical 01: Data Analysis with Pandas")
    print("=" * 50)
    
    # Load data
    df = load_data('data/students.csv')
    
    if df is not None:
        # Explore data
        explore_data(df)
        
        # Analyze data
        df = analyze_data(df)
        
        # Visualize data
        visualize_data(df)
        
        print("\n" + "=" * 50)
        print("Analysis Complete!")
        print("=" * 50)

if __name__ == "__main__":
    main()
