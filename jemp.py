#-*-coding:utf8;-*-
# Import module(s)
from random import randint

# Declare global variables
level = raw_input('(b)eginner, (i)ntermediate or (e)xpert? ')
how_many = int(raw_input('How many questions would you like? '))
prod = 0
operator_dict = {'+': 1, '-': 2, '*': 3, '/': 4}

# Set difficulty level
def lev(level):
    global x
    if level == 'b':
        x = 10
    elif level == 'i':
        x = 25
    else:
        x = 100

# dealing with division
def div():
    global n1, n2
    if n1 % n2 > 0 == False or n1 < n2 == True:
        n1 = randint(1, x) 
        n2 = randint(1, x)
        div()

# Set question method
def prob(oper):
    global prod, sign
    if oper == 'a':
        prod = n1 + n2
        sign = '+'
    elif oper == 's':
        prod = n1 - n2
        sign = '-'
    elif oper == 'm':
        prod = n1 * n2
        sign = '*'
    elif oper == 'd':
        div()
        prod = n1 / n2
        sign = '/'
    elif oper == 'r':
        y = randint(0, 3)
        prod = operator_dict.values()[y]
        sign = operator_dict.keys()[y]
    else:
        print 'Please choose valid method!\n'
        oper = raw_input('(a)ddition, (s)ubtraction, (m)ultiplication (d)ivision or (r)andom? ')
        
# Prompt user to play again
def new():
    global how_many, level
    new_game = raw_input('Continue - (y)es/(n)o?: ')
    if new_game == 'y':
        level = raw_input('(b)eginner, (i)ntermediate or (e)xpert? ')
        how_many = int(raw_input('How many questions would you like? '))
        compute()
    else:
        print "Thanks for playing!"
        
# Main game code
def compute():
    global questions, correct, ans, prod, oper, n1, n2
    correct = 0
    questions = 0
    oper = raw_input('(a)ddition, (s)ubtraction, (m)ultiplication (d)ivision or (r)andom? ')
    lev(level)
    for i in range(how_many):
        n1 = randint(1, x) 
        n2 = randint(1, x)
        operator_dict['+'] = n1 + n2
        operator_dict['-'] = n1 - n2
        operator_dict['*'] = n1 * n2
        operator_dict['/'] = n1 / n2
        prob(oper)
        ans = int(raw_input("What's %d %s %d? " % (n1, sign, n2))) 
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