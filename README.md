# Report Card Generator
This is a Python script that generates a report card for students. It provides a graphical user interface (GUI) using the Tkinter library and generates the report card in PDF format using the fpdf library. I had made this in my high school as part of an evaluation.

## Prerequisites
Before running the script, ensure that you have the following prerequisites installed:

Python 3.x: The script is written in Python and requires Python 3.x to be installed on your system.
Tkinter: The Tkinter library is used for creating the GUI. It is usually included with Python installations by default.
fpdf: The fpdf library is used for generating the report card in PDF format. You can install it by running the following command: pip install fpdf.
## Running the Script
To run the script, follow these steps:

#### Clone the repository: Start by cloning the repository to your local machine using the following command: git clone <repository_url>.

#### Navigate to the project directory: Use the cd command to navigate to the project directory.

#### Install dependencies: If you haven't installed the required dependencies mentioned in the prerequisites section, install them using the appropriate commands.

#### Run the script: Execute the script by running the following command: python ReportCard.py.

## Using the Application
The application provides a GUI for entering personal information and marks for various subjects. After entering the necessary details, click the "Generate Report Card" button to generate the report card in PDF format.



### Personal Information
The following personal information fields are available:

#### Name: Enter the student's name.
#### Roll Number: Enter the student's roll number.
#### Class: Enter the student's class.
### Marks
The application allows entering marks for multiple subjects. The subjects are predefined and include:

#### Physics, Chemistry, Maths, Computer Science, English
For each subject, enter the marks obtained in three periodic tests.

![image](https://github.com/abid7955/Report-Card-Generator/assets/112928966/cd2c31ff-10d9-4832-ad4d-a09430439e6a)
![image](https://github.com/abid7955/Report-Card-Generator/assets/112928966/7ad23dfe-dd20-43b0-802d-cd735cd57f7c)

### Generate Report Card
Clicking the "Generate Report Card" button will generate the report card in PDF format. The generated report card will include the following information:



#### School name and logo.
#### Personal information (name, roll number, class).
#### Marks obtained in each subject for three periodic tests.
#### Total marks, obtained marks, percentage, and remarks.

![image](https://github.com/abid7955/Report-Card-Generator/assets/112928966/1791a524-238c-41b2-98d3-288f9d86f4a6)


## File Structure
#### The project includes the following files:

ReportCard.py: The main Python script that generates the report card.
sample school image.jpg: An example image file representing the school logo. Replace it with your own school logo if desired.
### Customization
Feel free to customize the script and GUI according to your requirements. You can modify the subjects, add more fields to the personal information section, change the appearance of the report card, and more.

## License
This project is licensed under the MIT License.

## Acknowledgments
The script is developed based on the functionality provided by the Tkinter and fpdf libraries. Special thanks to the developers of these libraries for their contributions.

## References
### Tkinter documentation: https://docs.python.org/3/library/tkinter.html
### fpdf documentation: https://pyfpdf.readthedocs.io/en/latest/
