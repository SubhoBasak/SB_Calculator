import tkinter as tk

# the main class
class App:

    # initialize all the components.
    def __init__(self, master):
        self.master = master
        self.master.title('SB Calculator')
        self.master.iconbitmap('icon.ico')
        self.master.config(bg = '#636664')
        self.master.minsize(300, 400)

        self.font = ('Arial', 18)
        self.data = tk.StringVar()
        self.val = None             # to store the first operand. the second operand will directly taken from the text box.
        self.operator = None        # to store the operator.
        self.clrscr = False         # to keep a note that the screen is clear or not

        self.top_level = tk.Frame(self.master, bg = '#636664')
        self.top_level.pack(fill = tk.BOTH, expand = True, padx = 5, pady = 5)

        self.entry = tk.Entry(self.top_level, font = ('Arial', 30), width = 10, textvariable = self.data, bg = '#7d827e')
        self.entry.pack(fill = tk.BOTH, expand = True, pady = 5)

        # each frame is used to hold each row of buttons.
        self.frame_0 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_0.pack(fill = tk.BOTH, expand = True)

        self.frame_1 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_1.pack(fill = tk.BOTH, expand = True)

        self.frame_2 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_2.pack(fill = tk.BOTH, expand = True)

        self.frame_3 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_3.pack(fill = tk.BOTH, expand = True)

        self.frame_4 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_4.pack(fill = tk.BOTH, expand = True)

        # delete button
        self.button_DEL = tk.Button(self.frame_0, text = 'Delete', font = ('Arial', 12), command = self.delete, height = 1)
        self.button_DEL.config(relief = tk.FLAT, bg = 'gray')
        self.button_DEL.pack(side = tk.RIGHT, padx = 2, pady = 2)

        # clear button
        self.button_CLR = tk.Button(self.frame_0, text = 'Clear', font = ('Arial', 12), command = self.clear, height = 1)
        self.button_CLR.config(relief = tk.FLAT, bg = 'gray')
        self.button_CLR.pack(side = tk.RIGHT, padx = 2, pady = 2)

        # digit 1 button
        self.button_1 = tk.Button(self.frame_1, text = '1', font = self.font, command = self.one, height = 2, width = 4)
        self.button_1.config(relief = tk.FLAT, bg = 'gray')
        self.button_1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 2, pady = 2)

        # digit 2 button
        self.button_2 = tk.Button(self.frame_1, text = '2', font = self.font, command = self.two, height = 2, width = 4)
        self.button_2.config(relief=tk.FLAT, bg='gray')
        self.button_2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 2, pady = 2)

        # digit 3 button
        self.button_3 = tk.Button(self.frame_1, text = '3', font = self.font, command = self.three, height = 2, width = 4)
        self.button_3.config(relief=tk.FLAT, bg='gray')
        self.button_3.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 4 button
        self.button_4 = tk.Button(self.frame_2, text = '4', font = self.font, command = self.four, height = 2, width = 4)
        self.button_4.config(relief=tk.FLAT, bg='gray')
        self.button_4.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 5 button
        self.button_5 = tk.Button(self.frame_2, text = '5', font = self.font, command = self.five, height = 2, width = 4)
        self.button_5.config(relief=tk.FLAT, bg='gray')
        self.button_5.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 6 button
        self.button_6 = tk.Button(self.frame_2, text = '6', font = self.font, command = self.six, height = 2, width = 4)
        self.button_6.config(relief=tk.FLAT, bg='gray')
        self.button_6.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 7 button
        self.button_7 = tk.Button(self.frame_3, text = '7', font = self.font, command = self.seven, height = 2, width = 4)
        self.button_7.config(relief=tk.FLAT, bg='gray')
        self.button_7.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 8 button
        self.button_8 = tk.Button(self.frame_3, text = '8', font = self.font, command = self.eight, height = 2, width = 4)
        self.button_8.config(relief=tk.FLAT, bg='gray')
        self.button_8.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 9 button
        self.button_9 = tk.Button(self.frame_3, text = '9', font = self.font, command = self.nine, height = 2, width = 4)
        self.button_9.config(relief=tk.FLAT, bg='gray')
        self.button_9.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # digit 0 button
        self.button_0 = tk.Button(self.frame_4, text = '0', font = self.font, command = self.zero, height = 2, width = 4)
        self.button_0.config(relief=tk.FLAT, bg='gray')
        self.button_0.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # dot (.) button
        self.button_DOT = tk.Button(self.frame_4, text = '.', font = self.font, command = self.dot, height = 2, width = 4)
        self.button_DOT.config(relief=tk.FLAT, bg='gray')
        self.button_DOT.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # equals to (=) button
        self.button_EQL = tk.Button(self.frame_4, text = '=', font = self.font, command = self.enter, height = 2, width = 4)
        self.button_EQL.config(relief=tk.FLAT, bg='gray')
        self.button_EQL.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # addition (+) button
        self.button_ADD = tk.Button(self.frame_4, text = '+', font = self.font, command = self.add_function, height = 2, width = 4)
        self.button_ADD.config(relief=tk.FLAT, bg='gray')
        self.button_ADD.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # subtraction (-) button
        self.button_SUB = tk.Button(self.frame_3, text = '-', font = self.font, command = self.sub_function, height = 2, width = 4)
        self.button_SUB.config(relief=tk.FLAT, bg='gray')
        self.button_SUB.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # multiplication (*) button
        self.button_MUL = tk.Button(self.frame_2, text = '*', font = self.font, command = self.mul_fuction, height = 2, width = 4)
        self.button_MUL.config(relief=tk.FLAT, bg='gray')
        self.button_MUL.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        # divition (/) button
        self.button_DIV = tk.Button(self.frame_1, text = '/', font = self.font, command = self.div_function, height = 2, width = 4)
        self.button_DIV.config(relief=tk.FLAT, bg='gray')
        self.button_DIV.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

    # delete button's function, which delete one digit from the text box.
    def delete(self):
        tmp = self.data.get()
        if len(tmp) > 0:
            tmp = tmp[:-1]
            self.data.set(tmp)

    # clear button's function, which clear the text box and clear all the previous inputs.
    def clear(self):
        self.data.set('')
        self.val = None
        self.operator = None
        self.clrscr = False

    # digit 1 button's function, which insert 1 at the end of the text box.
    def one(self):
        if self.clrscr:         # if it require to clear the screen then
            self.clrscr = False # first it change the flag
            self.data.set('')   # then it clear the text box.
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '1')

    # digit 2 button's function, which insert 2 at the end of the text box.
    def two(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '2')

    # digit 3 button's function, which insert 3 at the end of the text box.
    def three(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '3')

    # digit 4 button's function, which insert 4 at the end of the text box.
    def four(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '4')

    # digit 5 button's function, which insert 5 at the end of the text box.
    def five(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '5')

    # digit 6 button's function, which insert 6 at the end of the text box.
    def six(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '6')

    # digit 7 button's function, which insert 7 at the end of the text box.
    def seven(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '7')

    # digit 8 button's function, which insert 8 at the end of the text box.
    def eight(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '8')

    # digit 9 button's function, which insert 9 at the end of the text box.
    def nine(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '9')

    # digit 0 button's function, which insert 0 at the end of the text box.
    def zero(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '0')

    # dot (.) button's function, which insert (.) at the end of the text box.
    def dot(self):
        if self.clrscr:         # again clear screen requrement checking
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            if not '.' in self.data.get():
                if len(self.data.get()) > 0:        # first it check if there is digit present or not
                    self.entry.insert(tk.END, '.')  # if any digit present then it insert only a (.)
                else:
                    self.entry.insert(tk.END, '0.') # otherwise it insert 0.

    def enter(self):
        if self.val != None:        # it check if two operands is given or not
            tmp = self.data.get()   # if there is already a operand is given then it take the second operand
            if len(tmp) < 0:        # it check if the input data is empty or not
                return None
            self.data.set(eval(self.val + self.operator + tmp)) # then using the eval function the the operation is performed
            
            # reset all the values and flags
            self.val = None
            self.operator = None
            self.clrscr = True

    # addition button's function.
    def add_function(self):
        if self.val == None:        # it check if two operands is given or not
            tmp = self.data.get()   # if no operand is given then it take the first operand
            if len(tmp) > 0:        # it check if the input data is empty or not
                self.val = tmp      # if the input data is not empty then it initialize the val with the input value
            self.operator = '+'     # and the operator is set as '+'
            self.data.set('')       # then if clear the text box
        
        else:                       # if the one operand is already given then
            tmp = self.data.get()   # it take the second value
            if len(tmp) > 0:        # it check if the input data is empty or not, if it is not empty then
                result = str(eval(self.val+self.operator+tmp))  # it do the operation with the pending operator
                self.data.set(result)   # then the result is set in the output
                self.val = result       # and the first operand value is replaced with the result
                self.operator = '+'     # and the current operator is set as '+'
                self.clrscr = True      # andthe clear screent flag is set True
            else:
                self.operator = '+' # and if the input data is empty it just set the operator as '+'

    # subtraction button's function. logic is same as the add_function
    def sub_function(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '-'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val + self.operator + tmp))
                self.data.set(result)
                self.val = result
                self.operator = '-'
                self.clrscr = True
            else:
                self.operator = '-'

    # multiplication button's function. logic is same as the add_function
    def mul_fuction(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '*'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val + self.operator + tmp))
                self.data.set(result)
                self.val = result
                self.operator = '*'
                self.clrscr = True
            else:
                self.operator = '*'

    # divition button's function. logic is same as the add_function
    def div_function(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '/'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val + self.operator + tmp))
                self.data.set(result)
                self.val = result
                self.operator = '/'
                self.clrscr = True
            else:
                self.operator = '/'

# run the program
if __name__ == '__main__':
    root = tk.Tk()  # create the root window
    app = App(root) # create the App object with the root window
    root.mainloop() # start the root window
