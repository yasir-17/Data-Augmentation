import urllib.request
import fitz
import camelot

def extract_data(url):
    try:
        # Download the PDF data using urllib.request
        response = urllib.request.urlopen(url)
        pdf_data = response.read()

        # Create a temporary in-memory file for processing
        with open('temp.pdf', 'wb') as temp_file:
            temp_file.write(pdf_data)

        # Open the PDF using fitz
        pdf_file = fitz.open('temp.pdf')

        # Extract tables using camelot
        tables = camelot.read_pdf(pdf_file.name, pages='all', flavor='stream')
        data = []

        # Iterate over the tables, skipping the header row if necessary
        for (i, table) in enumerate(tables):
            table_data = table.df.values.tolist()
            if i == 0:
                table_data = table_data[2:]  # Skip header if it's in the first table

            # Merge rows when the first column is empty
            merged_data = []
            j = 0
            while j < len(table_data):
                row = table_data[j]
                if row[0] == '':
                    merged_row = row
                    for k in range(1, 3):  # Merge the next two rows
                        if j + k < len(table_data):
                            merged_row = [merged_row[m] + table_data[j + k][m] for m in range(len(merged_row))]
                    merged_data.append(merged_row)
                    j += 3  # Skip the next two rows
                else:
                    merged_data.append(row)
                    j += 1

            # Append merged table data to the main list
            data.extend(merged_data)

        # Close the temporary file (optional but recommended)
        temp_file.close()
        return data
    except Exception as e:
        print(f"An error occurred while processing the PDF: {e}")
        return []  # Return an empty list on error