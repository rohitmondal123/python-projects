# =========  N1 EXAMINATION SYSTEM  =========



students = {}
results = []

def register_student():
    name = input("enter student name : ")
    username = input("choose a username : ")
    password = input("choose a password : ")
    if username in students:
        print("student already exists in the database....")
        return
    students[username] = {"name": name, "password": password}
    print("student registration successfully ! you can log in now ....")


def student_login():
    username = input("username : ")
    password = input("password : ")
    if username in students and students[username]['password'] == password:
        name = students[username]['name']
        print(f"welcome {name}")
        student_menu(name)
    else:
        print("invalid usernmae or password ! please enter valid usernmae or password....")


def admin_login():
    usernmae = input("username : ")
    password = input("password : ")
    if usernmae == 'admin@34563' and password == 'admin':
        print("admin login successful ...")
        admin_menu()
    else:
        print("incorrect admin login....")


def get_questions():
    return [
        {
            "question": "Which language is used for AI development?",
            "options": ["A. Python", "B. C", "C. Java", "D. HTML"],
            "answer": "A"
        },
        {
            "question": "Who developed the Python language?",
            "options": ["A. Elon Musk", "B. Guido van Rossum", "C. Bill Gates", "D. Mark Zuckerberg"],
            "answer": "B"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Central Processor Unit", "D. None"],
            "answer": "B"
        },
        {
            "question": "What is the full form of RAM?",
            "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Access Memory", "D. Random Active Memory"],
            "answer": "B"
        },
        {
            "question": "HTML is used to?",
            "options": ["A. Design a webpage", "B. Create apps", "C. Compile code", "D. Manage database"],
            "answer": "A"
        }
    ]



def take_exam(student_name):
    questions = get_questions()
    score = 0
    print("====== ONLINE EXAM ======")
    for i,q in enumerate(questions,1):
        print(f"Q{i}. {q['question']}")
        for opt in q['options']:
            print(opt)
        ans = input("your answer (A/B/C/D) : ").strip().upper()
        if ans == q['answer']:
            print("correct")
            score += 1
        else:
            print("wrong ! attempt next question.....")
    total = len(questions)
    percentage = (score/total) * 100
    print(f"exam finished ! you scored {score}/{total} ({percentage:.2f}%)\n")
    results.append({
        "name": student_name,
        "score":score,
        "total":total,
        "percent":percentage
    })


def view_result():
    if not results:
        print("no result found ")
        return
    print("==== EXAM RESULT ====")
    for r in results:
        print(f"{r['name']} - {r['score']}/{r['total']} ({r['percent']:.2f}%)")
        print()

def student_menu(name):
    while True:
        print("""
===== STUDENT MENU =====
1. Take Exam
2. View result
3. Logout""")
        ch = int(input("enter choice "))
        if ch == 1:
            take_exam(name)
        elif ch == 2:
            view_result()
        elif ch == 3:
            print("Logged out successfully ")
            break
        else:
            print("invalid choice please try again...")

def admin_menu():
    while True:
        print("===== ADMIN MENU =====")
        print("1. view all students ")
        print("2. view all result")
        print("3. logout")
        ch = int(input("enter your choice : "))
        if ch == 1:
            if not students:
                print("no students registered....")
            else:
                print("=== registered students ===")
                for u,data in students.items():
                    print(f"{data['name']} ({u})")
                print()
        elif ch == 2 :
            view_result()
        elif ch == 3:
            print("admin logged out ....")
            break
        else:
            print("invalid input....")

while True:
    print("1. register")
    print("2. student login")
    print("3. admin login")
    print("4. exit")
    ch = int(input("enter your choice : "))
    if ch == 1:
        register_student()
    elif ch == 2:
        student_login()
    elif ch == 3:
        admin_login()
    elif ch == 4:
        print("existing our system....")
        break
    else:
        print("invalid option |  please enter coorrect option")         