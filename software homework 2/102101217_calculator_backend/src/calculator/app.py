from flask import Flask, request, jsonify, json

import math
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update, func, and_
from sqlalchemy import create_engine, Column, Integer, String, FLOAT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

HOSTNAME = "127.0.0.1"

USERNAME = "root"

PASSWORD = "su123456,,"

DATABASE = "calculator"

engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Expression(Base):
    __tablename__ = 'expression'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(String)


class depositRate(Base):
    __tablename__ = 'depositRate'
    id = Column(Integer, primary_key=True)
    time = Column(FLOAT)
    rate = Column(FLOAT)


class loanRate(Base):
    __tablename__ = 'loanRate'
    id = Column(Integer, primary_key=True)
    time = Column(FLOAT)
    rate = Column(FLOAT)


@app.route('/calculateNum', methods=['POST'])
def calculateNum():
    data = request.get_json()
    expression = data['expression']
    re = cal(expression)
    data = {
        'result': re
    }
    re = expression + " = " + str(re)
    new_expression = Expression(content=re)
    session.add(new_expression)
    session.commit()
    return jsonify(data)


@app.route('/calculateRate', methods=['POST'])
def calculateRate():
    data = request.get_json()
    amount = float(data['amount'])
    time = float(data['time'])
    flag = float(data['flag'])
    print(amount)
    print(time)
    print(flag)
    if flag == 0:
        rate = session.query(depositRate) \
            .filter(depositRate.time == 0) \
            .all()
    elif flag == 1:
        rate = 0
        if time <= 0.3:
            session.query(depositRate) \
                .filter(depositRate.time == 0.3) \
                .all()
        elif time <= 0.5:
            rate = session.query(depositRate) \
                .filter(depositRate.time == 0.5) \
                .all()
        elif time <= 1:
            rate = session.query(depositRate) \
                .filter(depositRate.time == 1) \
                .all()
        elif time <= 3:
            rate = session.query(depositRate) \
                .filter(depositRate.time == 3) \
                .all()
        elif time <= 5:
            rate = session.query(depositRate) \
                .filter(depositRate.time == 5) \
                .all()
    else:
        if time < 0.6:
            session.query(loanRate) \
                .filter(loanRate.time == 0.6) \
                .all()
        elif time < 1:
            rate = session.query(loanRate) \
                .filter(loanRate.time == 1) \
                .all()
        elif time < 3:
            rate = session.query(loanRate) \
                .filter(loanRate.time == 3) \
                .all()
        elif time < 5:
            rate = session.query(loanRate) \
                .filter(loanRate.time == 5) \
                .all()
        else:
            rate = session.query(loanRate) \
                .filter(loanRate.time == 6) \
                .all()
    re = rate[0].rate * amount * time / 100
    data = {
        'result': re
    }

    return jsonify(data)


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
    while i < len(temp):
        sub_2 = temp[i:i + 2]
        sub_3 = temp[i:i + 3]
        sub_4 = temp[i:i + 4]
        if (sub_2 == 'ln' or sub_3 == 'sin' or sub_3 == 'cos' \
                or sub_3 == 'tan' or sub_3 == 'sqrt' or sub_3 == 'log' \
                or sub_4 == 'asin' or sub_4 == 'acos' or sub_4 == 'atan' or sub_4 == 'sqrt'):
            le = 0
            if sub_2 == 'ln':
                le = 2
            elif sub_3 == 'sin' or sub_3 == 'cos' or sub_3 == 'tan' or sub_3 == 'sqrt' or sub_3 == 'log':
                le = 3
            elif sub_4 == 'asin' or sub_4 == 'acos' or sub_4 == 'atan' or sub_4 == 'sqrt':
                le = 4
            re = calculate_science(i + le, temp, 1)
            if sub_2 == 'ln':
                temp_val += str(math.log(re[0]))
            elif sub_3 == 'sin':
                temp_val += str(math.sin(re[0] / 180 * math.pi))
            elif sub_3 == 'cos':
                temp_val += str(math.cos(re[0] / 180 * math.pi))
            elif sub_3 == 'tan':
                temp_val += str(math.tan(re[0] / 180 * math.pi))
            elif sub_3 == 'log':
                temp_val += str(math.log10(re[0]))
            elif sub_4 == 'asin':
                temp_val += str(math.asin(re[0]))
            elif sub_4 == 'acos':
                temp_val += str(math.acos(re[0]))
            elif sub_4 == 'atan':
                temp_val += str(math.atan(re[0]))
            elif sub_4 == 'sqrt':
                temp_val += str(math.sqrt(re[0]))
            i = re[1]
        elif temp[i] == '!':
            flag_1 = 0
            temp_val_1 = ""
            for j in range(len(temp_val) - 1, -1, -1):
                if temp_val[j] == '(':
                    if flag_1 > 0:
                        flag_1 -= 1
                    else:
                        temp_val = temp_val[:j + 1] + \
                                   str(factorial_iterative(eval(temp_val_1)))
                        break
                elif temp_val[j] == ')':
                    flag_1 += 1
                temp_val_1 = temp_val[j] + temp_val_1
                if (temp_val[j] < '0' or temp_val[j] > '9' or j == 0) and flag_1 == 0:
                    if j == 0 or temp_val[j] == '(':
                        temp_val = temp_val[:j] + \
                                   str(factorial_iterative(eval(temp_val_1)))
                    else:
                        temp_val = temp_val[:j + 1] + \
                                   str(factorial_iterative(eval(temp_val_1)))
                    break
        elif temp[i] == '^':
            temp_val += '**'
        elif temp[i] == '×':
            temp_val += '*'
        elif temp[i] == '÷':
            temp_val += '/'
        elif temp[i] == 'π':
            temp_val += str(math.pi)
        elif temp[i] == 'e':
            temp_val += str(math.e)
        else:
            if temp[i] == '(':
                flag += 1
            elif temp[i] == ')':
                flag -= 1
            temp_val += temp[i]
            if ((flag == 0 and temp[i] == ')') or i == len(temp) - 1) and (ch == 1):
                return eval(temp_val), i
        i += 1
    return eval(temp_val), len(temp) - 1


def cal(temp):
    re = calculate_science(0, temp, 0)
    result = re[0]
    return result


@app.route('/updateRate', methods=['POST'])
def updateRate():
    data = request.get_json()
    rate = data['rate']
    i = 1
    print(rate)
    while i <= 7:
        rate[i-1]=float(rate[i-1])
        session.query(depositRate).filter(depositRate.id == i).update(
            {depositRate.rate: rate[i-1]})
        session.commit()
        i += 1
    i = 1
    while i <= 5:
        rate[i+6] = float(rate[i+6])
        rate[i+6] = float(rate[i+6])
        session.query(loanRate).filter(loanRate.id == i).update(
            {loanRate.rate: rate[i+6]})
        session.commit()
        i += 1
    return "200"


@app.route('/queryRate', methods=['POST'])
def queryRate():
    data = request.get_json()
    rate = []
    re = session.query(depositRate).all()
    i = 0
    while i < 7:
        rate.append(re[i].rate)
        i += 1
    re = session.query(loanRate).all()
    i = 0
    while i < 5:
        rate.append(re[i].rate)
        i += 1
    print(rate)
    data = {
        'rate': rate
    }
    return jsonify(data)


@app.route('/queryHistory', methods=['POST'])
def queryHistory():
    results = session.query(Expression) \
        .order_by(Expression.id.desc()) \
        .limit(10) \
        .all()
    history = []
    i = 0
    while i < len(results):
        history.append(results[i].content)
        i += 1
    data = {
        'history': history
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
