# Laboration 1. Python intro lab

## Getting started

1. Accept the GitHub Classroom invitation if your teacher has shared one.
2. Open your repository on GitHub.
3. Clone it to your computer with `git clone <repo-url>`.
4. Open the folder in VS Code.
5. Start working through the lab in the order described below.

This assumes that you already understand the basic Git workflow. After you have cloned the repository, you are expected to commit and push your work regularly.

```bash
git add -A
git commit -m "a short message about what you changed"
git push
```

When you open vscode, if you want to do it more professionally

1. Open an integrated terminal, make sure it’s a bash terminal
2. Split that terminal into two terminals, using the split button on the right side
3. Use the left terminal to write the code, e.g “python student_system.py”
4. Use the right terminal to write git commands

## Read this first

**Grade:** `G` only

To pass, you need to complete all parts of the lab:

- `part_1_fundamentals.ipynb`
- `number_list_manager.py`
- `inventory_manager.py`
- `student_system.py`

Focus on learning, not on rushing.

This is a warm-up lab. The point is to make you practice the basics properly before we move on to more practical data work later in the course.

## Submission

You submit by pushing commits to your repository.

When the lab is reviewed, the latest valid version on your repository is the one that counts. That means you should:

- commit regularly
- keep your repository clean
- make sure your latest pushed version is the one you want reviewed

## Rules

The lab is individual, I do not really recommend doing this together with someone else, that usually leads to us finding ways to not overcome things on our own. However, you could discuss small parts of it, ask for tips, but generally try to avoid doing it “together” with someone else. The first rule of learning programming is you need to be patient, and ENDURE. Learning how to code involves suffering mentally, it is part of the process.

You may use AI to ask for explanations, examples, or help understanding an error message. You may not use AI to generate the actual solutions for you. The point of this lab is to make you practice problem-solving yourself.

If you get stuck, do things like this instead:

- test smaller pieces of code
- print values and inspect what is happening, we do this all the time, even senior devs! Use print A LOT to see how the code is flowing. Are you entering an expected loop? are you exiting one? did you if-statement trigger as you’d expect? PRINT!!!!
- ask for explanations, not full solutions

## Introduction

This lab is meant to help you start getting comfortable with the fundamentals of Python.

That means things like:

- variables
- data types
- `if` statements
- loops
- functions
- lists
- dictionaries
- basic error handling

Programming is learned by coding. Not by just reading. Not by only watching videos. And not by asking AI to do the thinking for you. You will never quite feel ready to start, you just have to take the first step. What seems like the easiest thing to do? 

## How to work through the lab

Do the parts in this order.

### Part 1. Fundamentals notebook

Open:

`part_1_fundamentals.ipynb`

This is the most guided part. Some tasks want code. Some want text. Some want both.

Use markdown cells if you want to explain something in words.

Write all code and comments in English. I REPEAT, ALL CODE SHOULD BE IN ENGLISH. We never write code in our native languages (e.g swedish)

### Part 2. Warm-up programs

Before you build the larger student system, do these two smaller terminal programs:

- `number_list_manager.py`
- `inventory_manager.py`

These are there to warm you up on:

- menu logic
- functions
- loops
- formatting output nicely
- working with lists and dictionaries

Start with `number_list_manager.py`.

Then move on to `inventory_manager.py`.

## Part 3. Student system - Practice problem solving

The assignment below can be quite challenging for a beginner, but if you really get through it, you’ll be a lot closer to knowing most of the basics of python!

### Description:

You are going to build a simple system for managing students through the terminal.
The file `student_system.py` contains starter data for all students, and you should build more functionality on top of it. You are not expected to do heavy error handling, just very basic error handling is fine. 

When the user enters a choice that does not fit, you can try to show error messages and show the alternatives again.

The program should welcome the user and give them a menu with the following numbered choices. The flow below is not suggestion, it’s what I literally exactly how the program should work (if you make some improvements that’s okay, but you can never reduce the complexity) 

```python

[q] Shut down the program
[0] List all students with name and student ID.
[1] Add a student with student ID and name
[2] Remove a student
```

### Example of what it can look like when using parts of the program:

*starts the program*

```python
Welcome to the greatest student system in the world.
What would you like to do?
[q] - Exit
[0] - List all students from the registry
[1] - Add a student to the registry
[2] - Remove a student from the registry
```

*chooses 0*

```python
Choose a student
[q] Go back
[0] ID: 11230 - Tobias Fors
[1] ID: 11231 - Karin Börjell
....
```

*0*

```python
What would you like to do?
[q] Go back
[0] Show summary of grades
[1] List personal information
```

*0*

```python
Pythonprogrammering 1: 1
Pythonprogrammering 2: 4
------------------------
```

Press enter to continue

*enter*

```python
What would you like to do?
[q] Go back
[0] Show summary of grades
[1] List personal information
```

*1*

```python
Name: Tobias Fors
ID: 11230
Email: tobias@utvecklarakademin.se
Age: 30
```

Press enter to continue

*enter*

```python
What would you like to do?
[q] Go back
[0] Show summary of grades
[1] List personal information
```

Etc. You can add more functionality if you want. The purpose here is that you should practice `if` statements, `while` loops, `for` loops, lists, and dictionaries. It is a "boring" task that helps you warm up. Again: DO NOT USE AI!

# Things to keep in mind

- Try to show the menu alternatives often
- Use functions and loops a lot!
- Try to give feedback to the user when they do something
- The program should NOT shut down after you perform an action. If you add a student, for example, you should just return to the menu
- When you show information, you should never just print a list or dictionary. I expect you to loop through the data and present it nicely for the user
- Remember that **while loops** can help you with menus
- Avoid having a function call itself recursively
- Before you submit the assignment, you should test the program
- Do not get stuck in details. **Exactly** how you do it or how it looks does not matter. You should always ask yourself: Have I created something that feels good to use?

**BONUS** (not required): The user should also be able to add grades and courses for individual students when adding a student through option [1] in the start menu