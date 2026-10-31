# ============================================================
# PROGRAMMING WITH PYTHON LAB - BCACC393
# LAB 8
# Programs 1 to 25
# ============================================================


# ============================================================
# PART A - ARRAYS IN PYTHON
# ============================================================


#1
from array import array

arr = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("\n#1")
print("Array:", arr)
print("All elements:")

for x in arr:
    print(x, end=" ")

print("\nFirst element:", arr[0])
print("Last element:", arr[-1])
print("Middle element:", arr[len(arr)//2])


#2
print("\n#2")

arr = array('i', [10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", sum(arr))
print("Average:", sum(arr) / len(arr))
print("Maximum:", max(arr))
print("Minimum:", min(arr))
print("Length:", len(arr))


#3
print("\n#3")

arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Original array:", arr)

arr.insert(3, 99)
print("After inserting 99 at position 3:", arr)

arr.append(100)
print("After appending 100:", arr)

arr.remove(5)
print("After removing 5:", arr)


#4
print("\n#4")

arr = array('i', [45, 12, 78, 23, 9, 56, 34])

print("Original array:", arr)

sorted_arr = sorted(arr)

print("Ascending order:", sorted_arr)
print("Descending order:", sorted_arr[::-1])
print("Reversed array:", list(arr)[::-1])


#5
print("\n#5")

arr = array('i', [10, 20, 30, 20, 40, 20, 50])

search = 20

print("Array:", arr)

if search in arr:
    print(search, "found at index:", arr.index(search))
    print("Number of occurrences:", arr.count(search))
else:
    print(search, "not found")


# ============================================================
# PART B - NUMPY
# ============================================================


#6
print("\n#6")

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros(5)
arr4 = np.ones(5)
arr5 = np.arange(1, 11)

print("1D Array:", arr1)
print("Shape:", arr1.shape)

print("\n2D Array:")
print(arr2)
print("Shape:", arr2.shape)

print("\nZeros Array:", arr3)
print("Shape:", arr3.shape)

print("\nOnes Array:", arr4)
print("Shape:", arr4.shape)

print("\nRange Array:", arr5)
print("Shape:", arr5.shape)


#7
print("\n#7")

arr = np.arange(1, 21)

print("Array:", arr)

print("Positive indexing:")
print("First element:", arr[0])
print("Fifth element:", arr[4])

print("Negative indexing:")
print("Last element:", arr[-1])
print("Second last element:", arr[-2])

print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])


#8
print("\n#8")

A = np.array([10, 20, 30, 40, 50])
B = np.array([2, 4, 5, 8, 10])

print("A:", A)
print("B:", B)

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)
print("Modulus:", A % B)
print("Exponentiation:", A ** B)


#9
print("\n#9")

marks = np.array([85, 72, 90, 65, 78, 88, 92, 70, 81, 95])

print("Marks:", marks)

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))


#10
print("\n#10")

arr = np.arange(1, 25)

print("Original array:")
print(arr)

a = arr.reshape(2, 12)
b = arr.reshape(3, 8)
c = arr.reshape(4, 6)
d = arr.reshape(6, 4)

print("\n2 x 12:")
print(a)
print("Shape:", a.shape)

print("\n3 x 8:")
print(b)
print("Shape:", b.shape)

print("\n4 x 6:")
print(c)
print("Shape:", c.shape)

print("\n6 x 4:")
print(d)
print("Shape:", d.shape)


#11
print("\n#11")

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition:")
print(A + B)

print("\nMatrix Subtraction:")
print(A - B)

print("\nElement-wise Multiplication:")
print(A * B)

print("\nMatrix Multiplication:")
print(A @ B)

print("\nTranspose of A:")
print(A.T)

print("\nTranspose of B:")
print(B.T)


#12
print("\n#12")

arr = np.array([
    10, 15, 22, 30, 35,
    42, 50, 55, 60, 65,
    70, 75, 80, 85, 90,
    12, 25, 48, 52, 100
])

print("Array:", arr)

print("Even numbers:", arr[arr % 2 == 0])
print("Odd numbers:", arr[arr % 2 != 0])
print("Numbers greater than 50:", arr[arr > 50])
print("Numbers between 20 and 60:", arr[(arr >= 20) & (arr <= 60)])

condition = arr > 50
print("Boolean indexing:", condition)
print("Elements using Boolean indexing:", arr[condition])


#13
print("\n#13")

angles = np.array([0, 30, 45, 60, 90])

radians = np.deg2rad(angles)

print("Angles:", angles)

print("Sine:", np.sin(radians))
print("Cosine:", np.cos(radians))
print("Tangent:", np.tan(radians))

numbers = np.array([1, 10, 100, 1000])

print("\nNumbers:", numbers)
print("Square Root:", np.sqrt(numbers))
print("Logarithm:", np.log(numbers))
print("Exponential:", np.exp(numbers))


#14
print("\n#14")

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("A:", A)
print("B:", B)

print("\nConcatenation:")
print(np.concatenate((A, B)))

print("\nVertical Stack:")
print(np.vstack((A, B)))

print("\nHorizontal Stack:")
print(np.hstack((A, B)))

C = np.array([1, 2, 3, 4, 5, 6])

print("\nOriginal array:", C)

print("Split into two parts:")
print(np.split(C, 2))


#15
print("\n#15")

arr = np.array([
    10, 20, np.nan, 30,
    40, np.nan, 50, 60
])

print("Original array:")
print(arr)

print("Missing values:", np.isnan(arr))
print("Number of missing values:", np.isnan(arr).sum())

mean_value = np.nanmean(arr)

print("Mean ignoring NaN:", mean_value)

arr[np.isnan(arr)] = mean_value

print("Array after replacing NaN:")
print(arr)


# ============================================================
# PART C - PANDAS
# ============================================================


#16
print("\n#16")

import pandas as pd

marks = [75, 82, 68, 90, 85, 72, 95, 60, 88, 78]

series = pd.Series(marks)

print("Series:")
print(series)

print("\nIndex:")
print(series.index)

print("\nValues:")
print(series.values)

print("\nFirst five values:")
print(series.head())

print("\nLast three values:")
print(series.tail(3))

print("\nMaximum:", series.max())
print("Minimum:", series.min())


#17
print("\n#17")

data = {
    "Roll No": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Rahul", "Ananya", "Amit", "Priya", "Rohan",
        "Sneha", "Arjun", "Neha", "Karan", "Riya"
    ],
    "Department": [
        "BCA", "BCA", "BCA", "MCA", "BCA",
        "MCA", "BCA", "BCA", "MCA", "BCA"
    ],
    "Marks": [85, 92, 78, 88, 75, 90, 95, 70, 82, 86],
    "Attendance": [90, 85, 78, 92, 80, 88, 95, 75, 82, 89]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nFirst five rows:")
print(df.head())

print("\nLast five rows:")
print(df.tail())

print("\nSelected columns:")
print(df[["Name", "Marks"]])

print("\nDetails of student with Roll No 105:")
print(df[df["Roll No"] == 105])


#18
print("\n#18")

data = {
    "Roll No": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Rahul", "Ananya", "Amit", "Priya", "Rohan",
        "Sneha", "Arjun", "Neha", "Karan", "Riya"
    ],
    "Department": [
        "BCA", "BCA", "BCA", "MCA", "BCA",
        "MCA", "BCA", "BCA", "MCA", "BCA"
    ],
    "Marks": [85, 92, 78, 88, 75, 90, 95, 70, 82, 86],
    "Attendance": [90, 85, 78, 92, 80, 88, 95, 75, 82, 89]
}

df = pd.DataFrame(data)

print("Students with marks greater than 75:")
print(df[df["Marks"] > 75])

print("\nStudents with attendance greater than 80:")
print(df[df["Attendance"] > 80])

print("\nMarks > 60 and Attendance > 75:")
print(df[(df["Marks"] > 60) & (df["Attendance"] > 75)])

print("\nStudents from BCA department:")
print(df[df["Department"] == "BCA"])


#19
print("\n#19")

data = {
    "Employee ID": [101, 102, 103, 104, 105, 106],
    "Name": [
        "Rahul", "Ananya", "Amit",
        "Priya", "Rohan", "Sneha"
    ],
    "Department": [
        "IT", "HR", "IT",
        "Finance", "HR", "IT"
    ],
    "Salary": [45000, 55000, 65000, 50000, 75000, 60000]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

print("\nSalary in Ascending Order:")
print(df.sort_values("Salary"))

print("\nSalary in Descending Order:")
print(df.sort_values("Salary", ascending=False))

print("\nHighest Paid Employee:")
print(df.loc[df["Salary"].idxmax()])

print("\nLowest Paid Employee:")
print(df.loc[df["Salary"].idxmin()])

df["Rank"] = df["Salary"].rank(
    ascending=False,
    method="min"
)

print("\nEmployees with Salary Rank:")
print(df.sort_values("Rank"))


#20
print("\n#20")

data = {
    "Name": ["Rahul", "Ananya", "Amit", "Priya", "Rohan", "Sneha"],
    "Marks": [85, np.nan, 78, 90, np.nan, 88],
    "Attendance": [90, 85, np.nan, 92, 80, np.nan],
    "Department": ["BCA", "BCA", np.nan, "MCA", "BCA", "MCA"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing values:")
print(df.isnull())

print("\nCount of missing values:")
print(df.isnull().sum())

print("\nRows after removing missing values:")
print(df.dropna())

marks_mean = df["Marks"].mean()
attendance_mean = df["Attendance"].mean()

df["Marks"] = df["Marks"].fillna(marks_mean)
df["Attendance"] = df["Attendance"].fillna(attendance_mean)

print("\nAfter replacing missing numerical values with mean:")
print(df)


#21
print("\n#21")

data = {
    "Department": [
        "IT", "IT", "HR",
        "HR", "Finance", "Finance",
        "IT", "HR"
    ],
    "Name": [
        "Rahul", "Amit", "Ananya",
        "Priya", "Rohan", "Sneha",
        "Arjun", "Neha"
    ],
    "Salary": [
        50000, 65000, 55000,
        60000, 70000, 75000,
        60000, 58000
    ],
    "Experience": [
        2, 5, 3, 4, 6, 7, 4, 3
    ]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

group = df.groupby("Department")

print("\nAverage Salary:")
print(group["Salary"].mean())

print("\nMaximum Salary:")
print(group["Salary"].max())

print("\nMinimum Salary:")
print(group["Salary"].min())

print("\nNumber of Employees:")
print(group["Name"].count())


# ============================================================
# PART D - MATPLOTLIB
# ============================================================


#22
print("\n#22")

import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

sales = [
    120, 150, 170, 160,
    190, 210, 230, 220,
    250, 270, 290, 310
]

plt.plot(
    months,
    sales,
    marker="o",
    label="Monthly Sales"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.legend()
plt.grid(True)
plt.show()


#23
print("\n#23")

students = [
    "Rahul", "Ananya", "Amit",
    "Priya", "Rohan"
]

marks = [85, 92, 78, 88, 75]

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Five Students")

for i in range(len(marks)):
    plt.text(i, marks[i] + 1, str(marks[i]), ha="center")

plt.show()


#24
print("\n#24")

months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

temperature = [
    18, 20, 24, 28,
    32, 34, 33, 31,
    29, 26, 22, 19
]

plt.figure(figsize=(10, 10))

# Line Plot
plt.subplot(3, 1, 1)
plt.plot(months, temperature, marker="o")
plt.title("Monthly Temperature - Line Plot")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Bar Chart
plt.subplot(3, 1, 2)
plt.bar(months, temperature)
plt.title("Monthly Temperature - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

# Scatter Plot
plt.subplot(3, 1, 3)
plt.scatter(months, temperature)
plt.title("Temperature Distribution - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.tight_layout()
plt.show()


#25
print("\n#25")

data = {
    "Student Name": [
        "Rahul", "Ananya", "Amit", "Priya", "Rohan",
        "Sneha", "Arjun", "Neha", "Karan", "Riya"
    ],

    "Mathematics": [
        85, 92, 78, 88, 75,
        90, 95, 70, 82, 86
    ],

    "Physics": [
        80, 85, 72, 90, 78,
        88, 91, 68, 79, 84
    ],

    "Chemistry": [
        82, 89, 75, 85, 80,
        92, 94, 72, 81, 87
    ],

    "Computer Science": [
        90, 95, 88, 92, 85,
        94, 98, 80, 89, 93
    ]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer Science"
]

# Calculate average marks using Pandas
subject_average = df[subjects].mean()

print("\nAverage Marks of Each Subject:")
print(subject_average)

# Calculate total marks
df["Total Marks"] = df[subjects].sum(axis=1)

# Calculate average marks using NumPy
df["Average Marks"] = np.mean(
    df[subjects].values,
    axis=1
)

print("\nStudent Total and Average Marks:")
print(df)

# ------------------------------------------------------------
# Bar Chart - Average Marks of Subjects
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    subjects,
    subject_average
)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Average Marks of Each Subject")

plt.grid(axis="y")
plt.show()


# ------------------------------------------------------------
# Line Plot - Marks of Individual Students
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

for subject in subjects:
    plt.plot(
        df["Student Name"],
        df[subject],
        marker="o",
        label=subject
    )

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Individual Students")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Histogram - Average Marks
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Average Marks"],
    bins=5,
    edgecolor="black"
)

plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Average Marks")
plt.grid(axis="y")

plt.show()


# ============================================================
# END OF LAB 8
# ============================================================
