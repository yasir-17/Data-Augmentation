import unittest
from src.extract_data import extract_data

class TestExtractData(unittest.TestCase):
    def test_extract_data(self):
        # Define a test URL for a PDF file
        url = "https://www.normanok.gov/sites/default/files/documents/2024-04/2024-04-04_daily_incident_summary.pdf"

        # Call the function
        data = extract_data(url)

        # Assertions
        self.assertIsInstance(data, list)  # Check if data is a list
        self.assertTrue(len(data) > 0)  # Check if data is not empty

if __name__ == '__main__':
    unittest.main()
