# Workers Salary Prediction Model

Welcome to the Workers Salary Prediction Model project! This repository provides a comprehensive approach for analyzing and predicting workers' salaries using various machine learning techniques. The project is presented in a Jupyter Notebook, which walks through data preprocessing, exploratory data analysis (EDA), feature engineering, model building, and evaluation.

## Author
**By Adedara Ademola**

---

## Project Overview

This model aims to predict workers' salaries based on multiple features, such as age, gender, education level, job title, and years of experience. The project includes steps for data cleaning, analysis, visualization, and training a linear regression model.

### Key Steps in the Analysis

1. **Data Import & Preprocessing**
   - Importing necessary libraries (pandas, numpy, seaborn, matplotlib, scikit-learn)
   - Loading the salary dataset
   - Handling missing values and duplicates

2. **Exploratory Data Analysis (EDA)**
   - Statistical summaries
   - Categorical feature value counts
   - Data visualization (bar plots, scatter plots, line plots)

3. **Feature Engineering**
   - Encoding categorical variables
   - Selecting relevant features for modeling

4. **Model Building & Evaluation**
   - Splitting data into training and test sets
   - Training a linear regression model
   - Evaluating model performance (MSE, RMSE, R², MAE)
   - Model serialization (pickle)

5. **Visualization**
   - Relationship between salary and features (education, job title, experience, age)
   - Insights from graphical analysis

---

## Getting Started

To run this project, you need:

- Python 3.x
- Jupyter Notebook
- Required Python packages: pandas, numpy, seaborn, matplotlib, scikit-learn, pickle

### Installation

Install required packages via pip:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

---

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    ```
2. Open `Demmy_Salary_Analysis.ipynb` in Jupyter Notebook.
3. Run the cells sequentially to follow the data analysis and prediction workflow.

---

## Data

The project uses a CSV file named `Salary Data.csv`, which contains the following columns:

- Age
- Gender
- Education Level
- Job Title
- Years of Experience
- Salary

Ensure this file is placed in the same directory as the notebook.

---

## Results

- The notebook provides insights into factors affecting salary.
- The trained model can be used to predict salaries for new data based on the selected features.

---

## Visualization Samples

- **Bar plots** for salary by education and gender
- **Scatter plots** for salary by job title
- **Line plots** for salary by years of experience

---

## License

This project is open-source and available under the MIT License.

---

## Contact

For questions, suggestions, or contributions, feel free to contact [Adedara Ademola](https://github.com/AdemolaAdedara).
