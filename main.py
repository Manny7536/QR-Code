import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

# Function to generate and display the QR code
def generate_qr_code():
    qr_text = text_entry.get()

    if not qr_text:
        messagebox.showwarning("Input Error", "Please enter text to encode in the QR code!")
        return

    img = qrcode.make(qr_text)

    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved successfully at {file_path}")
        display_qr_code(file_path)
        text_entry.delete(0, tk.END)  # Clear the text field after generating the QR code
    else:
        messagebox.showwarning("Save Cancelled", "QR code was not saved!")

# Function to display the saved QR code in the GUI
def display_qr_code(file_path):
    img = Image.open(file_path)
    img = img.resize((200, 200))  # Resize the image to fit in the window
    img_tk = ImageTk.PhotoImage(img)
    
    qr_code_label.configure(image=img_tk, text="")  # Remove the text and display image
    qr_code_label.image = img_tk  # Keep a reference to avoid garbage collection

# Creating the main window
root = ctk.CTk()
root.title("QR Code Generator")
root.geometry("400x350")

# Label for the text input
label = ctk.CTkLabel(root, text="Enter text to encode in the QR code:")
label.pack(pady=10)

# Text entry field
text_entry = ctk.CTkEntry(root, width=300)
text_entry.pack(pady=5)

# Button to generate the QR code
generate_button = ctk.CTkButton(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=20)

# Label to display the QR code image
qr_code_label = ctk.CTkLabel(root, text="QR code will be displayed here after generation")
qr_code_label.pack(pady=20)

# Run the application
root.mainloop()
