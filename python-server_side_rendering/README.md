# Python Server-Side Rendering

This project introduces server-side rendering in Python using Flask and Jinja.

## Learning Objectives

By completing this project, I learned how to:

* Generate text files from templates in Python.
* Handle missing and invalid data.
* Build basic Flask applications.
* Render HTML templates using Jinja.
* Reuse HTML components with Jinja includes.
* Use loops and conditional statements in Jinja templates.
* Read data from JSON and CSV files.
* Use Flask query parameters.
* Filter data based on URL parameters.
* Read and display data from a SQLite database.
* Render data from multiple sources using the same HTML template.

## Project Structure

```text
python-server_side_rendering/
├── README.md
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── template.txt
├── items.json
├── products.json
├── products.csv
├── products.db
└── templates/
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── header.html
    ├── footer.html
    ├── items.html
    └── product_display.html
```

## Tasks

### Task 0 - Simple Templating Program

Creates personalized invitation files from a text template and attendee data.

The program handles:

* Invalid input types.
* Empty templates.
* Empty attendee lists.
* Missing values using `N/A`.
* Sequential output files.

### Task 1 - Flask and Jinja Templates

Introduces Flask routes and Jinja templates.

Pages include:

* Home
* About
* Contact

Reusable header and footer templates are included using Jinja.

### Task 2 - Dynamic Templates

Reads items from a JSON file and displays them dynamically using:

* Jinja loops.
* Jinja conditions.
* Flask template variables.

### Task 3 - JSON and CSV Data

Displays product information from either JSON or CSV files.

The data source is selected using a query parameter:

```text
/products?source=json
/products?source=csv
```

Products can also be filtered by ID:

```text
/products?source=json&id=1
```

### Task 4 - SQLite Data

Extends the product application to support SQLite as another data source.

Example:

```text
/products?source=sql
```

The same Jinja template is used for JSON, CSV, and SQLite data.

## Running the Application

Run the final Flask application with:

```bash
python3 task_04_db.py
```

Then open:

```text
http://127.0.0.1:5000/
```

Available routes include:

```text
/
/about
/contact
/items
/products?source=json
/products?source=csv
/products?source=sql
```

## Technologies

* Python
* Flask
* Jinja
* HTML
* JSON
* CSV
* SQLite
