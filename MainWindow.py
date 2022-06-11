import tkinter as tki
import tkinter.filedialog as fd
from tkinter.ttk import Treeview

import pandas as pd
import numpy as np
import os.path
import sys
from functools import partial

massstart = []
mas = []

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


tabl1 = []
tabl2 = []
tabl3 = []
tabl4 = []


def MainWind(root):
    def newwin():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        tabl1.append("tabl1.csv")
        tabl2.append("tabl2.csv")
        tabl3.append("tabl3.csv")
        tabl4.append("tabl4.csv")
        DataWindow(root, tabl1[-1], tabl2[-1], tabl3[-1], tabl4[-1])

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        start(root)

    def newwinifopened():
        if tabl1 == [] or tabl2 == [] or tabl3 == [] or tabl4 == []:
            print("Ещё не всё")
        else:
            for i in massstart:
                if i.winfo_viewable():
                    i.grid_remove()
                else:
                    i.grid()
            DataWindow(root, tabl1[-1], tabl2[-1], tabl3[-1], tabl4[-1])

    def choose_file():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl1.append(filename)

    def choose_file2():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl2.append(filename)

    def choose_file3():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl3.append(filename)

    def choose_file4():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl4.append(filename)

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

    btnchoose1.grid(column=0, row=1, pady=40, ipadx=18)
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
    btnchoose2.grid(column=0, row=2, pady=40, ipadx=88)
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
    btnchoose3.grid(column=0, row=3, pady=40, ipadx=62)
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
    btnchoose4.grid(column=0, row=4, pady=40, ipadx=96)
    btnusingready = tki.Button(
        root,
        text='Использовать готовую БД',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=newwin)
    btnusingready.grid(column=1, row=2, pady=40)
    btnusingready1 = tki.Button(
        root,
        text='Создать свою БД',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=newwinifopened)
    btnusingready1.grid(column=1, row=3, pady=40, ipadx=40)

    massstart = [btn, btnchoose1, lbl1, btnchoose2, btnchoose3, btnchoose4, btnusingready, btnusingready1]


def DataWindow(root, tabl1, tabl2, tabl3, tabl4):
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        MainWind(root)

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

    def to_window_report():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        Reports(root, db)

    to_reports = tki.Button(root,
                            text='К отчётам',
                            font=(
                                'Times',
                                14,
                                'bold'),
                            background='cyan1',
                            fg='black',
                            command=to_window_report)
    to_reports.grid(column=0, row=1, ipadx=80)

    db = pd.read_csv(tabl1, sep=';') \
        .merge(pd.read_csv(tabl2, sep=';'), on='Н_ПРО') \
        .merge(pd.read_csv(tabl3, sep=';'), on='Н_ПРО') \
        .merge(pd.read_csv(tabl4, sep=';'), on='Н_ЖАНР') \
        .drop(columns=['Н_ПРО', 'Н_ЖАНР']).sort_values(by='Н_АКТЁР', ascending=True)
    tree = Treeview(root)
    db_col = list(db.columns)
    verscrlbar = tki.Scrollbar(root,
                               orient="vertical",
                               command=tree.yview)
    tree["columns"] = db_col
    tree['show'] = 'headings'
    for i in range(len(db_col)):
        tree.column(db_col[i], width=15, anchor='c')
        tree.heading(db_col[i], text=str(db_col[i]))
    for k in range(len(db)):
        tree.insert("", 'end', values=(list(db.iloc[k])))
    tree.grid(column=2, row=10, ipadx=200)
    verscrlbar.grid(column=3, row=10, ipady=86)
    tree.configure(yscrollcommand=verscrlbar.set)
    massstart = [btn, to_reports, verscrlbar, tree]


def Reports(root, db):
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        DataWindow(root, tabl1[-1], tabl2[-1], tabl3[-1], tabl4[-1])

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

    def opensimple_report():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        simple_report(root, db)

    generate_pivot = tki.Button(root,
                                text="Сводная таблица",
                                font=(
                                    'Times',
                                    14,
                                    'bold'),
                                background='cyan1',
                                fg='black',
                                command=lambda: create_pivot(db))
    generate_pivot.grid(column=53, row=44)

    def create_pivot(db):

        pivot = db.groupby(['ФИО', 'ЖАНР'], as_index=False) \
            .agg({'ПРОЕКТ': 'count'}) \
            .pivot('ФИО', 'ЖАНР', 'ПРОЕКТ') \
            .fillna(0) \
            .reset_index()
        tree2 = Treeview(root)
        db_col = list(pivot.columns)
        verscrlbar2 = tki.Scrollbar(root,
                                    orient="vertical",
                                    command=tree2.yview)
        tree2["columns"] = db_col
        tree2['show'] = 'headings'
        for i in range(len(db_col)):
            tree2.column(db_col[i], width=15, anchor='c')
            tree2.heading(db_col[i], text=str(db_col[i]))
        for k in range(len(pivot)):
            tree2.insert("", 'end', values=(list(pivot.iloc[k])))
        tree2.grid(column=2, row=10, ipadx=200)
        verscrlbar2.grid(column=3, row=10, ipady=86)
        tree2.configure(yscrollcommand=verscrlbar2.set)

    to_simple = tki.Button(root,
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='cyan1',
                           fg='black',
                           text='Простой отчёт',
                           command=opensimple_report)
    to_simple.grid(column=50, row=44, pady=40)
    massstart = [generate_pivot, to_simple]


def simple_report(root, db):
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        Reports(root, db)

    def clean(db):
        for i in mas:
            i.grid_remove()
        search_simple(db)
    def search_simple(db=None):
        tree3 = Treeview(root)
        verscrlbar2 = tki.Scrollbar(root,
                                    orient="vertical",
                                    command=tree3.yview)
        mas.append(tree3)
        mas.append(verscrlbar2)
        Needed_columns = ['Н_АКТЁР']
        if bolcb2.get() == True:
            Needed_columns.append(cb2.cget('text'))
        if bolcb3.get() == True:
            Needed_columns.append(cb3.cget('text'))
        if bolcb4.get() == True:
            Needed_columns.append(cb4.cget('text'))
        if bolcb5.get() == True:
            Needed_columns.append(cb5.cget('text'))
        if bolcb6.get() == True:
            Needed_columns.append(cb6.cget('text'))
        if bolcb7.get() == True:
            Needed_columns.append(cb7.cget('text'))


        db_simple = db[Needed_columns]

        db_col = list(db_simple.columns)
        tree3["columns"] = db_col
        tree3['show'] = 'headings'
        for i in range(len(db_col)):
            tree3.column(db_col[i], width=50, anchor='c', stretch=False)
            tree3.heading(db_col[i], text=str(db_col[i]))
        for k in range(len(db_simple)):

            tree3.insert("", 'end', values=(list(db_simple.iloc[k])))
        tree3.grid(column=2, row=10)
        verscrlbar2.grid(column=3, row=10, ipady=86)
        tree3.configure(yscrollcommand=verscrlbar2.set)

    bolcb2 = tki.BooleanVar()
    cb2 = tki.Checkbutton(text="ФИО", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb2)
    bolcb3 = tki.BooleanVar()
    cb3 = tki.Checkbutton(text="Д.Р.", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb3)
    bolcb4 = tki.BooleanVar()
    cb4 = tki.Checkbutton(text="ПОЛ", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb4)
    bolcb5 = tki.BooleanVar()
    cb5 = tki.Checkbutton(text="СТАЖ", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb5)
    bolcb6 = tki.BooleanVar()
    cb6 = tki.Checkbutton(text="ПРОЕКТ", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb6)
    bolcb7 = tki.BooleanVar()
    cb7 = tki.Checkbutton(text="ЖАНР", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb7)
    cb2.grid(column=0, row=2, sticky='W')
    cb3.grid(column=0, row=3, sticky='W')
    cb4.grid(column=0, row=4, sticky='W')
    cb5.grid(column=0, row=5, sticky='W')
    cb6.grid(column=0, row=6, sticky='W')
    cb7.grid(column=0, row=7, sticky='W')

    search = tki.Button(root,
                        text="Искать",
                        font=(
                            'Times',
                            14,
                            'bold'),
                        background='cyan1',
                        fg='black',
                        command=lambda: clean(db))
    search.grid(column=1, row=1)
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
    massstart = [btn, search, cb5, cb6, cb7, cb4, cb3, cb2]
