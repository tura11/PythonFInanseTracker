import os
import tempfile
import unittest
import pandas as pd
from datetime import datetime

# Import the CSV class from your finance tracker module.
# Adjust the import below to match your file/module name.
from main import CSV

class TestCSVMethods(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and CSV file for testing.
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_csv_file = os.path.join(self.test_dir.name, "test_finance_data.csv")
        # Override the CSV file path to use the temporary file.
        CSV.CSV_FILE = self.test_csv_file

        # Ensure the file does not exist before each test.
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def tearDown(self):
        # Clean up the temporary directory.
        self.test_dir.cleanup()

    def test_initialize_csv_creates_file(self):
        # When the CSV file does not exist, initialize_csv should create it.
        CSV.initialize_csv()
        self.assertTrue(os.path.exists(self.test_csv_file), "CSV file was not created.")
        # Check that the file has the correct column headers.
        df = pd.read_csv(self.test_csv_file)
        self.assertListEqual(list(df.columns), CSV.COLUMNS, "CSV file columns do not match expected headers.")

    def test_add_entry_appends_row(self):
        # First, initialize the CSV.
        CSV.initialize_csv()
        # Add a sample entry.
        test_date = "15-03-2025"
        test_amount = 100.0
        test_category = "income"
        test_description = "Test income"
        CSV.add_entry(test_date, test_amount, test_category, test_description)
        # Read the CSV file and check that the new row is present.
        df = pd.read_csv(self.test_csv_file)
        self.assertEqual(len(df), 1, "Expected one row in the CSV file.")
        self.assertEqual(df.iloc[0]["date"], test_date)
        self.assertEqual(float(df.iloc[0]["amount"]), test_amount)
        self.assertEqual(df.iloc[0]["category"], test_category)
        self.assertEqual(df.iloc[0]["description"], test_description)

    def test_get_transactions_returns_filtered_dataframe(self):
        # Initialize and populate the CSV with multiple entries.
        CSV.initialize_csv()
        entries = [
            {"date": "01-01-2025", "amount": 100.0, "category": "income", "description": "Salary"},
            {"date": "15-01-2025", "amount": 50.0, "category": "expense", "description": "Groceries"},
            {"date": "10-02-2025", "amount": 200.0, "category": "income", "description": "Bonus"},
            {"date": "20-03-2025", "amount": 70.0, "category": "expense", "description": "Utilities"},
        ]
        for entry in entries:
            CSV.add_entry(entry["date"], entry["amount"], entry["category"], entry["description"])

        # Retrieve transactions within a specific date range.
        df_filtered = CSV.get_transactions("01-01-2025", "28-02-2025")
        # Expected rows: entries from 01-01-2025, 15-01-2025, and 10-02-2025.
        self.assertEqual(len(df_filtered), 3, "Filtered transactions count is incorrect.")

        # Validate summary calculations.
        total_income = df_filtered[df_filtered["category"] == "income"]["amount"].sum()
        total_expense = df_filtered[df_filtered["category"] == "expense"]["amount"].sum()
        self.assertAlmostEqual(total_income, 300.0, msg="Total income calculation is incorrect.")
        self.assertAlmostEqual(total_expense, 50.0, msg="Total expense calculation is incorrect.")

if __name__ == "__main__":
    unittest.main()
