---
title: Mini Project
---

## Mini Project

---

### Overview

Your client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders.

<aside class="notes">
    This is the scope of your new project.
    Each week will cover some of the requirements and look to you to build an app to meet them.
</aside>

---

### Requirements

As a business:

- I want to maintain a collection of `products` and `couriers`.
- When a customer makes a new `order`, I need to create this on the system.
- I need to be able to update the status of an `order` i.e: `preparing`, `out-for-delivery`, `delivered`.
- When I exit my app, I need all data to be persisted and not lost.
- When I start my app, I need to load all persisted data.
- I need to be sure my app has been tested and proven to work well.
- I need to receive regular software updates.

<aside class="notes">
    This may look scary, but these are the kinds of functionality that will be learned in the first six weeks
    We will be covering a little part of it each week based on what you have just learned.
    And each week will build on top of the work you have already done.
</aside>

---

## Technical Specifications

---

### User Interface

You will be building a program that runs on the command line (CLI).

- UI should be logical, clear, and simple to navigate.
- It should display a menu of options, some may be nested.
- There should be the option to exit / return to main menu.
- It should handle invalid input.

<aside class="notes">
    We are not expecting a fully functional web page with a form.  
    As you have already seen, there is more than one way to get a user to interact with a program.
</aside>

---

### Data Persistence

You will incrementally adopt three methods to persist data between user sessions:

- `txt`: Initially we'll store our data in plaintext files.
- `csv`: As our data changes shape, we'll need to switch to the CSV format.
- `SQL`: Ultimately, we'll finish up using a database.

<aside class="notes">
    Don't worry now about what each of them are, we will cover each of them and their usages in time.
</aside>

---

### Testing

Python has some basic testing functionality built-in which we'll use to test the quality of our code. This will allow us to be confident that our app works as we intended it to.

<aside class="notes">
    Remember, programming is more than just writing code, it's about being confident in delivering something proven to work.
</aside>

---

### Data Visualisation

We'll want to build some bar charts to help our client better understand the business. For this we'll use:

`Jupyter Notebooks + Matplotlib`

<aside class="notes">
    Data Visualisation appears a stretch goal in WK6
</aside>

---

### Suggested Project Structure<!-- .element: class="centered" -->

![structure](img/structure.png)<!-- .element: class="centered" -->

---

### Method

- You will be allotted enough time each week to work on your project.
- Your instructor will brief you on the requirements and goals each week.
- You should each produce your own app, however pairing up with a colleague is encouraged.
- At the end you will be expected to present your finished app to a friendly panel for review.

#### Available Time: 6 Weeks

<aside class="notes">
    It may be worth pointing out the Agile nature of Software Development...
</aside>

---

### Stuck?

Getting stuck on something is not fun for anyone. Due to the size of the group please follow this recommended workflow:

When stuck:

- Don't panic: Relax, take a break, think about the problem.
- Google it: There is a wealth of information on the web and you'll likely find the solution to your problem quite quickly.
- Syntax: If it's a syntax problem try referring to earlier slides, or the official Python Docs / W3 Schools.
- Ask a colleague: Ask someone in the group. It's likely they too have come across and solved your problem.
- Ask your instructor: If all else fails, reach out to your instructor for some guidance.

<aside class="notes">
    There will be plenty of time to complete the basics of the mini-project.
    Remember it's not a race, we want everyone to complete it.
</aside>

---

### Glossary

- `CLI` Command Line Interface
- `CRUD` Create, Read, Update, Delete
- `Refactor` The process of rewriting code to _improve_ it or to fix code smells
- `Code Smell` Code that doesn't adhere to best practices
- `CSV` Comma Separated Value
- `SQL` Structured Query Language
- `Data Layer` The part of your code that handles all data interaction
- `Storage Layer` The part of your code that handles all file storage
- `UI/UX` User Interface / User Experience

---

### Resources

- https://realpython.com/
- https://blog.finxter.com/python-cheat-sheet/
- https://www.mysqltutorial.org/
- https://websitesetup.org/mysql-cheat-sheet/

---

### Libraries

- pylint
- black (code-formatter)
- pymysql
- matplotlib

---

![](img/force.jpg)<!-- .element: class="centered" -->
