# 软工作业1

### 0. 界面及功能展示

![img](https://img-blog.csdnimg.cn/c405efcdbfa642939f6aefc5ed9cdea3.gif)

### 1. PSP表格

| PSP                                     | Personal Software Process Stages        | 预估耗时（分钟） | 实际耗时（分钟） |
| --------------------------------------- | --------------------------------------- | ---------------- | ---------------- |
| Planning                                | 计划                                    | 20               | 15               |
| • Estimate                              | • 估计这个任务需要多少时间              | 20               | 15               |
| Development                             | 开发                                    | 580              | 635              |
| • Analysis                              | • 需求分析 (包括学习新技术）            | 60               | 60               |
| • Design Spec                           | • 生成设计文档                          | 70               | 60               |
| • Design Review                         | • 设计复审                              | 10               | 20               |
| • Coding Standard                       | • 代码规范 (为目前的开发制定合适的规范) | 10               | 15               |
| • Design                                | • 具体设计                              | 30               | 50               |
| • Coding                                | • 具体编码                              | 240              | 300              |
| • Code Review                           | • 代码复审                              | 60               | 30               |
| • Test                                  | • 测试（自我测试，修改代码，提交修改）  | 100              | 100              |
| Reporting                               | 报告                                    | 120              | 100              |
| • Test Repor                            | • 测试报告                              | 20               | 20               |
| • Size Measurement                      | • 计算工作量                            | 10               | 10               |
| • Postmortem & Process Improvement Plan | • 事后总结, 并提出过程改进计划          | 90               | 70               |
|                                         | 合计                                    | 720              | 750              |

### 2. 解题思路描述

​    科学计算器本质上处理的是一串具有多重优先级的计算表达式，其难点主要如下：

​    1.括号匹配

​        通过 flag增减 标记 '(' 和 ')' 来实现括号的匹配

​    2.多重函数嵌套

​        显现多重函数嵌套可以通过函数的递归来解决问题，需要注意的点是边界的划分

​    3.计算阶乘的时候需要向前匹配

​        在前面已经处理过阶乘前面计算表达式的基础上向前匹配一个括号表式或者一个数字

### 3. 核心代码

```python
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
```

### 3. 设计与实现过程

1. 导入所需的库：
2. 
   1. tkinter：用于创建GUI窗口。
   2. functools：用于创建部分函数，用于按钮点击事件的绑定。
   3. math：提供数学函数和常数。
3. 创建计算器窗口：
   - 创建一个tkinter窗口，并设置窗口标题为 "Consonnm's 科学计算器"。
4. 创建显示结果的文本框：
   - 创建一个tkinter Entry（文本框）小部件，用于显示计算结果。
   - 使用StringVar来管理文本框中的文本内容。
   - 设置文本框的字体、文本对齐方式、边框等属性。
5. 定义计算函数 `calculate_science`：
   - `calculate_science`函数用于处理用户输入的表达式并计算结果。
   - 函数采用三个参数：0/1标记返回情况，用户输入字符串 `temp` 和一个标志 `ch`。
   - 通过循环遍历输入表达式 `temp` 中的字符，逐步解析并计算表达式。
   - 使用特定的字符串标记（如'ln'、'sin'等）来识别数学函数和常数，并调用相关的math库函数进行计算。
   - 使用标志 `flag` 来跟踪括号的开启和关闭，以便正确计算表达式。
   - 函数返回一个包含计算结果和当前位置的元组。
6. 定义计算按钮的事件处理函数 `calculate`：
   - `calculate` 函数从文本框中获取用户输入的表达式。
   - 调用 `calculate_science` 函数来计算表达式的结果，并将结果设置为文本框的内容。
   - 如果计算出错，将显示 "Error"。
7. 定义其他按钮事件处理函数：
   - `Backspace` 函数用于删除最后一个字符。
   - `input_science` 函数用于处理科学函数按钮的点击事件，将对应的函数名添加到文本框中。
   - `input_normal` 函数用于处理普通按钮的点击事件，将按钮上的文本添加到文本框中。
   - `clear` 函数用于清空文本框内容。
8. 创建按钮并布局：
   - 定义按钮的文本和布局顺序，包括科学函数按钮、操作符按钮、数字按钮、等号等。
   - 使用循环创建按钮，并为每个按钮绑定相应的事件处理函数。
9. 运行计算器：
   - 启动tkinter的主事件循环，使计算器界面可以响应用户操作。

### 4. 程序性能改进

- **代码思路**：一开始采用后缀表达式和正则匹配，后来采用递归处理字符串可以在O(n)的时间复杂度内处理完计算表达式

### 5. 单元测试展示

​    ![img](https://img-blog.csdnimg.cn/725a3484b9b24b919e9ae3a9857e1455.png)

- **单元测试样例**

```python
        # 测试综合加法、减法、乘法和除法
        result = calculate_science(0, '2+2-3x4÷2', 0)
        self.assertEqual(result[0], -2)

        # 测试带有括号的表达式
        result = calculate_science(0, '(2+(3*4))%8*2^2', 0)
        self.assertEqual(result[0], 24)

        # 测试科学计算函数 - 正弦值、平方根、自然对数综合
        result = calculate_science(0, 'sin(45)+sqrt(16)-ln(e)+cos(45)+tan(45)', 0)
        self.assertAlmostEqual(result[0], 5.4142, places=4)

        # 测试科学计算函数 asin,acos,atan,atan
        result = calculate_science(0, 'asin(0.5)+acos(0.5)+atan(1)', 0)
        self.assertAlmostEqual(result[0], 2.35619, places=4)

        # 测试科学计算函数 log,
        result = calculate_science(0, 'log(10)', 0)
        self.assertAlmostEqual(result[0], 1, places=4)

        # 测试科学计算函数 - 阶乘
        result = calculate_science(0, '1+5!', 0)
        self.assertEqual(result[0], 121)

        # 测试阶乘嵌套括号
        result = calculate_science(0, '2+(3*(4-1)!)', 0)
        self.assertEqual(result[0], 20)

        # 测试科学计算函数 - 正弦值嵌套平方根
        result = calculate_science(0, 'sqrt(sin(45))', 0)
        self.assertAlmostEqual(result[0], 0.8409, places=4)

        # 测试科学计算函数 - 对数嵌套阶乘
        result = calculate_science(0, 'ln(5!)*π', 0)
        self.assertAlmostEqual(result[0], 15.0403, places=4)
        
        # 测试正弦值嵌套阶乘
        result = calculate_science(0, 'sqrt(sin(5!))', 0)
        self.assertAlmostEqual(result[0], 0.9306, places=4)
```

### 6. 异常处理

- **对不符合规范计算表达式的式子抛出异常并显示Error**

```python
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
```

### 7. 心路历程和收获

- **心路历程**：再一开始的时候没有考虑边读入边处理计算的结果，这样导致了退格键的不好设计后来修改为了再等号输入后对整个计算表达式进行递归计算，这样使得整个设计清晰明了，逻辑更加的明析。
- **用户界面细节**：关注用户界面的细节，包括按钮外观、文本框字体和对齐方式，以提高用户体验。
- **学习收获**：通过项目学到了关于tkinter库、字符串处理、异常处理、函数编程等方面的知识，锻炼了问题解决和调试能力。
- **总结**：这个项目不仅提高了Python和tkinter的理解，还加强了编程技能和软件单元测试能力