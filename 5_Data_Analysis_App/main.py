import customtkinter as ctk
from uploader_ui import MainAppUI
from src.MainApp.explorer_ui import ExplorerUI



class MainApp(ctk.CTk):  # Main application inherits from ctk.CTk
    def __init__(self):
        super().__init__()  # Call the parent constructor
        self.title("Uploader")
        self.geometry("800x400")
        self.frames = {}
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create and store frames
        for F in (MainAppUI, ExplorerUI):
            frame = F(self)  # Initialize the frame with self as the parent
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Pack the frame

        self.show_frame(MainAppUI)  # Show the initial frame

    def get_frame(self, frame_class):
        return self.frames[frame_class]


    def show_frame(self, frame_class):
        if frame_class in self.frames:
            frame = self.frames[frame_class]
            frame.tkraise()

        else:
            print(f"Frame {frame_class.__name__} does not exist.")

if __name__ == "__main__":
    app = MainApp()  # Create an instance of MainApp
    app.mainloop()
