
import customtkinter as ctk
import pandas as pd
from tkinter import ttk, messagebox
from components.custom_button import CustomButton
from components.custom_frame import CustomFrame
from src.MainApp.excel_uploader import browse_file, upload_file
from src.MainApp.tree_view_functions import TreeViewFunctions  # Updated import
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import openpyxl
import os


class ExplorerUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.file_path = None
        self.sheet_names = []
        self.df = pd.DataFrame()
        self.modified_df = None
        self.column1 =None
        self.column2 =None


        # Create an instance of TreeViewFunctions
        self.tree_view_functions = TreeViewFunctions(self)


        self.create_layout()

    def create_layout(self):
        """Setup the overall UI layout."""
        self.configure_grid()
        self.setup_frames()
        self.setup_treeview()
        self.setup_widgets_frame2a()
        self.setup_widget_frame2b()
        self.setup_chart_area()

    def configure_grid(self):
        """Configure grid layout for the UI."""
        self.grid_columnconfigure(0, weight=1, uniform="col")  # Column 0 with weight 2
        self.grid_columnconfigure(1, weight=1, uniform="col")  # Column 1 with weight 1
        self.grid_rowconfigure((0, 1), weight=1, uniform="row")

    def setup_frames(self):
        """Setup frames used in the layout."""
        self.frame1 = self.create_frame(row=0, col=0, color="#333333")
        self.frame1b = self.create_frame(row=0, col=1, color="white")
        self.frame2a = self.create_frame(row=1, col=0, color="#333333")
        self.frame2b = self.create_frame(row=1, col=1, color="#333333")


    def create_frame(self, row, col, col_span=1, color="white"):
        """Helper method to create frames."""
        frame = ctk.CTkFrame(self, fg_color=color)
        frame.grid(row=row, column=col, columnspan=col_span, padx=3, pady=3, sticky="nsew")
        return frame

    def setup_treeview(self):
        """Setup the TreeView widget with a scrollbar."""
        self.treeview = ttk.Treeview(self.frame1, show="headings")
        self.treeview.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ctk.CTkScrollbar(self.frame1, command=self.treeview.yview)
        self.scrollbar.grid(row=0, column=0, sticky="w")
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(0, weight=1)

    def setup_widgets(self):
        for row in range(self.df.shape[0]):
            self.frame2a.labels

    def setup_widgets_frame2a(self):
        """Setup all widgets in frame2."""

        self.frame_title = ctk.CTkLabel(self.frame2a, text="Data Selection & Manipulation", corner_radius= 8, fg_color="Azure4",
                                        anchor="center")
        self.frame_title.grid(row=0, column=0, columnspan=3, padx=3, pady=3, sticky="nsew")
        self.select_button = ctk.CTkButton(self.frame2a, text="New File", command=self.open_browse)
        self.select_button.grid(row=1, column=0, padx=3, pady=1, sticky="nswe")

        self.file_path_entry = ctk.CTkEntry(self.frame2a, width=20)
        self.file_path_entry.grid(row=1, column=1, padx=3, pady=1, sticky="nswe")

        self.upload_button = ctk.CTkButton(self.frame2a, text="Upload File", command=self.open_upload)
        self.upload_button.grid(row=1, column=2, padx=3, pady=1, sticky="nswe")

        # Setup Sheet Combobox
        self.combobox_label = ctk.CTkLabel(self.frame2a, text="Select Sheet")
        self.combobox_label.grid(row=2, column=0, padx=3, pady=1, sticky="nswe")

        self.sheet_combobox = ttk.Combobox(self.frame2a, state="readonly")
        self.sheet_combobox.grid(row=2, column=1, padx=3, pady=1, sticky="we")
        self.sheet_combobox.bind("<<ComboboxSelected>>", self.load_sheet_data)

        # Setup Column Combobox
        self.select_column1_label = ctk.CTkLabel(self.frame2a, text="Select Column 1")
        self.select_column1_label.grid(row=3, column=0, padx=3, pady=1, sticky="nswe")

        self.col1_combobox = ttk.Combobox(self.frame2a, state="readonly")
        self.col1_combobox.grid(row=3, column=1, padx=3, pady=1, sticky="we")
        self.col1_combobox.bind("<<ComboboxSelected>>", self.select_column)

        self.select_column2_label = ctk.CTkLabel(self.frame2a, text="Select Column 2")
        self.select_column2_label.grid(row=4, column=0, padx=3, pady=1, sticky="nswe")

        self.col2_combobox = ttk.Combobox(self.frame2a, state="readonly")
        self.col2_combobox.grid(row=4, column=1, padx=3, pady=1, sticky="we")
        self.col2_combobox.bind("<<ComboboxSelected>>", self.select_column)

        # Setup Function Combobox
        self.select_function_label = ctk.CTkLabel(self.frame2a, text="Select Function")
        self.select_function_label.grid(row=5, column=0, padx=3, pady=1, sticky="nswe")

        self.func_combobox = ttk.Combobox(self.frame2a, state="readonly")
        self.func_combobox.grid(row=5, column=1, padx=3, pady=1, sticky="we")
        self.func_combobox["values"] = ["Convert to Integer", "Convert to Float"]
        self.func_combobox.bind("<<ComboboxSelected>>", self.apply_functions)

        rows = self.frame2a.grid_size()[1]  # Get the total number of rows
        columns = self.frame2a.grid_size()[0]  # Get the total number of columns

        # Configure weight for all rows
        for i in range(rows):
            self.frame2a.grid_rowconfigure(i, weight=1)

        # Configure weight for all columns
        for j in range(columns):
            self.frame2a.grid_columnconfigure(j, weight=1)

    def setup_widget_frame2b(self):
        self.frame_title = ctk.CTkLabel(self.frame2b, text="Data Visualisation", corner_radius=8, fg_color="Azure4",
                                        anchor="center")
        self.frame_title.grid(row=0, column=0, columnspan = 3, padx=3, pady=3, sticky="nswe")
        self.chart_label = ctk.CTkLabel(self.frame2b, text="Select Chart")
        self.chart_label.grid(row=1, column=0, padx=3, pady=1, sticky="nswe")
        self.chart_combobox = ttk.Combobox(self.frame2b, state="readonly")
        self.chart_combobox.grid(row=1, column=1, padx=3, pady=1, sticky="we")
        self.apply_button = ctk.CTkButton(self.frame2b, text="Apply", command=self.apply_chart)
        self.apply_button.grid(row=1, column=2, padx=3, pady=1, sticky="nswe")

        self.frame2b.grid_rowconfigure(0, weight=1)
        self.frame2b.grid_columnconfigure(0, weight=1)

        rows = 7  # Get the total number of rows
        columns = 3  # Get the total number of columns

        # Configure weight for all rows
        for i in range(rows):
            self.frame2b.grid_rowconfigure(i, weight=1)

        # Configure weight for all columns
        for j in range(columns):
            self.frame2b.grid_columnconfigure(j, weight=1)


    def setup_chart_area(self):
        # Create the chart frame without the 'text' argument
        self.chart_frame = ctk.CTkFrame(self.frame1b, fg_color="white")  # Example width and height

        self.chart_frame.grid(row=0, column= 0, padx=3, pady=3)  # Pack the frame into its parent

        self.frame1b.grid_rowconfigure(0, weight=1)
        self.frame1b.grid_columnconfigure(0, weight=1)

    def load_excel_file(self, file_path):
        """Load an Excel file and populate the ComboBox with sheet names."""
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"Excel file not found: {file_path}")
            return

        try:
            self.file_path = file_path
            workbook = openpyxl.load_workbook(self.file_path, data_only=True)
            self.sheet_names = workbook.sheetnames

            if not self.sheet_names:
                messagebox.showinfo("Info", "No sheets found in the workbook.")
                return

            self.sheet_combobox['values'] = self.sheet_names
            self.sheet_combobox.current(0)
            self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_combobox.get())
            self.modified_df = self.df.copy()

            self.load_sheet_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error loading Excel file: {e}")

    def load_sheet_data(self, event=None):
        """Load data from the selected sheet and display it in the TreeView."""
        selected_sheet = self.sheet_combobox.get()
        if not selected_sheet:
            print("No sheet selected. Please select a sheet.")
            return

        try:
            self.df = pd.read_excel(self.file_path, sheet_name=selected_sheet)

            # Update the column combobox with the new DataFrame columns
            self.col1_combobox['values'] = self.df.columns.tolist()
            self.col1_combobox.set('No Column Selected')

            self.col2_combobox['values'] = self.df.columns.tolist()
            self.col2_combobox.set('No Column Selected')

            self.chart_combobox['values'] = ["line chart", 'scatter plot']
            self.chart_combobox.current(0)

            self.update_treeview(self.df)
            return self.df
        except Exception as e:
            print(f"Error loading sheet data: {e}")
            print(f"Error loading sheet data: {e}")

    def select_column(self, event):
        """Get the selected column name from either col1_combobox or col2_combobox."""
        selected_column = None

        # Determine which combobox triggered the event and get the selected column name
        if event.widget == self.col1_combobox:
            self.column1 = self.col1_combobox.get()
            return self.column1
        elif event.widget == self.col2_combobox:
            self.column2 = self.col2_combobox.get()
            return self.column2

        else:
            print("No valid combobox triggered the event.")
            return

    def update_treeview(self, modified_df):
        """Update the TreeView with the DataFrame content."""

        # Clear existing data
        self.treeview.delete(*self.treeview.get_children())

        # Clear existing columns in TreeView
        self.treeview["columns"] = modified_df.columns.tolist()

        # Set up columns and headings
        for col in modified_df.columns:
            self.treeview.heading(col, text=col)  # Set column heading
            self.treeview.column(col, anchor="center", width=100)  # Set column width and center alignment

        # Insert rows into the TreeView
        for index, row in modified_df.iterrows():
            self.treeview.insert("", "end", values=list(row))  # Insert row values

        # Adjust column widths based on content
        self.adjust_column_width(modified_df)

    def adjust_column_width(self, df):
        """Adjust column widths in the TreeView based on content."""
        for col in df.columns:
            max_length = max(df[col].astype(str).map(len).max(), len(col)) * 10
            max_length = min(max(max_length, 100), 300)
            self.treeview.column(col, width=max_length)

    def apply_functions(self, event=None):
        selected_function = self.func_combobox.get()

        # Check if both columns are None
        if not self.column1 and not self.column2:
            messagebox.showwarning("Warning", "No column selected.")
            return

        if not selected_function:
            messagebox.showwarning("Warning", "No function selected.")
            return

        # Call the function and refresh the TreeView
        self.modified_df = self.tree_view_functions.apply_selected_function(self.df, self.column1, self.column2,
                                                                            self.func_combobox)
        self.update_treeview(self.modified_df)  # Update with modified DataFrame

    def apply_chart(self, event=None):
        selected_chart= self.chart_combobox.get()
        if not selected_chart:
            messagebox.showwarning("Warning", "No chart selected.")
            return
        self.plot_chart(selected_chart)  # Re-plot after modifications

    def open_browse(self):
        """Open the file browser to select a file."""
        selected_file = browse_file(self.file_path_entry)
        if selected_file:
            self.file_path_entry.delete(0, 'end')  # Clear the entry
            self.file_path_entry.insert(0, selected_file)

    def open_upload(self):
        self.file_path = self.file_path_entry.get()
        if upload_file(self.file_path):
            print("File uploaded successfully!")
            self.load_excel_file(self.file_path)
        else:
            print("File upload failed.")

    def create_line_chart(self, modified_df):
        # Sort the dataframe by the x-axis column (self.column1)
        sorted_df = modified_df.sort_values(by=self.column1)

        plt.figure(figsize=(3, 2))
        plt.plot(sorted_df[self.column1], sorted_df[self.column2], label='Y1', marker='o')
        plt.title('Two-Dimensional Line Chart')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid()

        return plt.gcf()

    def create_scatter_plot(self, modified_df):
        sorted_df = modified_df.sort_values(by=self.column1)
        plt.figure(figsize=(3, 2))
        plt.scatter(sorted_df[self.column1], sorted_df[self.column2], label='Y1', marker='o')
        plt.title('Two-Dimensional Scatter Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid()

        return plt.gcf()

    def plot_chart(self, selected_chart):
        if self.modified_df is not None:
            if selected_chart == 'line chart':
                fig = self.create_line_chart(self.modified_df)
                canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
                self.chart_frame.grid_rowconfigure(0, weight=1)
                self.chart_frame.grid_columnconfigure(0, weight=1)
            if selected_chart == 'scatter plot':
                fig = self.create_scatter_plot(self.modified_df)
                canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
                self.chart_frame.grid_rowconfigure(0, weight=1)
                self.chart_frame.grid_columnconfigure(0, weight=1)
