import customtkinter as ctk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

# Initialize CustomTkinter
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create the main window
root = ctk.CTk()
root.title("WiFi QR Code Generator")
root.geometry("400x500")

# WiFi Name (SSID) Label and Entry
ssid_label = ctk.CTkLabel(root, text="WiFi Name (SSID):")
ssid_label.pack(pady=5)
ssid_entry = ctk.CTkEntry(root)
ssid_entry.pack(pady=5)

# WiFi Password Label and Entry
password_label = ctk.CTkLabel(root, text="WiFi Password:")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(root, show='*')
password_entry.pack(pady=5)

# Encryption Type Label and Entry (default is WPA)
encryption_label = ctk.CTkLabel(root, text="Encryption Type (WPA/WEP):")
encryption_label.pack(pady=5)
encryption_entry = ctk.CTkEntry(root)
encryption_entry.insert(0, 'WPA')  # Default encryption is WPA
encryption_entry.pack(pady=5)

# Global variable to hold the reference to the QR label
qr_label = None

# Function to generate the QR code for WiFi
def generate_qr():
    global qr_label

    # Get user input
    ssid = ssid_entry.get()
    password = password_entry.get()
    encryption = encryption_entry.get().upper()

    if not ssid or not encryption:
        messagebox.showwarning("Input Error", "SSID and Encryption type are required")
        return

    # Generate the Wi-Fi QR Code format
    qr_data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"

    # Ask user where to save the QR code
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code as")
    if not file_path:
        return  # If the user cancels the save dialog, do nothing

    try:
        # Generate and save the QR code
        img = qrcode.make(qr_data)
        img.save(file_path)
        display_qr_code(file_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display the QR code
def display_qr_code(file_path):
    global qr_label

    # Remove the old QR code image if it exists
    if qr_label:
        qr_label.pack_forget()
    
    # Open and resize the new QR code image
    img = Image.open(file_path)
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    
    # Display the new QR code image
    qr_label = ctk.CTkLabel(root, image=img)
    qr_label.image = img  # Keep a reference to avoid garbage collection
    qr_label.pack(pady=10)

    messagebox.showinfo("Success", "QR Code generated and saved successfully!")

# Button to generate the QR code
generate_button = ctk.CTkButton(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()