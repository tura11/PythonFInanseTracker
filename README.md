# Financial Transactions Manager

This project is a simple command-line application for managing and analyzing financial transactions using CSV files. It allows users to add new transactions, view transactions within a specified date range (with a summary of income, expense, and net savings), and visualize the data in a plot.

## Features

- **CSV Initialization:** Automatically creates a CSV file (`finance_data.csv`) with the required columns if it does not exist.
- **Adding Transactions:** Users can add new financial transactions by providing the date, amount, category (income or expense), and description.
- **Transaction Filtering:** Retrieve and display transactions within a given date range, along with a summary:
  - Total income
  - Total expenses
  - Net savings (income minus expenses)
- **Visualization:** Plot daily income and expense trends using Matplotlib.
- **Input Validation:** Ensures dates, amounts, and categories are entered correctly.

## Project Structure

- **CSV Class (in the main module):**
  - `initialize_csv()`: Checks for the CSV file and creates it with headers if missing.
  - `add_entry()`: Appends a new transaction to the CSV file.
  - `get_transactions()`: Filters transactions within a date range, prints the data and summary.
- **Data Entry Module (`data_entry.py`):**
  - `get_date()`: Prompts for a date (with optional default to today's date) and validates the format (`dd-mm-YYYY`).
  - `get_amount()`: Prompts for the transaction amount and validates it is greater than zero.
  - `get_category()`: Prompts for the transaction category, accepting `I` for income and `E` for expense.
  - `get_description()`: Prompts for a transaction description.
- **Visualization:**
  - `polt_transactirons()`: Creates a line plot for income and expenses over time using Matplotlib.

## Requirements

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- Standard Python libraries (`csv`, `datetime`)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
