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

def run_button_click():
    #入力バリデーション
    
    #取得
    challenge_num = float(ntry_entry.get())
    default_probability = float(prob_entry.get())
    
    #確率計算
    result_prob =  calc_probability(challenge_num,default_probability)
    result_entry.insert(0, str(result_prob) + u"%")
    
    
def calc_probability(num, probability):
    all_false_prob = np.power(((100.0 - probability) / 100.0), num)
    result = math.floor((1.0 - all_false_prob) * 100)
    return result

all_false_prob = np.power(((100.0 - PROBABILITY) / 100.0),CHALLENGE_NUM)
result = math.floor((1.0 - all_false_prob) * 100)
print(str(result) + u"%")

root = tk.Tk()
root.title(u"確率シミュレータ")
root.geometry("600x400")

header_label = tk.Label(text=u"N回チャレンジするまでに成功する確率")
header_label.pack()

ntry_label = tk.Label(text=u"N : ")
ntry_label.pack()
ntry_entry = tk.Entry()
ntry_entry.pack()

prob_label = tk.Label(text=u"初期確率 : ")
prob_label.pack()
prob_entry = tk.Entry()
prob_entry.pack()

#ボタン
run_button = ｔｋ.Button(text=u"実行", width = 20,height = 1, command = run_button_click)
run_button.pack()

#結果
result_label = tk.Label(text=u"結果 : ")
result_label.pack()
result_entry = tk.Entry()
result_entry.pack()

# ウインドウ状態の維持
root.mainloop() 

