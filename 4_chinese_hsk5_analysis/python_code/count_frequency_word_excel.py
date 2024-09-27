import openpyxl
from docx import Document
# Function to count the occurrences of a word in a Word document
def count_word_frequency_in_word(file_path, search_word):
    doc = Document(file_path)
    word_count = 0

    # Iterate through each paragraph in the document
    for para in doc.paragraphs:
        word_count += para.text.lower().count(search_word.lower())

    return word_count
# Function to process each cell in the B column and write the count to the E column
def process_excel_and_update_counts(excel_file_path, word_file_path, sheet_name):
    # Load the workbook and the specified sheet
    workbook = openpyxl.load_workbook(excel_file_path)
    worksheet = workbook[sheet_name]

    # Iterate through each cell in column B (starting from B2)
    for row in range(2, worksheet.max_row + 1):  # Assuming data starts from row 2
        cell_b = worksheet[f'B{row}']
        search_word = cell_b.value

        if search_word:  # Check if the cell is not empty
            # Count the frequency of the word in the Word document
            frequency = count_word_frequency_in_word(word_file_path, search_word)
            print(f"The word '{search_word}' appears {frequency} times in the Word file.")

            # Write the frequency count in the corresponding F column cell
            worksheet[f'I{row}'] = frequency

    # Save the workbook with the updated counts
    workbook.save(excel_file_path)
    print("Excel file updated successfully.")


# Example usage
excel_file_path = "hsk5_voc.xlsx"  # Replace with your Excel file path
word_file_path = "hsk_chinese_text_20240829_104830.docx"  # Replace with your Word file path
sheet_name = "Sheet1"  # Replace with your sheet name

# Process the Excel file and update counts in column E
process_excel_and_update_counts(excel_file_path, word_file_path, sheet_name)