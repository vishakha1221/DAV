# Getting Started with DAV Practicals

Welcome to the Data Visualization & Analytics practicals repository! This guide will help you set up your environment and get started with the exercises.

## Prerequisites

Before you begin, make sure you have:
- Python 3.8 or higher installed
- pip (Python package manager)
- A text editor or IDE (VS Code, PyCharm, Jupyter Notebook, etc.)
- Git (for version control)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/vishakha1221/DAV.git
cd DAV
```

### 2. Create a Virtual Environment (Recommended)

Creating a virtual environment helps keep your dependencies isolated:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

This will install all necessary libraries including:
- Pandas (for data manipulation)
- NumPy (for numerical operations)
- Matplotlib (for plotting)
- Seaborn (for statistical visualization)
- Plotly (for interactive plots)
- Jupyter (for notebooks)
- Scikit-learn (for machine learning)

### 4. Verify Installation

Run the following command to verify everything is installed:

```python
python -c "import pandas as pd; import numpy as np; import matplotlib; import seaborn; print('All packages installed successfully!')"
```

## Working with Practicals

### Directory Structure

Each practical is organized as follows:
```
practical_XX/
├── README.md           # Instructions and problem statement
├── data/              # Dataset files
├── solution.py        # Python solution
└── solution.ipynb     # Jupyter notebook (optional)
```

### Running a Practical

1. Navigate to the practical directory:
```bash
cd practicals/practical_01_example
```

2. Read the README.md for instructions

3. Run the Python script:
```bash
python solution.py
```

Or open in Jupyter Notebook:
```bash
jupyter notebook solution.ipynb
```

## Using Jupyter Notebooks

Jupyter notebooks provide an interactive environment for data analysis:

1. Start Jupyter:
```bash
jupyter notebook
```

2. Your browser will open with the Jupyter interface

3. Navigate to the `notebooks/` directory

4. Create a new notebook or open an existing one

## Tips for Success

1. **Read the README First**: Each practical has detailed instructions
2. **Understand the Data**: Always explore your dataset before analysis
3. **Comment Your Code**: Make your code readable for future reference
4. **Experiment**: Try different approaches and visualizations
5. **Ask Questions**: Don't hesitate to search for help online

## Common Commands

### Package Management
```bash
pip install package_name          # Install a package
pip install --upgrade package_name # Update a package
pip list                          # List installed packages
pip freeze > requirements.txt     # Save current packages
```

### Jupyter Notebook
```bash
jupyter notebook                  # Start Jupyter
jupyter lab                       # Start JupyterLab (modern interface)
jupyter notebook --port 8889      # Start on different port
```

## Troubleshooting

### Issue: Package not found
**Solution**: Make sure your virtual environment is activated and run `pip install -r requirements.txt`

### Issue: Port already in use (Jupyter)
**Solution**: Use a different port: `jupyter notebook --port 8889`

### Issue: Matplotlib plots not showing
**Solution**: Add `plt.show()` at the end of your plotting code, or use `%matplotlib inline` in Jupyter

### Issue: Import errors
**Solution**: Restart your kernel/Python interpreter after installing packages

## Next Steps

1. Start with `practical_01_example` to understand the structure
2. Work through practicals sequentially
3. Refer to the `resources/` directory for additional help
4. Create your own projects in the `projects/` directory

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)

## Need Help?

- Check the `resources/` directory for helpful materials
- Search Stack Overflow for specific errors
- Refer to official documentation
- Review example code in the repository

Happy Learning! 🎓📊
