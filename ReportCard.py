import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF


class ReportCardGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Report Card Generator")

        # Personal Information
        tk.Label(root, text="Personal Information", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
        tk.Label(root, text="Roll Number:").grid(row=2, column=0, sticky="e")
        tk.Label(root, text="Class:").grid(row=3, column=0, sticky="e")

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)
        self.roll_entry = tk.Entry(root)
        self.roll_entry.grid(row=2, column=1)
        self.class_entry = tk.Entry(root)
        self.class_entry.grid(row=3, column=1)

        # Marks
        tk.Label(root, text="Marks", font=("Helvetica", 16, "bold")).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Label(root, text="Subject").grid(row=5, column=0)
        for i, subject in enumerate(self.subjects):
            tk.Label(root, text=subject).grid(row=i + 6, column=0, sticky="e")

        self.marks_entries = {}

        for j in range(3):
            tk.Label(root, text="Periodic Test " + str(j + 1)).grid(row=5, column=j + 1, padx=5)
            for i, subject in enumerate(self.subjects):
                entry = tk.Entry(root)
                entry.grid(row=i + 6, column=j + 1)
                self.marks_entries[(i, j)] = entry

        # Generate Report Card Button
        tk.Button(root, text="Generate Report Card", command=self.generate_report_card).grid(row=12, column=0, columnspan=4, pady=10)

    def generate_report_card(self):
        # Get personal information
        name = self.name_entry.get()
        roll_number = self.roll_entry.get()
        class_name = self.class_entry.get()

        # Get marks for each subject
        marks = []
        for i, subject in enumerate(self.subjects):
            marks_row = []
            for j in range(3):
                entry = self.marks_entries[(i, j)]
                try:
                    marks_row.append(int(entry.get()))
                except ValueError:
                    marks_row.append(0)
            marks.append(marks_row)

        # Calculate total marks and percentage
        total_marks = 1500
        obtained_marks = 0
        for i in range(len(marks)):
            subject_total = sum(marks[i])
            obtained_marks += sum(marks[i])

        percentage = (obtained_marks / total_marks) * 100

        # Determine remarks based on the percentage
        if percentage < 40:
            remarks = "Failed"
        elif percentage < 60:
            remarks = "Needs Improvement"
        elif percentage < 80:
            remarks = "Good"
        else:
            remarks = "Excellent"

        # Generate the report card in PDF format
        pdf = FPDF()
        pdf.add_page()

        # Set the margins
        left_margin = 20
        right_margin = 20
        top_margin = 20
        bottom_margin = 20

        # Set the font
        pdf.set_font("Arial", size=12)

        # Add the school image
        pdf.image("sample school image.jpg", x=10, y=11, w=17)

        # Add the title
        pdf.cell(0, 10, txt="Don Bosco School, Alaknanda", ln=True, align="C")
        pdf.cell(0, 8, txt="Report Card", ln=True, align="C")

        # Add personal information
        pdf.ln(3)
        pdf.cell(0, 10, txt="Name: " + name, ln=True)
        pdf.cell(0, 10, txt="Roll Number: " + roll_number, ln=True)
        pdf.cell(0, 10, txt="Class: " + class_name, ln=True)
        pdf.ln(5)
        
        pdf.cell(0, 10, txt="Academic Progress, 2022-23", ln=True, align="C")
        pdf.ln(5)
        
        # Add marks table
        col_width = 40
        row_height = 10
        table_width = col_width * 4
        table_height = row_height * (len(marks) + 1)

        # Add table header
        pdf.set_fill_color(200, 200, 200)
        pdf.cell(col_width, row_height, "Subject", border=1, fill=True, align="C")
        for j in range(3):
            pdf.cell(col_width, row_height, "Periodic Test " + str(j + 1), border=1, fill=True, align="C")
        pdf.ln(row_height)

        # Add table rows
        for i in range(len(marks)):
            pdf.set_fill_color(255, 255, 255)  # Reset fill color to white
            pdf.cell(col_width, row_height, self.subjects[i], border=1, fill=True, align="C")
            for j in range(3):
                pdf.cell(col_width, row_height, str(marks[i][j]), border=1, align="C")
            pdf.ln(row_height)
        
        pdf.ln(5)
        # Add total marks, obtained marks, percentage, and remarks
        pdf.set_fill_color(200, 200, 200)
        pdf.cell(col_width, row_height, "Total Marks", border=1, fill=True, align="C")
        pdf.cell(col_width, row_height, str(total_marks), border=1, align="C")
        pdf.ln(row_height)
        pdf.cell(col_width, row_height, "Obtained Marks", border=1, fill=True, align="C")
        pdf.cell(col_width, row_height, str(obtained_marks), border=1, align="C")
        pdf.ln(row_height)
        pdf.cell(col_width, row_height, "Percentage", border=1, fill=True, align="C")
        pdf.cell(col_width, row_height, "{:.2f}%".format(percentage), border=1, align="C")
        pdf.ln(row_height)
        pdf.cell(col_width, row_height, "Remarks", border=1, fill=True, align="C")
        pdf.cell(col_width, row_height, remarks, border=1, align="C")
        pdf.ln(row_height)

        # Add border to the page
        page_width = pdf.w
        page_height = pdf.h
        border_width = 6
        pdf.set_line_width(border_width)
        pdf.rect(0, 0, page_width, page_height)

        # Save the PDF file
        pdf_file = "report_card.pdf"
        pdf.output(pdf_file)

        messagebox.showinfo("Report Card Generated", "Report card generated successfully!")
        self.root.destroy()


# Create the Tkinter application window
root = tk.Tk()

# Define the subjects
ReportCardGenerator.subjects = ["Physics", "Chemistry", "Maths", "Computer Science", "English"]

app = ReportCardGenerator(root)

# Run the Tkinter event loop
root.mainloop()
