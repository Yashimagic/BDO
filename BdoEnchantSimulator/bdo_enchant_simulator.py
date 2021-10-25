# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:55:32 2017

@author: YSM
"""

import numpy as np
import math
import tkinter as tk

CHALLENGE_NUM = 10
PROBABILITY = 10 #percent


all_false_prob = np.power(((100.0 - PROBABILITY) / 100.0),CHALLENGE_NUM)
result = math.floor((1.0 - all_false_prob) * 100)
print(str(result) + u"%")

root = tk.Tk()
root.title(u"確率シミュレータ")
root.geometry("600x400")

#ラベル
ntry_label = tk.Label(text=u'N回チャレンジするまでに成功する確率')
ntry_label.pack()
ntry_label = tk.Label(text=u'N:')
ntry_label.pack()

#エントリー
EditBox = tk.Entry()
EditBox.pack()

#ボタン
run_button = ｔｋ.Button(text=u'実行', width = 20,height = 10)
run_button.pack()
# ウインドウ状態の維持
root.mainloop() 