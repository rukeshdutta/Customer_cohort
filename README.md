
# Customer Cohort Analysis

This project demonstrates how to perform customer cohort analysis using Python. Cohort analysis helps in understanding customer retention patterns and behavior over time by grouping customers based on their first purchase month and tracking their activity in subsequent months.

## Features
- **Synthetic Data Generation**: Generate realistic customer transaction data for analysis.
- **Cohort Analysis**: Calculate and visualize retention rates using cohort-based segmentation.
- **Heatmap Visualization**: Visualize retention rates to identify trends and patterns.

---

## Project Structure
```
.
├── synthetic_data_generator.py   # Script to generate synthetic data
├── cohort_analysis.py            # Script to perform cohort analysis
├── synthetic_cohort_data.csv     # Sample generated dataset (optional)
└── README.md                     # Documentation for the project
```

---

## Requirements
To run this project, you need the following:
- Python 3.7 or higher
- Required libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - faker

Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn faker
```

---

## Usage

### 1. Generate Synthetic Data
Run the `synthetic_data_generator.py` script to create a synthetic dataset. This will generate a CSV file containing customer transaction data with the following fields:
- `customer_id`: Unique identifier for each customer.
- `order_date`: Date of the transaction.
- `revenue`: Transaction revenue.

```bash
python synthetic_data_generator.py
```

### 2. Perform Cohort Analysis
Run the `cohort_analysis.py` script to perform the analysis using the generated dataset. This script:
1. Identifies customer cohorts based on their first purchase date.
2. Calculates retention rates over subsequent months.
3. Generates a heatmap visualization for retention rates.

```bash
python cohort_analysis.py
```

### 3. Visualization
The cohort analysis script produces a heatmap showing customer retention rates. Rows represent cohort months, and columns represent the number of months since the cohort's first purchase.

---

## Sample Output

### Heatmap Visualization
The heatmap shows customer retention rates as percentages:

- **Rows**: Cohort months (e.g., Jan 2023, Feb 2023).
- **Columns**: Months since the first purchase.
- **Cells**: Retention rates.

Example:

| Cohort Month | Month 1 | Month 2 | Month 3 |
|--------------|---------|---------|---------|
| Jan 2023     | 100%    | 80%     | 50%     |
| Feb 2023     | 100%    | 75%     | 60%     |

---

## Customization
You can modify the parameters in `synthetic_data_generator.py` to:
- Adjust the number of customers.
- Change the date range for transactions.
- Set the maximum number of orders per customer.

---

## Future Improvements
- Add support for revenue-based cohort analysis.
- Integrate customer segmentation features.
- Automate analysis for real-world datasets.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments
This project uses the `Faker` library for generating synthetic data and `Seaborn` for data visualization.

--- 

