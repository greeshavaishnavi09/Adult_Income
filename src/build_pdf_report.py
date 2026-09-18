# import libraries

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)

import pandas as pd


# define project paths

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data"
REPORTS_DIR = PROJECT_DIR / "reports"
CHARTS_DIR = REPORTS_DIR / "charts"
TABLES_DIR = REPORTS_DIR / "summary_tables"

PDF_FILE = REPORTS_DIR / "adult_income_eda_report.pdf"


# load cleaned dataset

df = pd.read_csv(
    DATA_DIR / "adult_income_cleaned.csv"
)


# create PDF document

document = SimpleDocTemplate(
    str(PDF_FILE),
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)


# create styles

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=22,
    leading=28,
    spaceAfter=15
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=12,
    leading=18,
    spaceAfter=20
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading1"],
    fontSize=16,
    leading=20,
    spaceBefore=15,
    spaceAfter=10
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=8
)


# create story

story = []


# add title

story.append(
    Paragraph(
        "Adult Income Data Cleaning and EDA",
        title_style
    )
)

story.append(
    Paragraph(
        "Exploratory Data Analysis Report",
        subtitle_style
    )
)

story.append(
    Paragraph(
        "UCI Adult Income Dataset",
        subtitle_style
    )
)

story.append(Spacer(1, 10))


# add project overview

story.append(
    Paragraph(
        "1. Project Overview",
        heading_style
    )
)

story.append(
    Paragraph(
        "This project uses the UCI Adult Income dataset to perform "
        "data collection, data cleaning, validation, feature engineering, "
        "and exploratory data analysis.",
        body_style
    )
)

story.append(
    Paragraph(
        f"The final analysis dataset contains {len(df):,} records "
        f"and {len(df.columns)} columns.",
        body_style
    )
)

story.append(
    Paragraph(
        "The main question is: Which demographic, education, and work "
        "characteristics are associated with an annual income above USD 50K?",
        body_style
    )
)


# add data cleaning section

story.append(
    Paragraph(
        "2. Data Cleaning",
        heading_style
    )
)

story.append(
    Paragraph(
        "The official adult.data and adult.test files were combined "
        "into a single analysis dataset while preserving the source "
        "split for traceability.",
        body_style
    )
)

story.append(
    Paragraph(
        "Whitespace was removed from categorical values and the UCI "
        "missing-value marker '?' was converted to missing values.",
        body_style
    )
)

story.append(
    Paragraph(
        "Missing workclass, occupation, and native_country values "
        "were replaced with 'Unknown' so that the affected records "
        "could be retained.",
        body_style
    )
)

story.append(
    Paragraph(
        f"The final cleaned dataset contains "
        f"{df.isnull().sum().sum()} remaining missing values.",
        body_style
    )
)

story.append(
    Paragraph(
        f"{df.duplicated().sum()} exact duplicate rows were identified "
        "and retained because the dataset does not contain a unique "
        "person identifier.",
        body_style
    )
)


# add income distribution

story.append(
    Paragraph(
        "3. Overall Income Distribution",
        heading_style
    )
)

high_income_count = int(df["high_income"].sum())
low_income_count = int((df["high_income"] == 0).sum())
high_income_rate = df["high_income"].mean() * 100

story.append(
    Paragraph(
        f"The dataset contains {len(df):,} records. "
        f"{high_income_count:,} records have income above USD 50K, "
        f"while {low_income_count:,} records have income at or below "
        f"USD 50K.",
        body_style
    )
)

story.append(
    Paragraph(
        f"The above-USD-50K rate is {high_income_rate:.2f}%.",
        body_style
    )
)


# add income chart

income_chart = CHARTS_DIR / "income_distribution.png"

if income_chart.exists():

    story.append(
        Image(
            str(income_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )

    story.append(Spacer(1, 10))


# add education section

story.append(
    Paragraph(
        "4. Education and Income",
        heading_style
    )
)

story.append(
    Paragraph(
        "The above-USD-50K rate varies across education categories. "
        "The education summary table was calculated using the proportion "
        "of records with the high_income indicator equal to 1.",
        body_style
    )
)

education_chart = CHARTS_DIR / "education_high_income_rate.png"

if education_chart.exists():

    story.append(
        Image(
            str(education_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add occupation section

story.append(
    Paragraph(
        "5. Occupation and Income",
        heading_style
    )
)

story.append(
    Paragraph(
        "The above-USD-50K rate varies across occupation categories. "
        "The analysis considers both the number of records and the "
        "proportion above USD 50K.",
        body_style
    )
)

occupation_chart = CHARTS_DIR / "occupation_high_income_rate.png"

if occupation_chart.exists():

    story.append(
        Image(
            str(occupation_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add age section

story.append(
    Paragraph(
        "6. Age Group and Income",
        heading_style
    )
)

story.append(
    Paragraph(
        "The above-USD-50K rate varies across the defined age groups. "
        "These differences describe patterns observed within the dataset.",
        body_style
    )
)

age_chart = CHARTS_DIR / "age_group_high_income_rate.png"

if age_chart.exists():

    story.append(
        Image(
            str(age_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add workclass section

story.append(
    Paragraph(
        "7. Workclass and Income",
        heading_style
    )
)

story.append(
    Paragraph(
        "The above-USD-50K rate differs across workclass categories, "
        "including private, government, self-employment, and other "
        "workclass categories.",
        body_style
    )
)

workclass_chart = CHARTS_DIR / "workclass_high_income_rate.png"

if workclass_chart.exists():

    story.append(
        Image(
            str(workclass_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add sex section

story.append(
    Paragraph(
        "8. Sex and Income",
        heading_style
    )
)

story.append(
    Paragraph(
        "The calculated above-USD-50K rate is 30.38% for male records "
        "and 10.93% for female records in this dataset.",
        body_style
    )
)

sex_chart = CHARTS_DIR / "sex_high_income_rate.png"

if sex_chart.exists():

    story.append(
        Image(
            str(sex_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add weekly hours section

story.append(
    Paragraph(
        "9. Weekly Working Hours",
        heading_style
    )
)

hours_below = df.loc[
    df["income"] == "<=50K",
    "hours_per_week"
]

hours_above = df.loc[
    df["income"] == ">50K",
    "hours_per_week"
]

story.append(
    Paragraph(
        f"The mean weekly working time is "
        f"{hours_below.mean():.2f} hours for the <=50K group "
        f"and {hours_above.mean():.2f} hours for the >50K group.",
        body_style
    )
)

story.append(
    Paragraph(
        f"The median is {hours_below.median():.0f} hours for the "
        f"<=50K group and {hours_above.median():.0f} hours for "
        f"the >50K group.",
        body_style
    )
)

hours_chart = CHARTS_DIR / "weekly_hours_by_income.png"

if hours_chart.exists():

    story.append(
        Image(
            str(hours_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )

hours_distribution_chart = CHARTS_DIR / "weekly_hours_distribution.png"

if hours_distribution_chart.exists():

    story.append(
        Image(
            str(hours_distribution_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add numeric relationships

story.append(
    Paragraph(
        "10. Numeric Relationships",
        heading_style
    )
)

story.append(
    Paragraph(
        "Correlation analysis was performed for age, education_num, "
        "hours_per_week, capital_gain, capital_loss, net_capital, "
        "and high_income.",
        body_style
    )
)

story.append(
    Paragraph(
        "The correlations with high_income were approximately "
        "0.23 for age, 0.33 for education_num, 0.23 for "
        "hours_per_week, 0.22 for capital_gain, 0.15 for "
        "capital_loss, and 0.21 for net_capital.",
        body_style
    )
)

correlation_chart = CHARTS_DIR / "numeric_correlation_heatmap.png"

if correlation_chart.exists():

    story.append(
        Image(
            str(correlation_chart),
            width=6.5 * inch,
            height=5.2 * inch
        )
    )


# add capital gain and loss

story.append(
    Paragraph(
        "11. Capital Gain and Capital Loss",
        heading_style
    )
)

story.append(
    Paragraph(
        "Capital gain and capital loss distributions are strongly "
        "concentrated around zero, with a smaller number of records "
        "having substantially larger values.",
        body_style
    )
)

capital_gain_chart = CHARTS_DIR / "capital_gain_distribution.png"

if capital_gain_chart.exists():

    story.append(
        Image(
            str(capital_gain_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )

capital_loss_chart = CHARTS_DIR / "capital_loss_distribution.png"

if capital_loss_chart.exists():

    story.append(
        Image(
            str(capital_loss_chart),
            width=6.5 * inch,
            height=4.2 * inch
        )
    )


# add limitations

story.append(
    PageBreak()
)

story.append(
    Paragraph(
        "12. Limitations",
        heading_style
    )
)

limitations = [
    "The dataset contains historical census information and may not represent current income patterns.",
    "The analysis is descriptive and identifies associations rather than causal relationships.",
    "The dataset contains demographic variables that require careful interpretation.",
    "Missing categorical values were represented as Unknown rather than deleting affected records.",
    "Exact duplicate rows were retained because there is no unique person identifier.",
    "The fnlwgt census weight was not applied to the visual summaries.",
    "Correlation measures linear association and does not establish causation.",
    "The income target uses the dataset's <=50K and >50K categories.",
    "This project does not perform predictive modeling or evaluate predictive performance."
]

for limitation in limitations:

    story.append(
        Paragraph(
            f"• {limitation}",
            body_style
        )
    )


# add conclusion

story.append(
    Paragraph(
        "13. Conclusion",
        heading_style
    )
)

story.append(
    Paragraph(
        "This project completed an end-to-end data cleaning and "
        "exploratory analysis workflow using the UCI Adult Income dataset.",
        body_style
    )
)

story.append(
    Paragraph(
        "The analysis examined income distribution and compared "
        "the above-USD-50K rate across education, occupation, age "
        "group, workclass, and sex. Weekly working-hour distributions "
        "and numeric relationships were also examined.",
        body_style
    )
)

story.append(
    Paragraph(
        "The findings describe patterns and associations within "
        "this historical dataset. They should not be interpreted "
        "as evidence of causal relationships or as representative "
        "estimates of the current population.",
        body_style
    )
)

# add final PDF

document.build(story)

print("PDF report created successfully.")
print("File:", PDF_FILE)
