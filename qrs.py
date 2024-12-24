import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get the input from the user
    input_data = entry.get()
    
    if not input_data.strip():
        messagebox.showerror("Error", "Please enter a valid URL or text.")
        return
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save QR Code"
    )
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Success", f"QR code saved at {file_path}")
    
    # Display the QR code in the GUI
    qr_image = qr_image.resize((200, 200))  # Resize for display
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo  # Keep a reference to avoid garbage collection

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="QR Code Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input entry
entry_label = tk.Label(root, text="Enter URL or Text:")
entry_label.pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# QR code display
qr_label = tk.Label(root, text="Your QR Code will appear here", font=("Helvetica", 10))
qr_label.pack(pady=10)

# Run the main event loop
root.mainloop()
