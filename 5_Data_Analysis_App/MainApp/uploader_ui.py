import customtkinter as ctk
import pickle
import webbrowser

import pandas as pd

from src.MainApp.excel_uploader import browse_file, upload_file
from src.MainApp.explorer_ui import ExplorerUI

class MainAppUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.controller = master
        self.data = self.load_data("outputs/ons_data.pkl")

        self.title_font = ctk.CTkFont(family="Arial", size=16, weight="bold")
        self.link_font = ctk.CTkFont(family="Arial", size=12, underline=True)

        self.create_frames()
        self.configure_grid()
        self.populate_ui()

    def load_data(self, filepath):
        """Load data from a pickle file."""
        try:
            with open(filepath, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error loading data: {e}")
            return {}

    def open_browse(self):
        """Open the file browser to select a file."""
        browse_file(self.file_path_entry)

    def open_upload(self):
        """Handle the upload of a selected file."""
        self.file_path = self.file_path_entry.get()
        df = pd.read_excel(self.file_path)
        if upload_file(self.file_path):
            print("File uploaded successfully!")
            explorer_frame = self.controller.get_frame(ExplorerUI)
            explorer_frame.load_excel_file(self.file_path)
            explorer_frame.update_treeview(df)
            self.controller.show_frame(ExplorerUI)
        else:
            print("File upload failed.")

    def create_frame(self, title, row_pos, col_pos, stick_type, is_upload_frame=False):
        """Create a UI frame with a title and optional upload functionality."""
        frame = ctk.CTkFrame(self, fg_color="#333333", border_color="white", border_width=2)
        frame.grid(row= row_pos, column= col_pos, sticky= stick_type, padx=3, pady=3)

        # Create title label
        title_label = ctk.CTkLabel(frame, text=title, font=self.title_font if is_upload_frame else None,
                                   text_color="white")
        title_label.grid(row=0, column=0, padx=3, pady=3, sticky="W")

        if is_upload_frame:
            self.setup_upload_frame(frame)

        return frame

    def setup_upload_frame(self, frame):
        """Set up the upload frame components."""
        self.file_path_entry = ctk.CTkEntry(frame)
        self.file_path_entry.grid(row=1, column=0, padx=3, pady=3, sticky="ew")

        ctk.CTkButton(frame, text="Browse File", command=self.open_browse).grid(row=2, column=0, padx=3, pady=3, sticky="ew")
        ctk.CTkButton(frame, text="Upload File", command=self.open_upload).grid(row=3, column=0, padx=3, pady=3, sticky="ew")
        ctk.CTkButton(frame, text="Go to Explorer", command=lambda: self.controller.show_frame(ExplorerUI)).grid(row=4, column=0, padx=3, pady=3, sticky="ew")

    def create_frames(self):
        """Create the main UI frames."""
        self.upload_frame = self.create_frame("Upload Excel File", 0,0, "ne", is_upload_frame=True)
        self.links_frame = self.create_frame("ONS Recent Release Links", 0,1, "ne")

    def configure_grid(self):
        """Configure grid layout for the main frame."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def open_link(self, url):
        """Open a URL in a web browser."""
        webbrowser.open(url)

    def populate_ui(self):
        """Populate the UI with links from the loaded data."""
        for index, (link_title, link) in enumerate(self.data.items()):
            link_label = ctk.CTkLabel(
                self.links_frame,
                text=f"{index + 1}. {link_title}",
                text_color="white",
                font=self.link_font,
                cursor="hand2"
            )
            link_label.grid(row=index + 1, column=0, pady=3, padx=3, sticky="W")
            link_label.bind("<Button-1>", lambda e, url=link: self.open_link(url))

