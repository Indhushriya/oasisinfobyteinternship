from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import csv
import os
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# Set a modern font and color scheme
FONT = ('Arial', 12, 'bold')
BG_COLOR = "#fafbfc"  # Light gray background color
FG_COLOR = "#0a0a0a"  # Dark gray text color
BUTTON_COLOR = "#8ea9dc"  # Green color for buttons

window = tk.Tk()
window.title('Body Mass Index Explorer')
window.configure(bg=BG_COLOR)

current_directory = os.path.dirname(__file__)

today = date.today()

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=40)
    window.rowconfigure(i, weight=1, minsize=50)

# Get the current directory where bmi_advanced.py is located
csv_path = os.path.join(current_directory, 'bmi_data.csv')

if not os.path.exists(csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['weight', 'height', 'bmi', 'date', 'age', 'gender'])

def visualize_data():
    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row

        dates = []
        bmi_values = []

        for row in reader:
            try:
                bmi_values.append(float(row[2]))  # Index 2 corresponds to the BMI value
                dates.append(row[3])  # Index 3 corresponds to the date
            except ValueError:
                # Skip rows with invalid BMI values
                continue

    visualize_window = tk.Toplevel(window)
    visualize_window.title(f'BMI Explorer')

    fig, ax = plt.subplots()
    ax.plot(dates, bmi_values, marker='o', linestyle='-')
    ax.set_xlabel('Date')
    ax.set_ylabel('BMI')
    ax.set_title(f'BMI History')

    canvas = FigureCanvasTkAgg(fig, master=visualize_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Add navigation toolbar for zooming and panning
    toolbar = NavigationToolbar2Tk(canvas, visualize_window)
    toolbar.update()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def on_close():
        visualize_window.destroy()

    visualize_window.protocol("WM_DELETE_WINDOW", on_close)

def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()
    age = age_entry.get()
    gender = gender_var.get()

    if not weight or not height or not age or not gender:
        tk.messagebox.showinfo('Error', 'Please enter weight, height, age, and select gender.')
        return

    weight = float(weight)
    height = float(height)
    age = int(age)
    bmi = weight / (height ** 2)
    d1 = today.strftime("%d/%m/%Y")

    # Determine the category
    if bmi < 18.5:
        category = "Underweight"
        suggestions = [
            "Ensure you're consuming a well-balanced diet rich in nutrients to support healthy weight gain.",
            "Incorporate strength training exercises to build muscle mass and improve overall fitness.",
            "Consult with a healthcare professional or nutritionist for personalized guidance on weight gain strategies."
        ]
    elif bmi < 25:
        category = "Healthy Weight"
        suggestions = [
            "Continue to eat a balanced diet and staying physically active.",
            "Stay physically active.",
            "Maintain your well-balanced state."
        ]
    elif bmi < 30:
        category = "Overweight"
        suggestions = [
            "Focus on adopting a sustainable, balanced diet with controlled portions to promote gradual weight loss.",
            "Increase physical activity, incorporating both cardiovascular exercises and strength training.",
            "Consult with a healthcare professional or a registered dietitian for personalized weight loss advice and support."
        ]
    else:
        category = "Obese"
        suggestions = [
            "Seek professional guidance for a comprehensive weight loss plan tailored to your health needs.",
            "Emphasize a nutrient-rich, calorie-controlled diet along with regular exercise.",
            "Engage in consistent and sustainable lifestyle changes, and consider support groups for motivation and accountability."
        ]
    # Append data to CSV file
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([weight, height, bmi, d1, age, gender])
    
    # Create a new Toplevel window for displaying the result and suggestions
    result_window = tk.Toplevel(window)
    result_window.title('BMI Result and Suggestions')
    result_window.geometry("550x250")  # Set the window size

    # Larger font size
    large_font = ('Arial', 14)
    tip_font = ('Arial', 11)
    # Display the result
    result_label = tk.Label(result_window, text=f'\nBMI: {bmi:.2f}', font=large_font)
    result_label.pack()

    # Display category
    category_label = tk.Label(result_window, text=f'Category: {category}', font=large_font)
    category_label.pack()

    # Add suggestions using a Text widget for better alignment
    suggestions_text = tk.Text(result_window, wrap=tk.WORD, height=8, width=50, font=large_font)
    suggestions_text.pack(expand=True, fill='both')  # Adjust the pack options

    for suggestion in suggestions:
        suggestions_text.insert(tk.END, f'- {suggestion}\n')


def clear_text():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set(None)

def history():
    new_window = tk.Toplevel(window)
    new_window.title('BMI History')
    new_window.configure(bg=BG_COLOR)

    history_heading_label = tk.Label(new_window, text='BMI History', font=('Arial', 18), bg=BG_COLOR, fg=FG_COLOR)
    history_heading_label.grid(column=0, row=0, sticky='w')

    history_tree = ttk.Treeview(new_window, columns=('Weight', 'Height', 'BMI', 'Date', 'Age', 'Gender'), show='headings', height=10)
    history_tree.grid(column=0, row=1, sticky='nsew')

    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_rowconfigure(1, weight=1)

    history_tree.heading('Weight', text='Weight')
    history_tree.heading('Height', text='Height')
    history_tree.heading('BMI', text='BMI')
    history_tree.heading('Date', text='Date')
    history_tree.heading('Age', text='Age')
    history_tree.heading('Gender', text='Gender')

    for tag in ('evenrow', 'oddrow'):
        history_tree.tag_configure(tag, background=BG_COLOR, foreground=FG_COLOR)

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            history_tree.insert('', 'end', values=row, tags=tags)

# Create a StringVar for gender selection
gender_var = tk.StringVar()

heading_label = tk.Label(window, text='🏃 BMI Calculator 🏃', font=('Arial', 18), bg=BG_COLOR, fg=FG_COLOR)
heading_label.grid(column=0, row=0, columnspan=3, pady=(10, 20))

weight_label = tk.Label(window, text='Weight (kg):', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
weight_label.grid(column=0, row=1, sticky='W', padx=20)

weight_entry = tk.Entry(window, width=20, font=FONT)
weight_entry.grid(column=1, row=1)

height_label = tk.Label(window, text='Height (m):', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
height_label.grid(column=0, row=2, sticky='W', padx=20)

height_entry = tk.Entry(window, width=20, font=FONT)
height_entry.grid(column=1, row=2)

age_label = tk.Label(window, text='Age:', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
age_label.grid(column=0, row=3, sticky='W', padx=20)

age_entry = tk.Entry(window, width=20, font=FONT)
age_entry.grid(column=1, row=3)

gender_label = tk.Label(window, text='Gender:', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
gender_label.grid(column=0, row=4, sticky='W', padx=20)

male_radio = tk.Radiobutton(window, text='Male', variable=gender_var, value='Male', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
male_radio.grid(column=1, row=4, sticky='W', padx=20)

female_radio = tk.Radiobutton(window, text='Female', variable=gender_var, value='Female', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
female_radio.grid(column=1, row=4, sticky='E', padx=20)

calculate_button = tk.Button(window, text='Evaluate BMI', command=calculate_bmi, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#0a0a0a')
calculate_button.grid(column=1, row=6)



history_button = tk.Button(window, text='View History', command=history, width=10, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#0a0a0a')
history_button.grid(column=0, row=6)

visualize_button = tk.Button(window, text='Visualize Data', command=visualize_data, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#0a0a0a')
visualize_button.grid(column=2, row=6, pady=(10, 5))



window.mainloop()
