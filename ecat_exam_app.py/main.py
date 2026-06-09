import time

# ─────────────────────────────────────────────
#  CONSTANTS
# ────────────────────────────────────────────
CORRECT_MARKS = 4
WRONG_MARKS = -1
SKIP_MARKS = 0
MIN_QUESTIONS = 10
MAX_LOGIN_ATTEMPTS = 3
#Amin credentials
ADMIN_USERNAME = "ecat_admin"
ADMIN_PASSWORD = "ecat@2024"
#Student credentials (shared for all students in this basic version)
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "student123"
#Questions(Physics,Mathematics,Computer,English)
questions = [
    {
     "id":1,
     "subject" : "Physics" ,
     "question"  : "One light year is equal to?",
     "choices": {"A":"9 x 10^12m", "B": "6 x 10^12",  "C": "9.5 x 10^13m" , "D": "None"},
     "answer" : "C"
    },
    {
     "id":2,
     "subject" : "Physics",
     "question": "least distance of distinct vision for human eye is?",
     "choices" : {"A" : "50cm","B" : "25cm", "C": "30cm", "D" : "20cm"},
     "answer" : "B"
    },
    {
        "id":3,
        "subject" : "Mathematics",
        "question" : "What is the derivative of 2x?",
        "choices" : {"A": "2x", "B":"2", "C":"x", "D": "x^2"},
        "answer" : "B"
    },
    {
        "id":4,
        "subject" : "Mathematics",
        "question" : "What is the value of log(1)?",
        "choices" : {"A": "1", "B":"undefined", "C":"0", "D": "infinity"},
        "answer" : "C"
    },
    {
        "id":5,
        "subject" : "Mathematics",
        "question" : "A die is rolled once.the probability of getting an even number is:",
        "choices" : {"A": "1/6", "B":"1/3", "C":"1/2", "D": "2/3"},
        "answer" : "C"
    },
    {
        "id":6,
        "subject": "Computer",
        "question": "Which number system is used only 0 and 1?",
        "choices": {"A": "Decimal", "B": "Binary", "C": "Octal", "D": "Hexadecimal"},
        "answer": "B"
    },
    {
        "id":7,
        "subject": "Computer",
        "question": "Which memory is temporary?",
        "choices": {"A": "ROM", "B": "Hard disk", "C": "SSD", "D": "RAM"},
        "answer": "D"
    },
    {
        "id":8,
        "subject": "Computer",
        "question": "Which of the following is system software?",
        "choices": {"A": "MS Word", "B": "Photoshop", "C": "Windows", "D": "Chrome"},
        "answer": "C"
    },
    {
        "id":9,
        "subject": "English",
        "question": "Choose the correct synonym of 'Abundant':",
        "choices": {"A": "Scarce", "B": "Plenty", "C": "Rare", "D": "Empty"},
        "answer": "B"
    },
    {
        "id":10,
        "subject": "English",
        "question": "Choose the correct antonym of 'Ancient':",
        "choices": {"A": "Old", "B": "Historic", "C": "Modern", "D": "Traditional"},
        "answer": "C"
    }
]

all_results = []   # Every student result is stored here

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line():
    print("-" * 55)

def print_double_line():
    print("=" * 55)

def pause():
    time.sleep(1)

def get_grade(percentage):
    if percentage >= 80:
        return "EXCELLENT"
    elif percentage >= 65:
        return "GOOD"
    elif percentage >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"

def calculate_score(answers_dict):
    correct = 0
    wrong   = 0
    skipped = 0

    for idx in range(len(questions)):
        chosen = answers_dict.get(idx, "S")   # default = skipped
        if chosen == "S":
            skipped += 1
        elif chosen == questions[idx]["answer"]:
            correct += 1
        else:
            wrong += 1

    score = (correct * CORRECT_MARKS) + (wrong * WRONG_MARKS)
    max_score = len(questions) * CORRECT_MARKS
    percentage = round((score / max_score) * 100, 2)
    grade = get_grade(percentage)

    return score, max_score, percentage, grade, correct, wrong, skipped
# ─────────────────────────────────────────────
#  ADMIN PORTAL FUNCTIONS
# ─────────────────────────────────────────────

def admin_login():
    print_double_line()
    print("        ADMIN PORTAL — ECAT TEAM")
    print_double_line()

    attempts = 0
    while attempts < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\n✓ Login successful! Welcome, ECAT Admin.")
            pause()
            return True
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"✗ Wrong credentials. {remaining} attempt(s) left.\n")
            else:
                print("✗ Account locked. Too many failed attempts.")

    return False
def view_all_questions():
    print_double_line()
    print("          ALL QUESTIONS IN BANK")
    print_double_line()

    if len(questions) == 0:
        print("No questions available.")
        return

    for i in range(len(questions)):
        q = questions[i]
        print(f"\nQ{i + 1}. [{q['subject']}] {q['question']}")
        print(f"   A) {q['choices']['A']}")
        print(f"   B) {q['choices']['B']}")
        print(f"   C) {q['choices']['C']}")
        print(f"   D) {q['choices']['D']}")
        print(f"   ✓ Correct Answer: {q['answer']}")
        print_line()

    input("\nPress Enter to go back...")

def add_new_question():
    print_double_line()
    print("           ADD NEW QUESTION")
    print_double_line()

    subject  = input("Enter subject (e.g. Physics): ").strip()
    question = input("Enter question text        : ").strip()
    choice_a = input("Choice A                   : ").strip()
    choice_b = input("Choice B                   : ").strip()
    choice_c = input("Choice C                   : ").strip()
    choice_d = input("Choice D                   : ").strip()

    correct = ""
    while correct not in ["A", "B", "C", "D"]:
        correct = input("Correct answer (A/B/C/D)   : ").strip().upper()
        if correct not in ["A", "B", "C", "D"]:
            print("Please enter A, B, C, or D only.")

    new_id = questions[-1]["id"] + 1 if questions else 1

    new_question = {
        "id":      new_id,
        "subject": subject,
        "question": question,
        "choices": {"A": choice_a, "B": choice_b, "C": choice_c, "D": choice_d},
        "answer":  correct
    }

    questions.append(new_question)
    print(f"\n✓ Question added successfully! Total questions: {len(questions)}")
    input("Press Enter to go back...")

def delete_question():
    print_double_line()
    print("          DELETE A QUESTION")
    print_double_line()

    if len(questions) == 0:
        print("No questions to delete.")
        input("Press Enter to go back...")
        return

    for i in range(len(questions)):
        print(f"{i + 1}. {questions[i]['question']}")

    print_line()
    choice = input("Enter question number to delete (or 'cancel'): ").strip().lower()
    if choice == "cancel":
        return
    if choice.isdigit():
        number = int(choice)
        if 1 <= number <= len(questions):
            removed = questions.pop(number - 1)
            print(f"\n✓ Deleted: {removed['question']}")
        else:
            print("✗ Invalid number.")
    else:
        print("✗ Please enter a valid number.")

    input("Press Enter to go back...")

def question_bank_statistics():
    print_double_line()
    print("        QUESTION BANK STATISTICS")
    print_double_line()

    print(f"Total Questions: {len(questions)}\n")

    # Count by subject
    subject_count = {}
    for q in questions:
        subj = q["subject"]
        if subj in subject_count:
            subject_count[subj] += 1
        else:
            subject_count[subj] = 1
    print("Breakdown by Subject:")
    print_line()
    for subj in subject_count:
        print(f"  {subj:<15} : {subject_count[subj]} question(s)")

    input("\nPress Enter to go back...")

def view_all_results():
    print_double_line()
    print("         ALL STUDENT RESULTS")
    print_double_line()

    if len(all_results) == 0:
        print("No student has attempted the exam yet.")
        input("Press Enter to go back...")
        return

    print(f"{'#':<4} {'Name':<18} {'Roll':<12} {'Score':<8} {'%':<8} {'Grade':<14} {'Time'}")
    print_line()

    for i in range(len(all_results)):
        r = all_results[i]
        print(f"{i + 1:<4} {r['name']:<18} {r['roll']:<12} {r['score']:<8} {r['percentage']:<8} {r['grade']:<14} {r['time']}")

    input("\nPress Enter to go back...")

def view_detailed_result():
    print_double_line()
    print("       VIEW DETAILED STUDENT RESULT")
    print_double_line()

    if len(all_results) == 0:
        print("No results available yet.")
        input("Press Enter to go back...")
        return

    for i in range(len(all_results)):
        print(f"{i + 1}. {all_results[i]['name']} — Roll: {all_results[i]['roll']}")

    print_line()
    choice = input("Enter result number to view (or 'cancel'): ").strip().lower()

    if choice == "cancel":
        return

    if choice.isdigit():
        number = int(choice)
        if 1 <= number <= len(all_results):
            r = all_results[number - 1]
            print_double_line()
            print(f"  Student : {r['name']}")
            print(f"  Roll No : {r['roll']}")
            print(f"  Score   : {r['score']} / {r['max_score']}")
            print(f"  Percent : {r['percentage']}%")
            print(f"  Grade   : {r['grade']}")
            print(f"  Time    : {r['time']}")
            print_double_line()

            # Per-question breakdown
            saved_answers = r["answers"]
            for idx in range(len(questions)):
                q      = questions[idx]
                chosen = saved_answers.get(idx, "S")
                correct_ans = q["answer"]

                if chosen == "S":
                    status = "SKIPPED"
                elif chosen == correct_ans:
                    status = "CORRECT ✓"
                else:
                    status = f"WRONG ✗  (Correct: {correct_ans})"

                print(f"\nQ{idx + 1}. {q['question']}")
                print(f"   Your Answer : {chosen}   →  {status}")
        else:
            print("✗ Invalid number.")
    else:
        print("✗ Please enter a valid number.")

    input("\nPress Enter to go back...")

def class_result_statistics():
    print_double_line()
    print("        CLASS RESULT STATISTICS")
    print_double_line()

    if len(all_results) == 0:
        print("No results available yet.")
        input("Press Enter to go back...")
        return

    scores = []
    pass_count = 0
    fail_count = 0
    grade_count = {"EXCELLENT": 0, "GOOD": 0, "AVERAGE": 0, "BELOW AVERAGE": 0}

    for r in all_results:
        scores.append(r["score"])
        if r["percentage"] >= 50:
            pass_count += 1
        else:
            fail_count += 1

        grade = r["grade"]
        if grade in grade_count:
            grade_count[grade] += 1

    highest = max(scores)
    lowest  = min(scores)
    average = round(sum(scores) / len(scores), 2)

    print(f"  Total Attempts  : {len(all_results)}")
    print(f"  Highest Score   : {highest}")
    print(f"  Lowest Score    : {lowest}")
    print(f"  Average Score   : {average}")
    print(f"  Passed          : {pass_count}")
    print(f"  Failed          : {fail_count}")
    print_line()
    print("  Grade Distribution:")
    for g in grade_count:
        print(f"    {g:<16} : {grade_count[g]}")

    input("\nPress Enter to go back...")

def admin_menu():
    while True:
        print_double_line()
        print("           ADMIN PORTAL MENU")
        print_double_line()
        print("  1. View All Questions")
        print("  2. Add New Question")
        print("  3. Delete a Question")
        print("  4. Question Bank Statistics")
        print("  5. View All Student Results")
        print("  6. View Detailed Result (Per Student)")
        print("  7. Class Result Statistics")
        print("  8. Logout")
        print_double_line()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            view_all_questions()
        elif choice == "2":
            add_new_question()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            question_bank_statistics()
        elif choice == "5":
            view_all_results()
        elif choice == "6":
            view_detailed_result()
        elif choice == "7":
            class_result_statistics()
        elif choice == "8":
            print("\n✓ Logged out from Admin Portal.")
            break
        else:
            print("✗ Invalid choice. Please enter 1 to 8.")
# ─────────────────────────────────────────────
#  STUDENT PORTAL FUNCTIONS
# ─────────────────────────────────────────────

def student_login():
    print_double_line()
    print("         STUDENT PORTAL — LOGIN")
    print_double_line()

    attempts = 0
    while attempts < 3:
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        if username == STUDENT_USERNAME and password == STUDENT_PASSWORD:
            print("\n✓ Login successful!")
            full_name = input("Enter your Full Name : ").strip()
            roll_no   = input("Enter your Roll No   : ").strip()
            pause()
            return True, full_name, roll_no
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"✗ Wrong credentials. {remaining} attempt(s) left.\n")
            else:
                print("✗ Account locked. Too many failed attempts.")

    return False, "", ""


def show_exam_rules():
    print_double_line()
    print("              EXAM RULES")
    print_double_line()
    print("  • Total Questions  : ", len(questions))
    print("  • Correct Answer   : +4 marks")
    print("  • Wrong Answer     : -1 mark")
    print("  • Skipped Question :  0 marks")
    print_line()
    print("  HOW TO ANSWER:")
    print("  • Type A, B, C, or D  → to answer the question")
    print("  • Type S              → to skip the question")
    print("  • Type SUBMIT         → to end the exam early")
    print_double_line()
    input("Press Enter to go back...")


def start_exam(full_name, roll_no):
    print_double_line()
    print("              EXAM STARTING")
    print_double_line()
    print(f"  Student : {full_name}")
    print(f"  Roll No : {roll_no}")
    print(f"  Total Q : {len(questions)}")
    print_line()
    input("Press Enter when you are ready...")

    answers = {}   # { question_index: 'A'/'B'/'C'/'D'/'S' }

    for idx in range(len(questions)):
        q = questions[idx]
        print_double_line()
        print(f"Question {idx + 1} of {len(questions)}  [{q['subject']}]")
        print_double_line()
        print(f"{q['question']}\n")
        print(f"  A)  {q['choices']['A']}")
        print(f"  B)  {q['choices']['B']}")
        print(f"  C)  {q['choices']['C']}")
        print(f"  D)  {q['choices']['D']}")
        print_line()
        print("  Type A/B/C/D to answer | S to skip | SUBMIT to finish early")

        # Keep asking until valid input
        while True:
            user_input = input("Your answer: ").strip().upper()

            if user_input == "SUBMIT":
                # Mark remaining as skipped and stop
                for remaining_idx in range(idx, len(questions)):
                    answers[remaining_idx] = "S"
                print("\n✓ Exam submitted early!")
                # jump out of both loops
                idx = len(questions)
                break

            elif user_input in ["A", "B", "C", "D"]:
                answers[idx] = user_input
                break

            elif user_input == "S":
                answers[idx] = "S"
                break

            else:
                print("✗ Invalid input. Type A, B, C, D, S, or SUBMIT.")

        # If SUBMIT was pressed, stop the exam loop too
        if len(answers) == len(questions):
            break

    # Fill any unanswered questions as skipped (safety)
    for i in range(len(questions)):
        if i not in answers:
            answers[i] = "S"

    # ── Calculate result ──
    score, max_score, percentage, grade, correct, wrong, skipped = calculate_score(answers)
    exam_time = time.strftime("%d-%b-%Y  %I:%M %p")

    # Save result
    result_record = {
        "name":       full_name,
        "roll":       roll_no,
        "score":      score,
        "max_score":  max_score,
        "percentage": percentage,
        "grade":      grade,
        "time":       exam_time,
        "answers":    answers
    }
    all_results.append(result_record)

    # ── Show result ──
    print_double_line()
    print("             YOUR RESULT")
    print_double_line()
    print(f"  Name         : {full_name}")
    print(f"  Roll No      : {roll_no}")
    print(f"  Score        : {score} / {max_score}")
    print(f"  Percentage   : {percentage}%")
    print(f"  Grade        : {grade}")
    print(f"  Correct      : {correct}")
    print(f"  Wrong        : {wrong}")
    print(f"  Skipped      : {skipped}")
    print(f"  Date & Time  : {exam_time}")
    print_double_line()

    # ── Per-question review ──
    view_review = input("\nWould you like to see answer review? (yes/no): ").strip().lower()
    if view_review == "yes":
        print_double_line()
        print("          ANSWER REVIEW")
        print_double_line()

        for idx in range(len(questions)):
            q           = questions[idx]
            chosen      = answers.get(idx, "S")
            correct_ans = q["answer"]

            if chosen == "S":
                status = "SKIPPED"
            elif chosen == correct_ans:
                status = "CORRECT ✓"
            else:
                status = f"WRONG ✗  (Correct: {correct_ans})"

            print(f"\nQ{idx + 1}. {q['question']}")
            print(f"   Your Answer : {chosen}   →  {status}")

    input("\nPress Enter to go back to Student Menu...")


def student_menu(full_name, roll_no):
    while True:
        print_double_line()
        print("          STUDENT PORTAL MENU")
        print_double_line()
        print(f"  Welcome, {full_name}!")
        print_line()
        print("  1. Start Exam")
        print("  2. View Exam Rules")
        print("  3. Logout")
        print_double_line()

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            start_exam(full_name, roll_no)
        elif choice == "2":
            show_exam_rules()
        elif choice == "3":
            print(f"\n✓ Logged out. Good luck, {full_name}!")
            break
        else:
            print("✗ Invalid choice. Please enter 1, 2, or 3.")

# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    while True:
        print_double_line()
        print("   ECAT EXAM APPLICATION — DUAL PORTAL")
        print("      UET Lahore | CMPE-112L | CEA")
        print_double_line()
        print("  1. Admin Portal  (ECAT Team)")
        print("  2. Student Portal")
        print("  3. Exit")
        print_double_line()

        choice = input("Select portal (1/2/3): ").strip()

        if choice == "1":
            success = admin_login()
            if success:
                admin_menu()

        elif choice == "2":
            success, full_name, roll_no = student_login()
            if success:
                student_menu(full_name, roll_no)

        elif choice == "3":
            print("\n  Thank you for using ECAT Exam App. Goodbye!\n")
            break

        else:
            print("✗ Invalid choice. Please enter 1, 2, or 3.\n")


# ─────────────────────────────────────────────
#  RUN THE PROGRAM
# ─────────────────────────────────────────────
main()