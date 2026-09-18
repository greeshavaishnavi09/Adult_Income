# Adult Income Data Cleaning and EDA

## Project Overview

This project performs data collection, data cleaning, data validation,
feature engineering, and exploratory data analysis (EDA) using the UCI
Adult Income dataset.

The project combines the official `adult.data` and `adult.test` files
and produces an analysis dataset containing 48,842 census records.

## Problem Statement

Which demographic, education, and work characteristics are associated
with an annual income above USD 50K in this census dataset?

This project is a descriptive analysis. It identifies associations in
the historical dataset and does not prove that a feature causes a
person's income.

## Dataset

Source: UCI Machine Learning Repository - Adult Dataset

The project uses these official files:

- `adult.data`
- `adult.test`

The dataset contains 14 original features and includes both numerical
and categorical variables. Missing categorical values are represented
by `?` in the original files.

## Data Cleaning

The cleaning workflow includes:

1. Downloading the official UCI data files.
2. Combining `adult.data` and `adult.test`.
3. Preserving the original source split.
4. Removing leading and trailing whitespace.
5. Converting `?` and empty text to missing values.
6. Replacing missing `workclass`, `occupation`, and `native_country`
   values with `Unknown`.
7. Converting numeric columns to appropriate numeric types.
8. Validating core numeric values.
9. Auditing duplicate rows.
10. Normalizing the income labels.
11. Creating a numeric `high_income` indicator.
12. Creating `age_group`, `hours_band`, and `net_capital`.
13. Exporting the cleaned dataset and analysis results.

## Final Dataset

The final cleaned dataset contains:

- 48,842 records
- 20 columns
- 0 remaining missing values
- 29 exact duplicate rows retained after auditing

The duplicate rows were retained because the dataset does not contain
a unique person identifier.

## Exploratory Data Analysis

The analysis includes:

- Overall income distribution
- Above-$50K income rate
- Education vs income
- Occupation vs income
- Age group vs income
- Workclass vs income
- Sex vs income
- Weekly working-hour distributions
- Numeric correlation analysis
- Capital gain distribution
- Capital loss distribution

## Key Results

There are 11,687 records above USD 50K and 37,155 records at or below
USD 50K.

The overall above-$50K rate is 23.93%.

The calculated above-$50K rates for the sex categories are:

- Male: 30.38%
- Female: 10.93%

The mean weekly working time is:

- <=50K group: 38.84 hours
- >50K group: 45.45 hours

The correlation of selected numeric variables with `high_income` is:

- `age`: 0.23
- `education_num`: 0.33
- `hours_per_week`: 0.23
- `capital_gain`: 0.22
- `capital_loss`: 0.15
- `net_capital`: 0.21

These values describe associations within the dataset and should not
be interpreted as causal relationships.

