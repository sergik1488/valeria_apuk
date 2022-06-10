import tkinter as tki
import pandas as pd
import numpy as np
import os.path
import sys



def start(root):
    lbl1 = tki.Label(
        root,
        text="Нажмите старт для работы с БВ",
        font=(
            'Times',
            24,
            'bold'))
    lbl1.grid(column=1, row=0, pady=100, padx=80)
    btn = tki.Button(
        root,
        text='Старт',
        font=(
            'Colibry',
            14,
            'bold'),
        bg='white',
        fg='black')
    btn.grid(column=1, row=1)
    mass = [lbl1, btn]