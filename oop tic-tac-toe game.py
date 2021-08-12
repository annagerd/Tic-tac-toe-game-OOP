# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 05:24:10 2021

@author: anna gerd
"""

class Board:
    
    def __init__(self):
        
        self.board = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}
    
    def __str__(self):
        
        return str("|" + self.board["top-L"] + "|" + self.board["top-M"] 
                   + "|" + self.board["top-R"] + "|" + "\n" + "--+-+-+" + "\n"
                   + "|" + self.board["mid-L"] + "|" + self.board["mid-M"] + "|" 
                   + self.board["mid-R"] + "|" + "\n" + "--+-+-+" + "\n" 
                   + "|" + self.board["low-L"] + "|" + self.board["low-M"] + "|" 
                   + self.board["low-R"] + "|") 

class BoardGame(Board):
    
    def __init__(self):
        Board.__init__(self)
        self.b = "O"
        
    
    def checkWin(self):
        
        checkBoard = list(self.board.values())
        i = 0
        for o in range(3):
            if self.b*3 in "".join(checkBoard[i:i+3]):
                return True
            i += 3
            
        for o in range(3):
            if self.b*3 in "".join(checkBoard[o::3]):
                return True

        if self.b*3 in checkBoard[0] + checkBoard[4] + checkBoard[8] or self.b*3 in checkBoard[2] + checkBoard[4] + checkBoard[6]:
            return True
        return False
    
    def turn(self, a, theAnswer):
        if a in self.board.keys() and a not in theAnswer:
            self.board[a] = self.b
            print(self)
            theAnswer.append(a)
            if self.checkWin():
                print("You are a winner!")
                return True
            
            if self.b == "X":
                self.b = "O"
            else:
                self.b = "X"
        else: 
            print("Error. Please try again.")
            a = input("Move on which space? ")
            self.turn(a, theAnswer)
        
    def inputData(self):
        theAnswer= []
        for i in range(9):
            a = input("Move on which space? ")
            if self.turn(a, theAnswer):
                break
                return
                       
krestiki = BoardGame()
krestiki.inputData()

