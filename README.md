# CSC302-Group10-Final
 
## Contributors

- [@Cameron Bentz](https://github.com/cambentz)
- [@Patrick Hill](https://github.com/xversaumich) 
- [@Ben Surgalski](https://github.com/bsurgalski) 

## Project Overview

This project explores trends in U.S. college tuition rates and student loan debt using data from the U.S. Department of Education's College Scorecard. Our goal is to analyze:
- Rising tuition and net cost of attendance
- Trends in student loan debt over time
- Correlations between tuition, debt, earnings, and institution types
- Potential inequalities based on school type, size, or location

We use **Python** for data cleaning, manipulation, and visualization, and **R** for statistical modeling and deeper analysis.

---

## Presentation Slides: https://docs.google.com/presentation/d/1WqQS7duh_HtHok34N6hXmt1btJlvic_wY-7f5PC8olQ/edit?usp=sharing

## Dataset Info

- **Source**: [Kaggle Dataset – Comprehensive U.S. College Scorecard Data](https://www.kaggle.com/datasets/programmerrdai/comprehensive-u-s-college-scorecard-data)
- **Maintained by**: U.S. Department of Education
- **Includes**:
  - Tuition, net cost, student debt, earnings
  - Institution-level demographics
  - Graduation and enrollment stats
  - Longitudinal data for multiple years
  - Crosswalk directory for metadata/definitions

---

##  Setup Instructions

### 1. Clone this repository

### 2. Install dependencies
``` python
pip install -r requirements.txt
```

### 3. Set up Kaggle API

1. Sign in to your Kaggle account  
2. Go to: https://www.kaggle.com/settings  
3. Click **"Create New API Token"** – this will download `kaggle.json`  
4. Place the file here:

```
C:\Users<your-username>\.kaggle\kaggle.json
```

## Download the Dataset

Run the script below to automatically download the dataset and move it into the `data/raw/` directory.

``` python
python scripts/python/data_download.py
```
