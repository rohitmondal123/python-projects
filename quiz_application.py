questions = [
    {
        "question": "what is the capital of india ?",
        "options": ["delhi","mumbai","kolkata","chennai"],
        "answer": 1
    },{
        "question": "what is 2 + 2 ?",
        "options": ["2","5","6","4"],
        "answer": 4
    },{
        "question": "who wrote harry potter ?",
        "options": ["j.k.rowling","mark twain","j.r.r.tolkien","roald dahl"],
        "answer": 1
    },{
        "question": "who was the first president o india ?",
        "options": ["rajendra prasad","jawaharlal nehru","s.radhakrishnan","b.r.ambedkar"],
        "answer": 1
    },{
        "question": "which is the longest river the world ?",
        "options": ["amazon","ganga","nile","yangtze"],
        "answer": 3
    },{
        "question": "what is the currency of united states ?",
        "options": ["dollar","pound","yen","euro"],
        "answer": 1
    },{
        "question": "which is the largest ocean in the world  ?",
        "options": ["atlantic ocean","indian ocean","pacific ocean","arctic ocean"],
        "answer": 3
    },{
        "question": "which gas is essential for breathing ?",
        "options": ["carbon dioxide","oxygen","nitrogen","helium"],
        "answer": 2
    },{
        "question": "what is the national animal of india ?",
        "options": ["lion","tiger","elephant","peacock"],
        "answer": 2
    },{
        "question": "who invented the telephone ?",
        "options": ["thomas edison","alexander graham bell","nikola tesla","isaac newton"],
        "answer": 2
    }
]

score = 0
for i,q in enumerate(questions):
    print(f"Q{i + 1} : {q['question']}")
    for idx,opt in enumerate(q["options"],start=1):
        print(f"{idx} : {opt}")
    try:
        choice = int(input("Enter your answer(1 - 4) : "))
    except ValueError:
        print("invalid input .....")
        continue
    if choice == q["answer"]:
        print("CORRECT !")
        score += 1
    else:
        print("INCORRECT !")
if score == len(questions):
    print(f"Congratulations! You got {score} out of {len(questions)} ")
else:
    print(f"You got {score} out of {len(questions)} ")