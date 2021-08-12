# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 03:05:20 2021

@author: anna gerd
"""

theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

theBoard2 = {"top-L": " ", "top-M": "X", "top-R": "X",
            "mid-L": "X", "mid-M": "O", "mid-R": "X",
            "low-L": "X", "low-M": " ", "low-R": " "}

#создаем решетку для игры 
def printBoard(board):
    print("|" + board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"] + "|")
    print("--+-+-+")
    print("|" + board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"] + "|")
    print("--+-+-+")
    print("|" + board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"] + "|")

printBoard(theBoard)
b = "O"

#проверка победы: если какой-то ответ (Х или О) встречается 3 раза, то это победа
def checkWin(board, answer):
    board = list(board.values())
    i = 0
    #проверка по строкам решетки
    for o in range(3): 
        #используем функцию join для превращения списка в строку с разделителем
        if answer*3 in "".join(board[i:i+3]): #формируем массив, начиная с i элемента
        #и заканчивая i+3, чтобы избежать ошибки считывания результата между двух строк
            return True
        i += 3 #увеличиваем значение i
    
    #проверка по столбцам решетки
    for o in range(3):
        #делаем то же самое, но для массива из каждого 3-го элемента
        if answer*3 in "".join(board[o::3]): 
            return True
    
    #по диагоналям указываем координаты диагоналей 
    if answer*3 in board[0] + board[4] + board[8] or answer*3 in board[2] + board[4] + board[6]:
        return True
    return False


#назначает ход Х и О и проверяет корректность назначения клетки
def check(a, theAnswer):
    global b #ссылка на глобальную переменную со значением Х или О
    #если клетка хода соответствует координатам и не заполнено 
    if a in theBoard.keys() and a not in theAnswer:
        #ответ заполняет клеточку
        theBoard[a] = b
        #выводим решетку с заполненной клеткой
        printBoard(theBoard)
        #заполняем список ответов совершенным ходом
        theAnswer.append(a)
        #проверяем победу на каждом шаге
        if checkWin(theBoard, b): 
            print("You are a winner!")
            return True
        #создаем последовательность ходов Х и О
        if b == "X":
            b = "O"
        else:
            b = "X"
    #если клетка занята другим ответом или ее название некорректно 
    else:
        print("Error. Please try again.")
        a = input("Move on which space? ")
        check(a, theAnswer)
        
        
#назначение места хода       
def inputData():
    #создаем список для записи ходов
    theAnswer = []
    #цикл из 9 ходов
    for i in range(9):
        #место хода вводит игрок
        a = input("Move on which space? ")
        #если место выбрано корректно, игра продолжается
        if check(a, theAnswer):
            break
            return
inputData()
# print(checkWin(theBoard2, "X"))