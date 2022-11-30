import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor



import math
from tkinter import *

def click(value):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    input_ = ''
    try:

        if value == 'C':
            #     input_ = input_[0:len(input_)-1]
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            #    input_ = 'sqrt(' + entryField.get() + ')'
            ex = "sqrt(" + entryField.get() + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            #answer = math.sqrt(eval(ex))
            return

        elif value == 'π':
            input = entryField.get()
            if not input:
                ex = input + "pi"
            elif input[-1] == '*' or input[-1] == '+'  or input[-1] == '-'  or input[-1] == '/':
                ex = input + "pi"
            else:
                ex = input + "*pi"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'cosθ':
            input = entryField.get()
            ex = "cos(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
           # answer = math.cos(math.radians(eval(ex)))
            return

        elif value == 'tanθ':
            input = entryField.get()
            ex = "tan(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
           # answer = math.tan(math.radians(eval(ex)))
            return

        elif value == 'sinθ':
            input = entryField.get()
            ex = "sin(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
         #   answer = math.sin(math.radians(eval(ex)))
            return

        elif value == '2π':
            input = entryField.get()
            if not input:
                ex = input + "2*pi"
            elif input[-1] == '*' or input[-1] == '+'  or input[-1] == '-'  or input[-1] == '/':
                ex = input + "(2*pi)"
            else:
                ex = input + "*2*pi"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'cosh':
            input = entryField.get()
            ex = "cosh(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
           # answer = math.cosh(eval(ex))
            return

        elif value == 'tanh':
            input = entryField.get()
            ex = "tanh(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
        # answer = math.cosh(eval(ex))
            return

        elif value == 'sinh':
            input = entryField.get()
            ex = "sinh(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
        # answer = math.cosh(eval(ex))
            return

        elif value == chr(8731):
            input = entryField.get()
            ex = 'cbrt' + "(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return
          #  answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # 7**2
            input = entryField.get()
            ex =  input + "^"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'x\u00B3':
            input = entryField.get()
            ex = input + "^3"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'x\u00B2':
            input = entryField.get()
            ex = input + "^2"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'ln':
            input = entryField.get()
            ex = "ln(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'deg':
            input = entryField.get()
            ex = "deg(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return
        # answer = math.degrees(eval(ex))

        elif value == "rad":
            input = entryField.get()
            ex = "rad(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
         #   answer = math.radians(eval(ex))
            return

        elif value == 'e':
            input = entryField.get()
            if not input:
                ex = input + "e"
            elif input[-1] == '*' or input[-1] == '+' or input[-1] == '-' or input[-1] == '/':
                ex = input + "e"
            else:
                ex = input + "*e"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'log₁₀':
            input = entryField.get()
            ex = "log10(" + input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == '(':
            input = entryField.get()
            ex = "(" + input
            entryField.delete(0,END)
            entryField.insert(0, ex)
            return


        elif value == ')':
            input = entryField.get()
            ex = input + ")"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'x!':
            input = entryField.get()
            ex = "(" + input + ")!"
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            try:
                input = InputStream(entryField.get())
                lexer = ExprLexer(input)
                stream = CommonTokenStream(lexer)
                parser = ExprParser(stream)
                tree = parser.prog()

                res = MyExprVisitor().visitProg(tree)  # Evaluate the expression
                answer = res
                print(res)


            except IndexError:
                answer = "ERROR"
            finally:
                entryField.delete(0, END)
                entryField.insert(0, answer)
                return


        else:
            input = entryField.get()

            if input:
                if input[-1] == 'pi' or input[-1] == 'e':
                    ex = input + "*" + value
                elif input == 'ERROR':
                    ex = value
                else:
                    ex = input + value
            else:
                ex = value
            print(value)
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

    #    entryField.delete(0, END)
    #  entryField.insert(0, answer)

    except Exception:
        answer = "ERROR"
        entryField.delete(0, END)
        entryField.insert(0, answer)
        return


root = Tk()
# title
root.title('Calculator')
# background color
root.config(bg='grey30')
# geometry setup
root.geometry('730x480+100+100')

# entry field with setup
entryField = Entry(root, font=('arial', 20, 'bold'), bg='grey50', fg='white', bd=5, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowvalue = 1
columnvalue = 0

for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='grey30', fg='grey50',
                    font=('arial', 18, 'bold'), command=lambda button=i: click(button))
    # creating button and activebackground=color set here
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
