# src/MainApp/excel_uploader.py
import os
import shutil
from tkinter import filedialog, messagebox


def browse_file(file_path_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
    if file_path:
        file_path_entry.configure(text_color="white")
        file_path_entry.delete(0, 'end')
        file_path_entry.insert(0, file_path)
    else:
        file_path_entry.configure(text_color="red")
        file_path_entry.delete(0, 'end')
        file_path_entry.insert(0, "Error: Select a .xlsx or .csv file.")


def upload_file(file_path_entry):
    file_path = file_path_entry
    print("upload_file called")

    if file_path and not file_path.startswith("Error"):
        output_folder = os.path.abspath("outputs")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file_name = os.path.basename(file_path)
        destination_path = os.path.join(output_folder, file_name)

        try:
            shutil.copy(file_path, destination_path)
            messagebox.showinfo("Success", f"File uploaded successfully to {destination_path}")
            return destination_path  # Return the destination file path

        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload file: {e}")

    else:
        messagebox.showwarning("Invalid Path", "Please provide a valid file path.")

