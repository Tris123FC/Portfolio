import pandas as pd

class TreeViewFunctions:
    def __init__(self, explorer_ui):
        self.explorer_ui = explorer_ui

    def apply_selected_function(self, df, column1, column2, func_combobox):
        selected_function = func_combobox.get()
        print(f"Selected function: {selected_function}")  # Debugging line

        # Check for valid columns and handle None values
        columns_to_apply = [col for col in [column1, column2] if col is not None and col in df.columns]

        if not columns_to_apply:
            print("No valid columns selected.")
            return

        function_mapping = {
            "Convert to Integer": self.reformat_column_int,
            "Convert to Float": self.reformat_column_float2
        }

        for column in columns_to_apply:
            if selected_function in function_mapping:
                self.modified_df = function_mapping[selected_function](df, column)
                print(f"Function applied to column: {column}")
            else:
                print("Invalid function selected.")
                return None  # Explicitly return None if function is invalid

        self.explorer_ui.update_treeview(self.modified_df)
        return self.modified_df

    def reformat_column_int(self, df, column):
        """Convert the specified column to integers and return the modified DataFrame."""
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).astype(int)
            print(f"DataFrame after conversion to integer:\n{df.head()}")
        else:
            print(f"Column '{column}' does not exist in the DataFrame.")
        return df

    def reformat_column_float2(self, df, column):
        """Convert the specified column back to floats, rounding to 2 decimals, and return the modified DataFrame."""
        if column in df.columns:
            if df is not None and column in df.columns:
                df[column] = pd.to_numeric(df[column], errors='coerce').round(2)
                print(f"Reverted '{column}' back to float values (rounded to 2 decimals):\n{df.head()}")  # Debugging line
            else:
                print("Original DataFrame is not available or doesn't have the column to revert changes.")
        else:
            print(f"Column '{column}' does not exist in the DataFrame.")
        return df
