import pandas as pd
import subprocess
import tkinter as tk
from tkinter import filedialog

# Create a root window and hide it
root = tk.Tk()
root.withdraw()

# Open a file dialog and get the path of the selected file
file_path = filedialog.askopenfilename()

# Execute the Python script and get the output
output = subprocess.check_output(['python', file_path])

# Convert the output to a DataFrame
df = pd.DataFrame([output])

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
