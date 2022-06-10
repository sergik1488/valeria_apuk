import tkinter as tki
import tkinter.filedialog as fd
import pandas as pd
import numpy as np
import os.path
import sys
from PIL import Image, ImageTk

massstart = []


def start(root):
    def opennextwindov():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        MainWind(root)

    root["bg"] = "SkyBlue1"
    lbl1 = tki.Label(
        root,
        text="Нажмите старт для работы с БД",
        font=(
            'Times',
            24,
            'bold'),
        bg='SkyBlue1')
    lbl1.grid(column=1, row=0, pady=100, padx=400)
    btn = tki.Button(
        root,
        text='Старт',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=opennextwindov)
    btn.grid(column=1, row=1)
    massstart = [lbl1, btn]


def MainWind(root):

    tabl1 = None
    tabl2 = None
    tabl3 = None
    tabl4 = None
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        start(root)

    def choose_file():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",filetypes=(("CSV файл", "*.csv"),))
        tabl1 = filename

    def choose_file2():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",filetypes=(("CSV файл", "*.csv"),))
        tabl2 = filename
    def choose_file3():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",filetypes=(("CSV файл", "*.csv"),))
        tabl3 = filename
    def choose_file4():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",filetypes=(("CSV файл", "*.csv"),))
        tabl14 = filename


    btn = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    btn.grid(column=0, row=0, ipadx=100)



    lbl1 = tki.Label(
        root,
        text="Используйте готовую или загрузите по отдельности БД",
        font=(
            'Times',
            24,
            'bold'),
        bg='SkyBlue1')
    lbl1.grid(column=1, row=0, padx=100)
    btnchoose1 = tki.Button(
        root,
        text='Выбрать личные данные',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file)
    btnchoose1.grid(column=0, row=1, pady=40)
    btnchoose2 = tki.Button(
        root,
        text='Проекты',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file2)
    btnchoose2.grid(column=0, row=2, pady=40)
    btnchoose3 = tki.Button(
        root,
        text='Номер проекта',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file3)
    btnchoose3.grid(column=0, row=3, pady=40)
    btnchoose4 = tki.Button(
        root,
        text='Жанры',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file4)
    btnchoose4.grid(column=0, row=4, pady=40)
    massstart = [btn, btnchoose1, lbl1, btnchoose2, btnchoose3, btnchoose4]
