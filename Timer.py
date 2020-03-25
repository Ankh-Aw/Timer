# coding: utf-8

import tkinter as tk
from tkinter import messagebox
import time
#import winsound

class Timer(tk.Frame):
    WID = 10
    countPushStartButton = 0

    def __init__(self,master = None):
        tk.Frame.__init__(self,master)

        self.master.title('集中力タイマー')

        #単位表記
        minute = tk.Label(self, text = u'分',font = 'Arial, 12', padx = 5, pady = 5)
        second = tk.Label(self, text = u'秒',font = 'Arial, 12', padx = 5, pady = 5)

        #スピンボックス
        self.minuteSpinbox = tk.Spinbox(self, value = 60, from_ = 0, to = 99, increment = 1, width = Timer.WID)
        self.secondSpinbox = tk.Spinbox(self, from_ = 0, to = 59, increment = 1, width = Timer.WID)

        #残り時間表示
        self.countDownView = tk.Label(self,text = u'00:00',font = 'Arial, 25')

        #押ボタン
        self.startButton = tk.Button(self,text = 'Start',command = self.start)
        resetButton = tk.Button(self,text = 'Reset', command = self.reset)

        #ウィジェット配置
        self.minuteSpinbox.grid(row = 0, column = 0, padx = 5, pady = 2)
        minute.grid(row = 0, column =1, padx =5, pady = 2, sticky = tk.W)
        self.secondSpinbox.grid(row = 0, column = 2, padx = 5, pady = 2)
        second.grid(row = 0, column = 3, padx = 5, pady = 2, sticky = tk.W)
        self.startButton.grid(row =1,column = 0, columnspan = 4,padx = 5, pady = 2, sticky = tk.W + tk.E)
        resetButton.grid(row =2, column = 0, columnspan = 4,padx =5, pady = 2, sticky = tk.W + tk.E)

        self.countDownView.grid(row = 3, column = 0, columnspan = 4, padx = 5, pady = 2, sticky = tk.W + tk.E)

    #startボタン押下時動作
    def start(self):
        self.getSpinboxValue()
        self.controlStartButton()
        self.count()

    #resetボタン押下時動作
    def reset(self):
        self.startButton.config(text = 'Start')
        self.countDownView.config(text = '00:00')
        Timer.countPushStartButton = 0

    #Startボタンを押した回数によって動作を変える（初回「Start」、奇数「Stop」、偶数「Restart」）
    def controlStartButton(self):
        if Timer.countPushStartButton == 0:
            self.finishTime = time.time() + self.secondsValue
            self.isStarted = True
        elif Timer.countPushStartButton % 2 == 0:
            self.isStarted = True
        else:
            self.isStarted = False
        Timer.countPushStartButton = Timer.countPushStartButton + 1
        self.refreshStartButton()
    
    #Startボタン押下回数によってボタン表示を変える
    def refreshStartButton(self):
        if self.isStarted is True:
            self.startButton.config(text = 'Stop')
        else:
            self.startButton.config(text = 'Restart')

    #カウントダウン機能
    def count(self):
        if self.isStarted:
            self.remainingTime = self.finishTime - time.time()
            if self.remainingTime < 0:
                self.countDownView.config(text = "時間です")
                messagebox.showinfo('お知らせ','時間です',geometry = "500x400")                
                #アラーム音を鳴らす
                #winsound.PlaySound("SystemAsterisk",winsound.SND_ALIAS)
                
            else:
                self.countDownView.config(text = '%02d:%02d'%(self.remainingTime/60,self.remainingTime%60))    
                #0.1秒後に関数countを呼び出す
                self.after(100, self.count)

    #単位変換
    def getSpinboxValue(self):
        minuteSpinboxValue = self.minuteSpinbox.get()
        secondSpinboxValue = self.secondSpinbox.get()
        c1 = int(minuteSpinboxValue)
        c2 = int(secondSpinboxValue)
        self.secondsValue = c1 * 60 + c2

if __name__ == '__main__':
    f = Timer()
    f.pack()
    f.mainloop()
