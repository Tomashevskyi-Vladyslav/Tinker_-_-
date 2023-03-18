from tkinter import *
from tkinter import ttk
import sus
import re

function_temporary_variable = sus.random_number_enerator()
print(function_temporary_variable)
var = []

def is_valid(newval):
    result=  re.match("^\d{0,4}$", newval) is not None
    return result

def clean():
    label_11 = Label(text = '                                                                                                               ', font = "Arial, 13")
    label_11.place(x=0, y=0)
    label22 = Label(text='                                                                                                                  ', font="Arial 15")
    label22.place(x=130, y=299)
    label_12 = Label(text = '                                                                                                               ', font = "Arial, 13")
    label_12.place(x=0, y=20)
    label_13 = Label(text = '                                                                                                               ', font = "Arial, 13")
    label_13.place(x=0, y=40)
    label_14 = Label(text = '                                                                                                               ', font = "Arial, 13")
    label_14.place(x=0, y=60)
    label = Label(text='                                                                                                                    ', font="Arial 20")
    label.place(x=5, y=450)
    label1 = Label(text='                                                                                                                   ', font="Arial 20")
    label1.place(x=60, y=270)
    label00=Label(foreground="red", text='                                                                                                  ', font = "Arial, 14")
    label00.place(x=0, y=450)

def main_print():
    label_11 = Label(text = var[0], font = "Arial, 13")
    label_11.place(x=0, y=0)
    label_12 = Label(text = var[1], font = "Arial, 13")
    label_12.place(x=0, y=20)
    label_13 = Label(text = var[2], font = "Arial, 13")
    label_13.place(x=0, y=40)
    label_14 = Label(text = var[3], font = "Arial, 13")
    label_14.place(x=0, y=60)

def show_message():
    dictionary_for_numbering_correct_numbers = {0:'First', 1:'Second', 2:'Third ', 3:'Fourth'}
    global function_temporary_variable
    global var
    global function_temporary_variable
    sequence_check_sheet = entry.get()
    sequence_check_sheet_1 = set(sequence_check_sheet)
    counter = 0
    count_element = 0
    bb=0
    clean()
    if len(sequence_check_sheet)==4:

        if len(sequence_check_sheet_1) != 4 :
            label00=Label(foreground="red", text='Numbers must not be repeated', font = "Arial, 14")
            label00.place(x=110, y=450)
            bb+=1

        for i in range(4):
            if int(sequence_check_sheet[counter])==function_temporary_variable[counter]:
                var.append(f'''{dictionary_for_numbering_correct_numbers[counter]} element in place''')
                count_element+=1
            elif int(sequence_check_sheet[counter]) in function_temporary_variable:
                var.append(f'''{dictionary_for_numbering_correct_numbers[counter]} the element is not in place, but it is in the hidden number''')
            else :
                var.append(f'''{dictionary_for_numbering_correct_numbers[counter]} the element is not in the cryptic number''')
            counter+=1

        if count_element!=4 and bb!=1:
            main_print()

        bb=0
        var = []
        if count_element==4:
            label = Label(text='Сongratulations you guessed the number', font="Arial 15")
            label.place(x=60, y=270)

            label22 = Label(text='New number generated', font="Arial 15")
            label22.place(x=130, y=299)
            function_temporary_variable = sus.random_number_enerator()
            print()
            print(function_temporary_variable)  

    else :
        label=Label(foreground="red", text='You made a mistake, you need to enter 4 natural numbers', font = "Arial, 14")
        label.place(x=5, y=450)

root = Tk()
root.title("Order - Disorder")
root.geometry("500x500")

root.resizable(width=False, height=False)

check = (root.register(is_valid), "%P")
errmsg = StringVar()
 
entry = ttk.Entry(root, justify = 'center', width = 13, validate="key", validatecommand=check) 
entry.place(x=200, y=200)

btn = ttk.Button(text = "Enter", command=show_message)
btn.place(x=203, y=221)

main_text = Label(text="Enter 4 digit number :", font="Arial 15")
main_text.place(x=0, y=194)
  
root.mainloop()