import tkinter as tk  # Import tkinter for GUI components
from tkinter import filedialog as fd  # Import filedialog for file selection dialogs
from PIL import Image, UnidentifiedImageError  # Import PIL for image processing

# Define color constants for the GUI
BG_COLOR = '#000000'         # Background color
FG_COLOR = '#ffffff'         # Foreground text color
ERROR_COLOR = '#ff0000'      # Color for error messages
SUCCESS_COLOR = '#00d400'    # Color for success messages
BG_BUTTON = '#00d400'        # Button background color
FG_BUTTON = '#000000'        # Button foreground color
BG_LABEL = '#ffffff'         # Label background color
FG_LABEL = '#000000'         # Label foreground color

# Define window dimensions
WIDTH = 480
HEIGHT = 450

# Define a class to store the selected image file
class ImageFile():
    def __init__(self, filename=None):
        self.filename = filename  # Initialize the filename attribute

# Function to handle the file selection process
def browsefile(image_file, label_obj_file, label_obj_status):
    label_obj_file.configure(text='')  # Clear the file label
    label_obj_status.configure(text='')  # Clear the status label
    filename = fd.askopenfilename()  # Open a file dialog to select a file
    image_file.filename = filename  # Store the selected file path
    label_obj_file.configure(text=filename)  # Display the selected file path

# Function to build the output file name with the new extension
def build_name(image, ext):
    uri = image.filename.split('.')[0]  # Remove the original extension
    return uri + ext  # Add the new extension

# Function to convert an image to the specified format
def convert_image(filename, ext, label_obj):
    try:
        image = Image.open(filename)  # Try to open the image file
    except UnidentifiedImageError:
        log_error('Not an Image File', label_obj)  # Handle non-image files
    except AttributeError:
        log_error('Please select an Image First', label_obj)  # Handle no file selected
    except PermissionError:
        log_error('No Read permission on this File', label_obj)  # Handle permission issues
    else:
        filename = build_name(image, ext)  # Build the output file name
        im = image.convert(mode='RGB')  # Convert the image to RGB mode
        im.save(filename)  # Save the converted image
        log_success(filename, label_obj)  # Log success message

# Function to display a success message
def log_success(filename, label_obj):
    msg = f'Success: Saved to: {filename}'  # Success message
    label_status.configure(text=msg, fg=SUCCESS_COLOR)  # Update the status label

# Function to display an error message
def log_error(errormsg, label_obj):
    errormsg = f'Error: {errormsg}'  # Error message
    label_obj.configure(text=errormsg, fg=ERROR_COLOR)  # Update the status label

# Conversion functions for each supported format
def to_png(filename, label_obj):
    convert_image(filename, '.png', label_obj)

def to_jpg(filename, label_obj):
    convert_image(filename, '.jpg', label_obj)

def to_bmp(filename, label_obj):
    convert_image(filename, '.bmp', label_obj)

def to_pdf(filename, label_obj):
    convert_image(filename, '.pdf', label_obj)

# Create an instance of the ImageFile class
img_file = ImageFile()

# Initialize the main application window
root = tk.Tk()
root.minsize(width=WIDTH, height=HEIGHT)  # Set minimum window size
root.resizable(width=1, height=0)  # Allow horizontal resizing only
root.title('Image Converter')  # Set the window title

# Create a canvas for background coloring
canvas = tk.Canvas(root, bg=BG_COLOR)
canvas.place(relheight=1, relwidth=1)  # Cover the entire window

# Frame for the file selection button and label
frame1 = tk.Frame(root, bg=BG_COLOR)
frame1.place(relx=0.05, rely=0.05, relheight=0.1, relwidth=0.9)

# Button to open the file selection dialog
button_open = tk.Button(frame1, text='Open File', padx=10, pady=5, font=('bold', 12), bg=BG_BUTTON, fg=FG_BUTTON, command=lambda: browsefile(img_file, label_file, label_status))
button_open.pack(side='left')

# Label prompting the user to select a file
label_select = tk.Label(frame1, fg=BG_BUTTON, bg=BG_COLOR, text='Select an Image File', font=('bold', 12))
label_select.pack(side='left', padx=10)

# Frame for displaying the selected file name
frame2 = tk.Frame(root, bg=BG_LABEL)
frame2.place(relx=0.05, rely=0.16, relheight=0.06, relwidth=0.9)

label_file = tk.Label(frame2, fg=FG_LABEL, bg=BG_LABEL, font=('bold', 9))
label_file.place(relheight=1)

# Frame for conversion buttons
frame3 = tk.Frame(root, bg=BG_COLOR)
frame3.place(relx=0.05, rely=0.26, relheight=0.6, relwidth=0.9)

# Buttons for converting to various formats
button_png = tk.Button(frame3, text='Convert to PNG', fg=FG_BUTTON, bg=BG_BUTTON, command=lambda: to_png(img_file.filename, label_status))
button_png.place(relx=0.25, rely=0.05, relheight=0.15, relwidth=0.5)

button_jpg = tk.Button(frame3, text='Convert to JPEG', fg=FG_BUTTON, bg=BG_BUTTON, command=lambda: to_jpg(img_file.filename, label_status))
button_jpg.place(relx=0.25, rely=0.30, relheight=0.15, relwidth=0.5)

button_bmp = tk.Button(frame3, text='Convert to BMP', fg=FG_BUTTON, bg=BG_BUTTON, command=lambda: to_bmp(img_file.filename, label_status))
button_bmp.place(relx=0.25, rely=0.55, relheight=0.15, relwidth=0.5)

button_pdf = tk.Button(frame3, text='Convert to PDF', fg=FG_BUTTON, bg=BG_BUTTON, command=lambda: to_pdf(img_file.filename, label_status))
button_pdf.place(relx=0.25, rely=0.80, relheight=0.15, relwidth=0.5)

# Frame for displaying status messages
frame4 = tk.Frame(root, bg=BG_COLOR)
frame4.place(relx=0.05, rely=0.9, relheight=0.06, relwidth=0.9)

label_status = tk.Label(frame4, bg=BG_COLOR, font=('bold', 9))
label_status.place(relheight=1)

# Start the main event loop
root.mainloop()