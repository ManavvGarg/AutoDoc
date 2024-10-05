import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from tkinter import ttk  # Use ttk for modern UI elements
from pathlib import Path
from functions.generate import generate_documentation, generate_readme
from functions.list_project_files import list_project_files
from functions.save_file import save_markdown
import threading  # For running the generation in a separate thread
import time  # To simulate progress bar loading

# Initialize the main application window
root = tk.Tk()
root.title("DocuGenie - AI Documentation Generator")
root.geometry("800x600")

# Style for the application
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10))
style.configure("TLabel", font=("Helvetica", 12))

# Global variables to hold file paths and generated content
uploaded_files = []
readme_content = ""
documentation_content = ""

# Function to handle file uploads
def upload_files():
    global uploaded_files
    uploaded_files = filedialog.askdirectory()
    if uploaded_files:
        file_label.config(text=f"Selected Directory: {uploaded_files}")
    else:
        file_label.config(text="No Directory Selected")

# Function to preview generated README.md and DOCUMENTATION.md
def preview_content():
    global readme_content, documentation_content
    # Display the generated content in the text area
    preview_text.delete(1.0, tk.END)
    preview_text.insert(tk.END, f"README.md:\n\n{readme_content}\n\n")
    preview_text.insert(tk.END, f"DOCUMENTATION.md:\n\n{documentation_content}")

# Function to handle the actual file generation in a thread
def generate_files_thread():
    global readme_content, documentation_content
    progress.start()  # Start the progress bar
    time.sleep(1)  # Simulate loading delay
    project_files = list_project_files(uploaded_files)
    readme_content = generate_readme(project_files)
    documentation_content = generate_documentation(project_files)
    preview_content()  # Call to show preview after generating content
    progress.stop()  # Stop the progress bar

# Function to start the file generation in a separate thread and show loading bar
def generate_files():
    if uploaded_files:  # Only start generation if files have been uploaded
        progress.pack(pady=10)  # Show the progress bar only after files are selected
        thread = threading.Thread(target=generate_files_thread)
        thread.start()
    else:
        messagebox.showwarning("Warning", "Please select a directory first!")

# Function to save the generated markdown files
def save_files():
    if readme_content and documentation_content:
        save_dir = filedialog.askdirectory()
        if save_dir:
            save_markdown(save_dir, readme_content, documentation_content)
            messagebox.showinfo("Success", "Files saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a directory to save the files.")
    else:
        messagebox.showwarning("Warning", "No content generated yet!")

# UI Components

# Upload Button
upload_button = ttk.Button(root, text="Upload Project Files", command=upload_files)
upload_button.pack(pady=10)

# Label to display selected directory
file_label = ttk.Label(root, text="No Directory Selected")
file_label.pack(pady=5)

# Generate Button
generate_button = ttk.Button(root, text="Generate README and Documentation", command=generate_files)
generate_button.pack(pady=10)

# Loading Progress Bar (Hidden by default)
progress = ttk.Progressbar(root, mode="indeterminate", length=400)
progress.pack(pady=10)
progress.pack_forget()  # Hide the progress bar initially

# Text area for previewing the content
preview_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Consolas", 10))
preview_text.pack(pady=20)

# Save Button
save_button = ttk.Button(root, text="Save Generated Files", command=save_files)
save_button.pack(pady=10)

# Run the main event loop
root.mainloop()
