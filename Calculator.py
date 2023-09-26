import tkinter as tk
import math
import functools
# 创建计算器窗口
root = tk.Tk()
root.title("Consonnm's 科学计算器")

# 创建显示结果的文本框
result_var = tk.StringVar()
result_var.set("")
result_display = tk.Entry(root, textvariable=result_var,
                          font=("Helvetica", 25), justify="right", bd=0, highlightthickness=0,state="readonly")
result_display.configure(bg=root.cget('bg'))
result_display.grid(row=0, column=0, columnspan=5)

# 计算阶乘


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 定义计算函数
def calculate_science(l, temp, ch):
    flag = 0
    temp_val = ""
    i = l
    while(i < len(temp)):
        sub_2 = temp[i:i+2]
        sub_3 = temp[i:i+3]
        sub_4 = temp[i:i+4]
        if(sub_2 == 'ln' or sub_3 == 'sin' or sub_3 == 'cos' or sub_3 == 'tan' or sub_3 == 'sqrt' or sub_3 == 'log' or sub_4 == 'asin' or sub_4 == 'acos' or sub_4 == 'atan' or sub_4 == 'sqrt'):
            le = 0
            if(sub_2 == 'ln'):
                le = 2
            elif (sub_3 == 'sin' or sub_3 == 'cos' or sub_3 == 'tan' or sub_3 == 'sqrt' or sub_3 == 'log'):
                le = 3
            elif (sub_4 == 'asin' or sub_4 == 'acos' or sub_4 == 'atan' or sub_4 == 'sqrt'):
                le = 4
            re = calculate_science(i+le, temp, 1)
            if(sub_2 == 'ln'):
                temp_val += str(math.log(re[0]))
            elif (sub_3 == 'sin'):
                temp_val += str(math.sin(re[0]/180*math.pi))
            elif (sub_3 == 'cos'):
                temp_val += str(math.cos(re[0]/180*math.pi))
            elif (sub_3 == 'tan'):
                temp_val += str(math.tan(re[0]/180*math.pi))
            elif (sub_3 == 'log'):
                temp_val += str(math.log10(re[0]))
            elif (sub_4 == 'asin'):
                temp_val += str(math.asin(re[0]))
            elif (sub_4 == 'acos'):
                temp_val += str(math.acos(re[0]))
            elif (sub_4 == 'atan'):
                temp_val += str(math.atan(re[0]))
            elif (sub_4 == 'sqrt'):
                temp_val += str(math.sqrt(re[0]))
            i = re[1]
        elif(temp[i] == '!'):
            flag_1 = 0
            temp_val_1 = ""
            for j in range(len(temp_val)-1, -1, -1):
                if(temp_val[j] == '('):
                    if(flag_1 > 0):
                        flag_1 -= 1
                    else:
                        temp_val = temp_val[:j+1] + \
                            str(factorial_iterative(eval(temp_val_1)))
                        break
                elif(temp_val[j] == ')'):
                    flag_1 += 1
                temp_val_1 = temp_val[j]+temp_val_1
                if((temp_val[j] < '0' or temp_val[j] > '9' or j == 0) and flag_1 == 0):
                    if(j == 0 or temp_val[j] == '('):
                        temp_val = temp_val[:j] + \
                            str(factorial_iterative(eval(temp_val_1)))
                    else:
                        temp_val = temp_val[:j+1] + \
                            str(factorial_iterative(eval(temp_val_1)))
                    break
        elif(temp[i] == '^'):
            temp_val += '**'
        elif(temp[i] == 'x'):
            temp_val += '*'
        elif(temp[i] == '÷'):
            temp_val += '/'
        elif(temp[i] == 'π'):
            temp_val += str(math.pi)
        elif(temp[i] == 'e'):
            temp_val += str(math.e)
        else:
            if(temp[i] == '('):
                flag += 1
            elif(temp[i] == ')'):
                flag -= 1
            temp_val += temp[i]
            if(((flag == 0 and temp[i] == ')') or i == len(temp)-1) and (ch == 1)):
                return (eval(temp_val), i)
        i += 1
    return (eval(temp_val), len(temp)-1)


def calculate(temp):
    try:
        temp = result_var.get()
        re = calculate_science(0, temp, 0)
        result = re[0]
        list.clear()
        result_var.set(result)
        list.append(str(result))
    except Exception as e:
        result_var.set("Error")


def Backspace():
    try:
        if(len(list) != 0):
            result_var.set(result_var.get()[:len(
                result_var.get())-len(list[len(list)-1])])
            del[list[len(list)-1]]
    except Exception as e:
        result_var.set("Error")


def input_science(button):
    try:
        result_var.set(result_var.get() + button + '(')
        list.append(button + '(')
    except Exception as e:
        result_var.set("Error")


def input_normal(button):
    try:
        result_var.set(result_var.get() + button)
        list.append(button)
    except Exception as e:
        result_var.set("Error")


def clear():
    try:
        result_var.set("")
        list.clear()
    except Exception as e:
        result_var.set("Error")


# 创建按钮并布局
buttons = [
    'asin', 'acos', 'atan', 'sqrt', 'AC',
    'C', 'Back', '%', '÷', '!',
    '7', '8', '9', 'x', 'sin',
    '4', '5', '6', '-', 'cos',
    '1', '2', '3', '=', 'tan',
    'π', '0', '.', '+', 'ln',
    '(', ')', '^', 'e', 'log'

]
list = []
row_val = 1
col_val = 0
result_var.set("")
for button in buttons:
    if(button == 'sin' or button == 'cos' or button == 'tan' or button == 'sqrt' or button == 'log' or button == 'ln' or button == 'asin' or button == 'acos' or button == 'atan'):
        tk.Button(root, text=button, width=5, height=2, relief=tk.FLAT, command=functools.partial(
            input_science, button)).grid(row=row_val, column=col_val)
    elif button == 'Back':
        tk.Button(root, text=button, width=5, height=2, relief=tk.FLAT,
                  command=Backspace).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(root, text=button, width=5, height=2, relief=tk.FLAT,
                  command=functools.partial(calculate, result_var.get())).grid(row=row_val, column=col_val)
    elif button == 'C' or button == 'AC':
        tk.Button(root, text=button, width=5, height=2, relief=tk.FLAT,
                  command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, relief=tk.FLAT, command=functools.partial(
            input_normal, button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# 运行计算器
root.mainloop()
