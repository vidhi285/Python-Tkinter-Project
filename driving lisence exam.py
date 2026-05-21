import tkinter as tk
from tkinter import ttk

def submit():
    # Get student information
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    above_18 = above_18_var.get()
    
    # Display eligibility message
    if above_18:
        eligibility_label.config(text="Congratulations! You are eligible to take the driving license exam.")
        start_quiz_button.pack()
        exam_button.pack()  # Display the button if eligible
    else:
        eligibility_label.config(text="You must be above 18 to take the driving license exam.")
        exam_button.pack_forget()  # Hide the button if not eligible

def start_quiz():
    # Close main window
    root.withdraw()
    
    # Open quiz window
    quiz_window = tk.Toplevel()
    quiz_window.title("Driving License Quiz")

    # Create frame with scrollbar for quiz questions
    quiz_frame = ttk.Frame(quiz_window)
    quiz_frame.pack(fill='both', expand=True)

    # Create canvas for quiz questions
    canvas = tk.Canvas(quiz_frame)
    canvas.pack(side='left', fill='both', expand=True)

    # Add scrollbar to canvas
    scrollbar = ttk.Scrollbar(quiz_frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')
    canvas.config(yscrollcommand=scrollbar.set)

    # Create frame to contain quiz content
    quiz_content = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=quiz_content, anchor='nw')
    

    # Quiz questions and options
    questions = [
        "1. What does a yellow traffic light mean?",
        "2. What does a white diamond-shaped sign with an orange background indicate?",
        "3. When parking on a hill, which way should you turn your front wheels?",
        "4. Which of the following is a legal parking position?",
        "5. What should you do when approaching a flashing red traffic signal?",
        "6. What is the maximum speed limit in a school zone in your state?",
        "7. What does a red octagonal sign indicate?",
        "8. When should you use your headlights?",
        "9. What should you do if you are involved in a minor accident?",
        "10. What is the purpose of a yield sign?"
    ]
    
    options = [
        ["A. Stop", "B. Slow down", "C. Proceed with caution"],
        ["A. Construction zone", "B. Yield sign", "C. School zone"],
        ["A. Away from the curb (uphill)", "B. Toward the curb (downhill)", "C. Parallel to the curb"],
        ["A. Parking next to a fire hydrant", "B. Parking within 15 feet of a fire station driveway", "C. Parking facing the wrong way on a street"],
        ["A. Stop and yield to pedestrians", "B. Slow down and proceed with caution", "C. Treat it as a stop sign"],
        ["A. 20 mph", "B. 25 mph", "C. 30 mph"],
        ["A. Yield", "B. Stop", "C. Do not enter"],
        ["A. During daylight hours", "B. Only when it's raining", "C. During dawn and dusk"],
        ["A. Exchange insurance information", "B. Apologize and leave", "C. Report it to the police"],
        ["A. To indicate a merge point", "B. To alert drivers to slow down", "C. To yield to other traffic"]
    ]

    # Create labels for questions and options
    question_labels = []
    answer_vars = []
    for idx, (question, options_list) in enumerate(zip(questions, options)):
        label = ttk.Label(quiz_content, text=question)
        label.grid(row=idx*4, column=0, padx=10, pady=5, sticky="w")
        question_labels.append(label)
        
        answer_var = tk.StringVar()
        answer_vars.append(answer_var)
        
        for i, option in enumerate(options_list):
            if idx in [0, 1, 4, 6, 9]:  # For questions with radio buttons
                radio = ttk.Radiobutton(quiz_content, text=option, variable=answer_var, value=option)
                radio.grid(row=idx*4 + i + 1, column=0, padx=10, pady=2, sticky="w")
            else:  # For other questions with checkboxes
                check = ttk.Checkbutton(quiz_content, text=option, variable=answer_var, onvalue=option)
                check.grid(row=idx*4 + i + 1, column=0, padx=10, pady=2, sticky="w")


    # Add a submit button after displaying the quiz
    submit_quiz_button = tk.Button(quiz_window, text="Submit Quiz", command=submit_quiz)
    submit_quiz_button.pack()

    
    # Update scroll region
    quiz_content.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def submit_quiz():
    # Initialize a variable to count correct answers
    correct_answers = 0
    
    # Placeholder for checking answers
    # For demonstration purposes, let's assume the user answered all questions correctly
    answers = [answer_var.get() for answer_var in answer_vars]
    for answer in answers:
        # Check if the answer is correct (you need to implement this logic)
        # For demonstration purposes, let's assume all answers are correct
        if answer:
            correct_answers += 1
    
    # Display results based on the number of correct answers
    if correct_answers >= 5:
        result_label.config(text="Congratulations! You passed the quiz.")
    else:
        result_label.config(text="Sorry, you did not pass the quiz. Please try again.")

    
    # Add a submit button after displaying the quiz
    submit_quiz_button = tk.Button(quiz_window, text="Submit Quiz", command=submit_quiz)
    submit_quiz_button.pack()



# Create main window
root = tk.Tk()
root.title("Student Information")

# Create labels and entries
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

gender_var = tk.StringVar()
gender_var.set("Male")

male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=2, column=1, padx=10, pady=5, sticky="w")

female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=2, column=1, padx=70, pady=5, sticky="w")

# Checkbox for above 18
above_18_var = tk.BooleanVar()
above_18_checkbox = tk.Checkbutton(root, text="I am above 18", variable=above_18_var)
above_18_checkbox.grid(row=3, column=0, columnspan=2, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label for eligibility message
eligibility_label = tk.Label(root, text="")
eligibility_label.grid(row=5, column=0, columnspan=2, pady=5)

# Button to start quiz
start_quiz_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_quiz_button.pack_forget()  # Initially hide the button

# Button to open another window for the exam
exam_button = tk.Button(root, text="Take Exam", command=start_quiz)
exam_button.grid(row=6, column=0, columnspan=2, pady=10)
exam_button.pack_forget()  # Initially hide the button

# Label for quiz results
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
