# 1. Introduction to Programming
## 1.1 Basic Understanding of Programming Concepts

Programming is the process of writing instructions that a computer can execute to perform tasks. It allows humans to communicate with computers and solve problems effectively.

## Key Concepts:

## Variables:

Variables are like storage boxes in memory where data can be stored and accessed later.

Example: age = 20 stores the number 20 in the variable age.

## Data Types:

Every variable has a type that defines what kind of data it holds.

### Common types:

int → whole numbers (10, -5)

float → decimal numbers (3.14, 0.5)

str → text ("Hello")

bool → True/False

### Loops:

Loops allow us to repeat a block of code multiple times without writing it again.

### Types: for loop (iterate over sequences), while loop (repeat while a condition is true).

### Conditionals:

Conditional statements let the program make decisions.

Types: if, elif, else.

# 2. Command Line Basics

## 2.1 Basic Command Line Navigation and Execution of Python Scripts

The command line (terminal or CMD) is a text-based interface to communicate with your computer.

### Basic Commands:

cd <folder> → change current directory

dir (Windows) → list files and folders

pwd → print the current directory path

## 2.2 Essential Python Topics

Variables and Data Types

Conditional Statements (if, else, elif)

Loops (for, while)

Lists, Tuples, Dictionaries, Sets

# 3. Getting Started
## 3.1 Introduction to Python

Python is a high-level, interpreted, and versatile programming language.

### Features of Python:

Simple and readable syntax

Supports multiple programming styles: procedural, object-oriented, and functional

Large library support for tasks like data analysis, web development, AI, and automation

Widely used in industry and academia

# 3.2 Installing Python

## Steps to install Python:

Visit Python official website

Download the latest version compatible with your system (Windows, Mac, Linux)

Run the installer and check “Add Python to PATH”

Verify installation in terminal/CMD

<img width="1331" height="261" alt="Screenshot 2025-10-13 181053" src="https://github.com/user-attachments/assets/e3df0be7-9648-44b5-9500-7212ce34112b" />

# 4. Python Basics
## 4.1 Variables and Data Types

Variables are used to store information that can be used later in the program.

<img width="1700" height="341" alt="image" src="https://github.com/user-attachments/assets/6a675d59-1a83-484d-a119-5ac3f5068e0a" />

<img width="1539" height="694" alt="image" src="https://github.com/user-attachments/assets/69f0bfde-e2aa-44eb-8ba0-3449f0eb1bce" />

## 4.2 control flow statements:

### if statement
Checks the first condition (marks >= 90).
If true, executes the block and skips the rest.

### elif statements
Checked only if the previous if or elif was false.
Allows multiple conditions to be tested sequentially.

### else statement
Executes when none of the above conditions are true.
Acts as a fallback.

<img width="1679" height="486" alt="Screenshot 2025-10-13 183707" src="https://github.com/user-attachments/assets/f485235e-75c4-4706-9e06-44b5dffa038e" />

# 5.loop statements:

## For Loop

The for loop is used to iterate over a sequence (like a list, tuple, or range) and execute a block of code multiple times.

<img width="1560" height="249" alt="Screenshot 2025-10-13 184259" src="https://github.com/user-attachments/assets/6aaecbc4-f5c5-49dc-a565-98cf1afd95ac" />

## while loop:

The while loop repeats a block of code as long as a condition is True.
<img width="1429" height="216" alt="image" src="https://github.com/user-attachments/assets/e97bbd0c-8c87-4714-b34a-15ed6a1d9db3" />

The loop continues until the user enters 5.
Useful for programs requiring repeated user input until a condition is met

<img width="1501" height="294" alt="image" src="https://github.com/user-attachments/assets/b86a9245-a270-4fe8-aa7f-66f6ba7701fd" />

# functions and datastructures
## functions:

A function is a block of reusable code that performs a specific task.
It helps make your code more organized, readable, and reusable.

<img width="1335" height="233" alt="image" src="https://github.com/user-attachments/assets/b0c92b2d-5b53-4d7d-a98e-52897158c504" />

# modules and pakages:

A module is a Python file (.py) that contains functions, variables, or classes you can reuse in other programs.

<img width="1366" height="677" alt="image" src="https://github.com/user-attachments/assets/b2347a82-52c3-41dc-a52d-d9576fab022a" />


## list 

A list in Python is a collection of ordered, mutable (changeable), and indexed items.
Lists are used to store multiple values in a single variable.

Ordered – Elements maintain the order in which they are added.
Mutable – You can modify elements after creation.
Allow duplicates – Same value can appear more than once.
Heterogeneous – Can store different data types together.
<img width="1847" height="782" alt="Screenshot 2025-10-14 174633 - Copy" src="https://github.com/user-attachments/assets/17ac0a69-29d2-4fcc-8e82-c3747439cc9a" />
<img width="1847" height="782" alt="Screenshot 2025-10-14 174633" src="https://github.com/user-attachments/assets/987eaf56-695a-4023-b3b9-188e5260b0ef" />

<img width="1898" height="901" alt="Screenshot 2025-10-14 174652" src="https://github.com/user-attachments/assets/7b6c8b41-f5a6-42a0-bb95-9f85a87701a5" />


## tuple

A tuple in Python is a collection of ordered and immutable elements.
It is similar to a list, but once created, the elements cannot be changed (no modification, addition, or deletion).

Ordered – Elements maintain the same sequence.
Immutable – You cannot modify elements once the tuple is created.
Allow duplicates – Same value can appear more than once.
Heterogeneous – Can store different data types.

<img width="1052" height="738" alt="Screenshot 2025-10-14 180618" src="https://github.com/user-attachments/assets/075b5c46-a0d1-4cc5-9cb3-dc14ab139405" />


## dictionaries

A dictionary in Python is a collection of key–value pairs.
It is unordered (in older versions), mutable, and indexed by keys.
Each key must be unique, and it is used to access the value associated with it.

Mutable – You can add, change, or remove items.
Unordered (before Python 3.7) – Now it maintains the insertion order.
Key–Value Mapping – Each value is accessed through its key.
Unique Keys – No duplicate keys allowed.
Dynamic – Can grow or shrink in size.

<img width="851" height="470" alt="Screenshot 2025-10-14 181823" src="https://github.com/user-attachments/assets/3536c460-7d44-4857-9893-3a6d4252dd68" />
<img width="851" height="470" alt="Screenshot 2025-10-14 181823" src="https://github.com/user-attachments/assets/6ddd3b1f-ca34-4263-8515-bf77b98fd973" />


<img width="1148" height="861" alt="Screenshot 2025-10-14 173931" src="https://github.com/user-attachments/assets/ccce04cd-da8e-45b6-a8ba-5db188711868" />

<img width="1095" height="421" alt="Screenshot 2025-10-14 174023" src="https://github.com/user-attachments/assets/e973f1db-2f0b-452b-9d3f-87380d3de3cb" />

<img width="1166" height="643" alt="Screenshot 2025-10-14 174031" src="https://github.com/user-attachments/assets/06e801d5-8e08-4308-9234-eec46c4202e8" />



## set

A set in Python is an unordered collection of unique elements.
It is mainly used when you want to store multiple items but don’t want duplicates.
Sets are mutable, but the elements inside must be immutable (like numbers, strings, or tuples).

Unordered – Items don’t have a fixed position or index.
Unique elements – Duplicate items are automatically removed.
Mutable – You can add or remove elements.
Heterogeneous – Can store different data types.
No indexing or slicing (because sets are unordered).

<img width="1209" height="819" alt="Screenshot 2025-10-14 182902" src="https://github.com/user-attachments/assets/5c513d11-baeb-4785-a06f-1affe0e82be6" />











