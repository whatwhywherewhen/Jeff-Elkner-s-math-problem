#! /usr/bin/env python
#-*-coding:utf8;-*-
# Import module(s)
print "\nJeff Elkner's Math Quiz"
print "From http://openbookproject.net/pybiblio/practice/elkner/mathquiz.php\n"

from random import randint

# Declare global variables
level = raw_input('(b)eginner, (i)ntermediate or (e)xpert? ')
how_many = int(raw_input('How many questions would you like? '))
oper = raw_input('(a)ddition, (s)ubtraction, (m)ultiplication (d)ivision or (r)andom? ')

scoreboard = {
	   'Addition Asked': 0,
	   'Addition Correct': 0,
	   'Subtraction Asked': 0,
	   'Subtraction Correct': 0,
	   'Multiplication Asked': 0,
	   'Multiplication Correct': 0,
	   'Division Asked': 0,
	   'Division Correct': 0,
	   'Total Asked': 0,
	   'Total Correct': 0,
}

def add_check():
    global ans, prod, sign
    prod = n1 + n2
    sign = '+'
    ans = int(raw_input("What's %d %s %d? " % (n1, sign, n2)))
    scoreboard['Addition Asked'] += 1
    if ans == prod:
        scoreboard['Addition Correct'] += 1

def sub_check():
    global ans, prod, sign
    prod = n1 - n2
    sign = '-'
    ans = int(raw_input("What's %d %s %d? " % (n1, sign, n2)))
    scoreboard['Subtraction Asked'] += 1
    if ans == prod:
        scoreboard['Subtraction Correct'] += 1  
 
def mul_check():
    global ans, prod, sign
    prod = n1 * n2
    sign = '*'
    ans = int(raw_input("What's %d %s %d? " % (n1, sign, n2)))
    scoreboard['Multiplication Asked'] += 1
    if ans == prod:
        scoreboard['Multiplication Correct'] += 1
 
def div_check():
    global ans, prod, sign
    div()
    prod = n1 / n2
    sign = '/'
    ans = int(raw_input("What's %d %s %d? " % (n1, sign, n2)))
    scoreboard['Division Asked'] += 1
    if ans == prod:
        scoreboard['Division Correct'] += 1

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
    if oper == 'a':
        add_check()
    elif oper == 's':
        sub_check()
    elif oper == 'm':
        mul_check()
    elif oper == 'd':
        div_check()
    elif oper == 'r':
        y = randint(0, 3)
        if y == 3:
            div_check()
        elif y == 2:
            mul_check()
        elif y == 1:
            sub_check()
        else:
            add_check()
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
    global questions, correct, ans, prod, oper, n1, n2, scoreboard
    correct = 0
    questions = 0
    lev(level)
    for i in range(how_many):
        scoreboard['Total Asked'] += 1
        n1 = randint(1, x) 
        n2 = randint(1, x)
        prob(oper) 
        questions += 1
        if ans == prod:
            print "That's right -- well done.\n"
            scoreboard['Total Correct'] += 1
            correct += 1
        else:
            print "No, I'm afraid the answer is %d.\n" % prod
        if how_many == questions:
            for key in sorted(scoreboard):
                print "  ", scoreboard[key], key
            print "\nI asked you %d questions. You got %d of them right.\n" % (how_many, correct)
            if (float(scoreboard['Total Correct']) / float(questions)) * 100 > 66.66666666:
                print "Well done!\n"
            elif (float(scoreboard['Total Correct']) / float(questions)) * 100 < 33.33333333:
                print "Please ask your math teacher for help!\n"
            else:
                print "You need more practice\n"
            new()
            
compute()
