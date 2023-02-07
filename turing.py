def turing_test():
    print("Let's start the Turing Test.\n")
    
    name = input("What is your name?\n")
    print("Nice to meet you, " + name + "!\n")
    
    questions = ["What's your favorite color?", "What's your favorite movie?", "What's your favorite book?", "What's your favorite TV show?","What did you have for lunch today","What is the color of your favorite vegetable","If you were in doubt that I was human rather than machine what question would you ask me?","What is possibly your earliest memory?","What High School did you go to?,","Who was your favorite teacher there?"]
    answers = []
    
    for question in questions:
        answer = input(question + "\n")
        answers.append(answer)
        
    score = 0
    
    for answer in answers:
        if answer.lower() == "I don't have one." or answer.lower() == "I don't know.":
            score += 1
            
    if score >= len(questions) / 2:
        print("I am not sure if you are human or Machine.\n")
    else:
        print("Based on your answers, it is confirmed that you are human.\n")
        
turing_test()
