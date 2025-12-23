# Python Basics
## 1.1 Variables

A variable is a container used to store data values in memory.

**Example:**

x = 10
name = "Zafar"
cgpa = 3.4

## 1.2 Data Types

Data types define the type of value stored in a variable.

**Common Data Types in Python**

Integer (int): Whole numbers

Float (float): Decimal numbers

String (str): Text

Boolean (bool): True or False

**Example:**

a = 5        # int

b = 2.5      # float

c = "AI"     # string

d = True     # boolean

## 1.3 If–Else Statement

The if–else statement is used for decision making based on conditions.

**Syntax:**
if condition:
    statement
else:
    statement


**Example:**

marks = 65

if marks >= 50:

    print("Pass")
    
else:

    print("Fail")

## 1.4 Loops

Loops are used to repeat a block of code.

### 1.4.1 For Loop

Used when the number of iterations is known.

for i in range(1, 6):

    print(i)

### 1.4.2 While Loop

Used when the condition is checked before each iteration.

i = 1

while i <= 5:

    print(i)
    
    i += 1

# 2. Machine Learning
## 2.1 What is Machine Learning (ML)?

Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data and improve automatically without explicit programming.

**Examples:**

YouTube recommendations

Email spam filtering

Face recognition

# 2.2 Supervised Learning

Supervised learning uses labeled data, where both input and output are known.

**Example Dataset:**

| Engine Size (L) | Weight (kg) | MPG (Miles per Gallon) |
| --------------- | ----------- | ---------------------- |
| 1.2             | 950         | 35                     |
| 1.8             | 1200        | 28                     |
| 2.5             | 1500        | 22                     |
| 3.0             | 1800        | 18                     |

## Types of Supervised Learning

**Classification**

– Output is a category (Pass/Fail)

**Regression**

– Output is a numeric value

# 2.3 Regression

Regression is a supervised learning technique used to predict continuous values.

**Common Uses:**

Predict marks

Predict salary

Predict house prices

**Simple Example:**

hours = [1, 3, 5]

marks = [30, 60, 85]

# 3. Machine Learning Process
## 3.1 ML Workflow
Data Collection → Training → Model → Prediction

## 3.2 Real-Life Example

YouTube Recommendation System

Input: Watch history

Model: Learns user behavior

Output: Suggested videos
