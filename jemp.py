#-*-coding:utf8;-*-

print "This is console module"
from random import randint 
correct = 0
questions = 0
x = 0
level = raw_input('(b)eginner, (i)ntermediate or (e)xpert? ')
how_many = int(raw_input('How many questions would you like? '))

def lev(level):
    global x
    if level == 'b':
        x = 10
    elif level == 'i':
        x = 25
    else:
        x = 100
     
def new():
    global how_many, level
    new_game = raw_input('Continue - (y)es/(n)o?: ')
    if new_game == 'y':
        level = raw_input('(b)eginner, (i)ntermediate or (e)xpert? ')
        how_many = int(raw_input('How many questions would you like? '))
        compute()
    else:
        print "Thanks for playing!"
     
def compute():
    global questions, correct, ans, prod
    correct = 0
    questions = 0
    lev(level)
    for i in range(how_many):
        n1 = randint(1, x) 
        n2 = randint(1, x) 
        prod = n1 * n2 
        ans = int(raw_input("What's %d times %d? " % (n1, n2))) 
        questions += 1
        if ans == prod: 
            print "That's right -- well done.\n" 
            correct += 1
        else: 
            print "No, I'm afraid the answer is %d.\n" % prod
        if how_many == questions:
            print "\nI asked you %d questions. You got %d of them right." % (how_many, correct)
            if (float(correct) / float(questions)) * 100 > 66.66666666:
                print "Well done!"
            elif (float(correct) / float(questions)) * 100 < 33.33333333:
                print "Please ask your math teacher for help!"
            else:
                print "You need more practice"
            new()
            
compute()
