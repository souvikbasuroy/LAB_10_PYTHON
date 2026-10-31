# ============================================================
# PROGRAMMING WITH PYTHON LAB - BCACC393
# LAB 9
# UCI AUTOMOBILE DATASET
# Programs 1 to 23
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# COMMON DATASET LOADING
# ============================================================

columns = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price"
]

# Load dataset
# "?" in the dataset is treated as NaN
df = pd.read_csv(
    "imports-85.data",
    names=columns,
    na_values="?"
)


# ============================================================
# CONVERT IMPORTANT NUMERICAL COLUMNS
# ============================================================

numeric_columns = [
    "normalized-losses",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-size",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# ============================================================
# PROGRAM 1
# LOADING AND EXPLORING THE DATASET
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 1: LOADING AND EXPLORING THE DATASET")
print("=" * 60)

# First five records
print("\nFirst five records:")
print(df.head())

# Last five records
print("\nLast five records:")
print(df.tail())

# Number of rows and columns
print("\nNumber of rows and columns:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns)

# Data types
print("\nData types of all columns:")
print(df.dtypes)


# ============================================================
# PROGRAM 2
# DATASET INFORMATION AND SUMMARY STATISTICS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 2: DATASET INFORMATION AND SUMMARY STATISTICS")
print("=" * 60)

print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())


# ============================================================
# PROGRAM 3
# HANDLING MISSING VALUES
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 3: HANDLING MISSING VALUES")
print("=" * 60)

# Count missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# Display columns containing missing values
print("\nColumns containing missing values:")
print(df.columns[df.isnull().any()])

# Total number of missing values
print("\nTotal number of missing values:")
print(df.isnull().sum().sum())


# ============================================================
# PROGRAM 4
# CLEANING THE PRICE COLUMN
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 4: CLEANING THE PRICE COLUMN")
print("=" * 60)

# Remove missing price values
price = df["price"].dropna()

print("\nMinimum car price:", price.min())
print("Maximum car price:", price.max())
print("Average car price:", price.mean())
print("Median car price:", price.median())


# ============================================================
# PROGRAM 5
# FREQUENCY OF CAR MAKES
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 5: FREQUENCY OF CAR MAKES")
print("=" * 60)

# Count cars for each manufacturer
make_count = df["make"].value_counts()

print("\nNumber of cars belonging to each make:")
print(make_count)

print("\nTop 10 car manufacturers:")
print(make_count.head(10))


# ============================================================
# PROGRAM 6
# BODY STYLE ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 6: BODY STYLE ANALYSIS")
print("=" * 60)

body_style_count = df["body-style"].value_counts()

print("\nFrequency of body styles:")
print(body_style_count)


# ============================================================
# PROGRAM 7
# FUEL TYPE ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 7: FUEL TYPE ANALYSIS")
print("=" * 60)

# Number of cars for each fuel type
fuel_count = df["fuel-type"].value_counts()

# Percentage of cars
fuel_percentage = df["fuel-type"].value_counts(
    normalize=True
) * 100

print("\nNumber of cars using each fuel type:")
print(fuel_count)

print("\nPercentage of cars using each fuel type:")
print(fuel_percentage)

# Bar chart
plt.figure(figsize=(7, 5))

fuel_count.plot(kind="bar")

plt.title("Number of Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 8
# CAR PRICE DISTRIBUTION
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 8: CAR PRICE DISTRIBUTION")
print("=" * 60)

price = df["price"].dropna()

print("\nMinimum price:", price.min())
print("Maximum price:", price.max())
print("Mean price:", price.mean())
print("Median price:", price.median())
print("Standard deviation:", price.std())

# Histogram
plt.figure(figsize=(8, 5))

plt.hist(price, bins=15)

plt.title("Distribution of Car Prices")
plt.xlabel("Car Price")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 9
# AVERAGE PRICE BY CAR MAKE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 9: AVERAGE PRICE BY CAR MAKE")
print("=" * 60)

average_price_make = df.groupby("make")["price"].mean()

average_price_make = average_price_make.sort_values(
    ascending=False
)

print("\nAverage price by car make:")
print(average_price_make)

print("\nFive most expensive manufacturers:")
print(average_price_make.head(5))


# ============================================================
# PROGRAM 10
# AVERAGE PRICE BY BODY STYLE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 10: AVERAGE PRICE BY BODY STYLE")
print("=" * 60)

average_price_body = df.groupby(
    "body-style"
)["price"].mean()

print("\nAverage price by body style:")
print(average_price_body)

# Bar chart
plt.figure(figsize=(8, 5))

average_price_body.plot(kind="bar")

plt.title("Average Car Price by Body Style")
plt.xlabel("Body Style")
plt.ylabel("Average Price")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 11
# HORSEPOWER ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 11: HORSEPOWER ANALYSIS")
print("=" * 60)

horsepower = df["horsepower"].dropna()

print("\nMinimum horsepower:", horsepower.min())
print("Maximum horsepower:", horsepower.max())
print("Mean horsepower:", horsepower.mean())
print("Median horsepower:", horsepower.median())
print("Standard deviation:", horsepower.std())

# Histogram
plt.figure(figsize=(8, 5))

plt.hist(horsepower, bins=15)

plt.title("Distribution of Horsepower")
plt.xlabel("Horsepower")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 12
# ENGINE SIZE ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 12: ENGINE SIZE ANALYSIS")
print("=" * 60)

engine_size = df["engine-size"].dropna()

print("\nMinimum engine size:", engine_size.min())
print("Maximum engine size:", engine_size.max())
print("Average engine size:", engine_size.mean())
print("Median engine size:", engine_size.median())

# Histogram
plt.figure(figsize=(8, 5))

plt.hist(engine_size, bins=15)

plt.title("Distribution of Engine Size")
plt.xlabel("Engine Size")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 13
# HORSEPOWER VS PRICE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 13: HORSEPOWER VS PRICE")
print("=" * 60)

data = df[["horsepower", "price"]].dropna()

# Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["horsepower"],
    data["price"]
)

plt.title("Horsepower vs Car Price")
plt.xlabel("Horsepower")
plt.ylabel("Car Price")
plt.grid(True)

plt.show()

print("\nObservation:")
print("There appears to be a positive relationship between")
print("horsepower and car price. Cars with higher horsepower")
print("generally tend to have higher prices.")


# ============================================================
# PROGRAM 14
# ENGINE SIZE VS PRICE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 14: ENGINE SIZE VS PRICE")
print("=" * 60)

data = df[["engine-size", "price"]].dropna()

# Correlation coefficient
correlation = data["engine-size"].corr(
    data["price"]
)

print("\nCorrelation coefficient:", correlation)

# Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["engine-size"],
    data["price"]
)

plt.title("Engine Size vs Car Price")
plt.xlabel("Engine Size")
plt.ylabel("Car Price")
plt.grid(True)

plt.show()


# ============================================================
# PROGRAM 15
# CURB WEIGHT VS PRICE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 15: CURB WEIGHT VS PRICE")
print("=" * 60)

data = df[["curb-weight", "price"]].dropna()

# Correlation coefficient
correlation = data["curb-weight"].corr(
    data["price"]
)

print("\nCorrelation coefficient:", correlation)

# Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["curb-weight"],
    data["price"]
)

plt.title("Curb Weight vs Car Price")
plt.xlabel("Curb Weight")
plt.ylabel("Car Price")
plt.grid(True)

plt.show()


# ============================================================
# PROGRAM 16
# HIGHWAY MPG ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 16: HIGHWAY MPG ANALYSIS")
print("=" * 60)

highway_mpg = df["highway-mpg"].dropna()

print("\nMinimum highway MPG:", highway_mpg.min())
print("Maximum highway MPG:", highway_mpg.max())
print("Mean highway MPG:", highway_mpg.mean())
print("Median highway MPG:", highway_mpg.median())

# Histogram
plt.figure(figsize=(8, 5))

plt.hist(highway_mpg, bins=15)

plt.title("Distribution of Highway MPG")
plt.xlabel("Highway MPG")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 17
# CITY MPG VS HIGHWAY MPG
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 17: CITY MPG VS HIGHWAY MPG")
print("=" * 60)

data = df[["city-mpg", "highway-mpg"]].dropna()

# Correlation coefficient
correlation = data["city-mpg"].corr(
    data["highway-mpg"]
)

print("\nCorrelation coefficient:", correlation)

# Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["city-mpg"],
    data["highway-mpg"]
)

plt.title("City MPG vs Highway MPG")
plt.xlabel("City MPG")
plt.ylabel("Highway MPG")
plt.grid(True)

plt.show()

print("\nObservation:")
print("Cars with higher city mileage generally also have")
print("higher highway mileage.")


# ============================================================
# PROGRAM 18
# NUMBER OF DOORS BY BODY STYLE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 18: NUMBER OF DOORS BY BODY STYLE")
print("=" * 60)

# Frequency table
door_body_table = pd.crosstab(
    df["body-style"],
    df["num-of-doors"]
)

print("\nNumber of doors by body style:")
print(door_body_table)

# Bar chart
door_body_table.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Number of Doors by Body Style")
plt.xlabel("Body Style")
plt.ylabel("Number of Cars")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 19
# FUEL TYPE AND AVERAGE PRICE
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 19: FUEL TYPE AND AVERAGE PRICE")
print("=" * 60)

average_price_fuel = df.groupby(
    "fuel-type"
)["price"].mean()

print("\nAverage price of cars for each fuel type:")
print(average_price_fuel)

# Bar chart
plt.figure(figsize=(7, 5))

average_price_fuel.plot(kind="bar")

plt.title("Average Car Price by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average Price")
plt.grid(axis="y")

plt.show()

print("\nObservation:")
print("The bar chart compares the average prices of")
print("gasoline and diesel cars.")


# ============================================================
# PROGRAM 20
# DRIVE WHEEL ANALYSIS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 20: DRIVE WHEEL ANALYSIS")
print("=" * 60)

drive_count = df["drive-wheels"].value_counts()

print("\nNumber of cars by drive wheels:")
print(drive_count)

print("\nfwd = Front-wheel drive")
print("rwd = Rear-wheel drive")
print("4wd = Four-wheel drive")

# Bar chart
plt.figure(figsize=(7, 5))

drive_count.plot(kind="bar")

plt.title("Distribution of Drive Wheels")
plt.xlabel("Drive Wheels")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 21
# PRICE COMPARISON BY DRIVE WHEELS
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 21: PRICE COMPARISON BY DRIVE WHEELS")
print("=" * 60)

average_price_drive = df.groupby(
    "drive-wheels"
)["price"].mean()

print("\nAverage price by drive wheels:")
print(average_price_drive)

# Bar chart
plt.figure(figsize=(7, 5))

average_price_drive.plot(kind="bar")

plt.title("Average Car Price by Drive Wheels")
plt.xlabel("Drive Wheels")
plt.ylabel("Average Price")
plt.grid(axis="y")

plt.show()


# ============================================================
# PROGRAM 22
# CORRELATION ANALYSIS OF NUMERICAL VARIABLES
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 22: CORRELATION ANALYSIS")
print("=" * 60)

variables = [
    "price",
    "engine-size",
    "horsepower",
    "curb-weight",
    "city-mpg",
    "highway-mpg"
]

# Correlation matrix
correlation_matrix = df[variables].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Correlation with price
price_correlation = correlation_matrix["price"].drop("price")

print("\nCorrelation with price:")
print(price_correlation)

# Strongest positive correlation
positive_variable = price_correlation.idxmax()
positive_value = price_correlation.max()

# Strongest negative correlation
negative_variable = price_correlation.idxmin()
negative_value = price_correlation.min()

print("\nMost strongly positively correlated with price:")
print(positive_variable, "=", positive_value)

print("\nMost strongly negatively correlated with price:")
print(negative_variable, "=", negative_value)


# ============================================================
# PROGRAM 23
# BASIC CAR PRICE ANALYTICS REPORT
# ============================================================

print("\n")
print("=" * 60)
print("PROGRAM 23: BASIC CAR PRICE ANALYTICS REPORT")
print("=" * 60)


# ------------------------------------------------------------
# 1. DATASET DIMENSIONS AND BASIC INFORMATION
# ------------------------------------------------------------

print("\n1. DATASET DIMENSIONS")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nBasic Information:")
df.info()


# ------------------------------------------------------------
# 2. MISSING VALUE ANALYSIS
# ------------------------------------------------------------

print("\n2. MISSING VALUE ANALYSIS")

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())


# ------------------------------------------------------------
# 3. DESCRIPTIVE STATISTICS
# ------------------------------------------------------------

print("\n3. DESCRIPTIVE STATISTICS")

important_columns = [
    "price",
    "engine-size",
    "horsepower",
    "curb-weight",
    "city-mpg",
    "highway-mpg"
]

print(df[important_columns].describe())


# ------------------------------------------------------------
# 4. TOP FIVE MANUFACTURERS BY AVERAGE PRICE
# ------------------------------------------------------------

print("\n4. TOP FIVE MANUFACTURERS BY AVERAGE PRICE")

average_price_make = df.groupby(
    "make"
)["price"].mean()

average_price_make = average_price_make.sort_values(
    ascending=False
)

print(average_price_make.head(5))


# ------------------------------------------------------------
# 5. MOST COMMON BODY STYLE
# ------------------------------------------------------------

print("\n5. MOST COMMON BODY STYLE")

body_style_count = df["body-style"].value_counts()

print(body_style_count)

most_common_body_style = body_style_count.idxmax()

print("\nMost common body style:")
print(most_common_body_style)


# ------------------------------------------------------------
# 6. AVERAGE PRICE BY FUEL TYPE
# ------------------------------------------------------------

print("\n6. AVERAGE PRICE BY FUEL TYPE")

average_price_fuel = df.groupby(
    "fuel-type"
)["price"].mean()

print(average_price_fuel)


# ------------------------------------------------------------
# 7. AVERAGE PRICE BY DRIVE WHEELS
# ------------------------------------------------------------

print("\n7. AVERAGE PRICE BY DRIVE WHEELS")

average_price_drive = df.groupby(
    "drive-wheels"
)["price"].mean()

print(average_price_drive)


# ------------------------------------------------------------
# 8. HISTOGRAM OF CAR PRICES
# ------------------------------------------------------------

print("\n8. HISTOGRAM OF CAR PRICES")

plt.figure(figsize=(8, 5))

plt.hist(
    df["price"].dropna(),
    bins=15
)

plt.title("Distribution of Car Prices")
plt.xlabel("Car Price")
plt.ylabel("Number of Cars")
plt.grid(axis="y")

plt.show()


# ------------------------------------------------------------
# 9. SCATTER PLOT - HORSEPOWER VS PRICE
# ------------------------------------------------------------

print("\n9. HORSEPOWER VS PRICE")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["horsepower"],
    df["price"]
)

plt.title("Horsepower vs Car Price")
plt.xlabel("Horsepower")
plt.ylabel("Car Price")
plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 10. SCATTER PLOT - ENGINE SIZE VS PRICE
# ------------------------------------------------------------

print("\n10. ENGINE SIZE VS PRICE")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["engine-size"],
    df["price"]
)

plt.title("Engine Size vs Car Price")
plt.xlabel("Engine Size")
plt.ylabel("Car Price")
plt.grid(True)

plt.show()


# ============================================================
# FINAL CONCLUSION
# ============================================================

print("\n")
print("=" * 60)
print("FINAL CONCLUSION")
print("=" * 60)

print("""
The Automobile dataset contains information about 205 cars
and 26 different attributes.

The dataset contains missing values in several columns.
Therefore, missing values were identified and numerical
columns were converted into suitable numeric data types.

The analysis shows that car prices vary among different
manufacturers, body styles, fuel types and drive-wheel types.

Engine size, horsepower and curb weight generally show a
positive relationship with car price. On the other hand,
city MPG and highway MPG generally show a negative relationship
with car price.

The histogram helps to understand the distribution of car
prices, while the scatter plots help to understand the
relationships between price and important car features.
""")

print("\n")
print("=" * 60)
print("END OF LAB 9")
print("=" * 60)
