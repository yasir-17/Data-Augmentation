import unittest
from src.createdb import createdb
from io import StringIO
from contextlib import redirect_stdout

class TestCreateDB(unittest.TestCase):
    def test_createdb(self):
        # Define test data
        db_name = "resources/normanpd.db"  # Use in-memory database for testing
        table_name = "test_table"
        data = [
            ["01/01/2022 12:00", "123", "Location A", "Nature A", "EMSSTAT"],
            ["01/01/2022 13:00", "456", "Location B", "Nature B", "Other"],
        ]

        # Capture printed output
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            # Call the function
            createdb(db_name, table_name, data)

        # Get the printed output as a string
        printed_message = captured_output.getvalue().strip()

        # Assertions
        self.assertTrue("Database created successfully" in printed_message) # Check if table was created successfully

if __name__ == '__main__':
    unittest.main()
