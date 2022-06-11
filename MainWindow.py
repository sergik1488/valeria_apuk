import tkinter as tki
import tkinter.filedialog as fd
from tkinter.ttk import Treeview
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os.path
import sys

from matplotlib import pyplot as plt
import seaborn as sns

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
        db = pd.read_csv(tabl1[-1], sep=';') \
            .merge(pd.read_csv(tabl2[-1], sep=';'), on='Н_ПРО') \
            .merge(pd.read_csv(tabl3[-1], sep=';'), on='Н_ПРО') \
            .merge(pd.read_csv(tabl4[-1], sep=';'), on='Н_ЖАНР') \
            .drop(columns=['Н_ПРО', 'Н_ЖАНР']).sort_values(by='Н_АКТЁР', ascending=True)
        DataWindow(root, db)

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
            db = pd.read_csv(tabl1[-1], sep=';') \
                .merge(pd.read_csv(tabl2[-1], sep=';'), on='Н_ПРО') \
                .merge(pd.read_csv(tabl3[-1], sep=';'), on='Н_ПРО') \
                .merge(pd.read_csv(tabl4[-1], sep=';'), on='Н_ЖАНР') \
                .drop(columns=['Н_ПРО', 'Н_ЖАНР']).sort_values(by='Н_АКТЁР', ascending=True)
            DataWindow(root, db)

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


def DataWindow(root, db):
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
    to_reports.grid(column=0, row=1, ipadx=81)
    def to_redact():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        RedactWindow(root, db)
    btn_redact = tki.Button(
        root,
        text='Редактировать базу данных',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=to_redact
    )
    btn_redact.grid(column=0, row=2, ipadx=4)
    db = pd.read_csv(tabl1[-1], sep=';') \
        .merge(pd.read_csv(tabl2[-1], sep=';'), on='Н_ПРО') \
        .merge(pd.read_csv(tabl3[-1], sep=';'), on='Н_ПРО') \
        .merge(pd.read_csv(tabl4[-1], sep=';'), on='Н_ЖАНР') \
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
    massstart = [btn, to_reports, verscrlbar, tree, btn_redact]


def Reports(root, db):
    def to_Graphs():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        Graphs(root,db)
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        DataWindow(root, db)

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
    def stats_report(db):
        for i in mas:
            i.grid_remove()
        genre_min = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'min'}) \
            .rename(columns={'СТАЖ': 'Минимальный стаж'})
        genre_max = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'max'}) \
            .rename(columns={'СТАЖ': 'Максимальный стаж'})
        genre_std = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'std'}) \
            .rename(columns={'СТАЖ': 'Стандартное отклонение стажа'})
        genre_median = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'median'}) \
            .rename(columns={'СТАЖ': 'Медиана стажа'})
        genre_full = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'mean'}) \
            .rename(columns={'СТАЖ': 'Средний стаж'}) \
            .merge(genre_max, on='ЖАНР') \
            .merge(genre_min, on='ЖАНР') \
            .merge(genre_std, on='ЖАНР') \
            .merge(genre_median, on='ЖАНР')
        tree3 = Treeview(root)
        db_col = list(genre_full.columns)
        tree3["columns"] = db_col
        tree3['show'] = 'headings'
        mas.append(tree3)
        for i in range(len(db_col)):
            tree3.column(db_col[i], width=15, anchor='c')
            tree3.heading(db_col[i], text=str(db_col[i]))
        for k in range(len(genre_full)):
            tree3.insert("", 'end', values=(list(genre_full.iloc[k])))
        tree3.grid(column=5, row=10, ipadx=200)
    btn_stats = tki.Button(root,
        text='Простая статистика БД',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=lambda:stats_report(db))
    btn_stats.grid(column=1, row=4)
    def opensimple_report():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
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
    generate_pivot.grid(column=1, row=2, ipadx=27)

    def create_pivot(db):
        for i in mas:
            i.grid_remove()
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
        tree2.grid(column=5, row=10, ipadx=200)
        verscrlbar2.grid(column=3, row=10, ipady=86)
        tree2.configure(yscrollcommand=verscrlbar2.set)
        mas.append(tree2)
        mas.append(verscrlbar2)
    to_simple = tki.Button(root,
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='cyan1',
                           fg='black',
                           text='Простой отчёт',
                           command=opensimple_report)
    to_simple.grid(column=1, row=1, ipadx=40)
    Graph_btn = tki.Button(root,
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='cyan1',
                           fg='black',
                           text='К графикам',
                           command=to_Graphs)
    Graph_btn.grid(column=1,row=3, ipadx=50)
    massstart = [btn, generate_pivot, to_simple,Graph_btn, btn_stats]


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
def Graphs(root, db):
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        Reports(root, db)
    btn_back = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    def barplot(db):
        db_for_bar = db.groupby('ФИО', as_index=False) \
            .agg({'ПРОЕКТ': 'count'}) \
            .rename(columns={'ПРОЕКТ': 'Количество проектов'})
        sns.set(rc={'figure.figsize': (9, 5)})
        fig = plt.figure()
        fig.patch.set_facecolor('blue')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('orange')
        ax.patch.set_alpha(1.0)
        sns.barplot(x=db_for_bar['ФИО'], y=db_for_bar['Количество проектов']) \
            .set(title='\nКоличество проектов актёра')
        plt.xticks(rotation=45)
        plt.savefig('graph.png',bbox_inches = 'tight', dpi=70)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
    barplot_btn = tki.Button(root,
        text='Построить Барплот',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=lambda:barplot(db))

    def histplot(db):
        fig = plt.figure()
        fig.patch.set_facecolor('none')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('none')
        ax.patch.set_alpha(1.0)
        sns.histplot(x=db['ПРОЕКТ'], hue=db['ЖАНР']) \
            .set(title='\nКоличество актёров в проекте')
        plt.xticks(rotation=90)
        plt.savefig('graph.png',bbox_inches = 'tight', dpi=70)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
    histplot_btn = tki.Button(root,
                             text='Построить Хистплот',
                             font=(
                                 'Times',
                                 14,
                                 'bold'),
                             background='cyan1',
                             fg='black',
                             command=lambda: histplot(db))
    def boxplot(db):
        fig = plt.figure()
        fig.patch.set_facecolor('none')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('none')
        ax.patch.set_alpha(1.0)
        sns.boxplot(x=db['ЖАНР'], y=db['СТАЖ']) \
            .set(title='\nСтаж актёров по жанрам')
        plt.xticks(rotation=45)
        plt.savefig('graph.png',bbox_inches = 'tight', dpi=70)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
    boxlot_btn = tki.Button(root,
                            text='Построить Боксплот',
                            font=(
                              'Times',
                              14,
                              'bold'),
                            background='cyan1',
                            fg='black',
                            command=lambda: boxplot(db))
    def scatter(db):
        fig = plt.figure()
        fig.patch.set_facecolor('none')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('none')
        ax.patch.set_alpha(1.0)
        sns.scatterplot(x=db['Д.Р.'], y=db['СТАЖ'], hue=db['ПОЛ']) \
            .set(title='\nВзаимосвязь даты рождения и стажа актёров')
        plt.xticks(rotation=45)
        plt.savefig('graph.png', bbox_inches='tight', dpi=70)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
    scatter_btn = tki.Button(root,
                            text='Построить Скаттер-плот',
                            font=(
                                'Times',
                                14,
                                'bold'),
                            background='cyan1',
                            fg='black',
                            command=lambda: scatter(db))
    btn_back.grid(column=0,row=0, ipadx=100)
    barplot_btn.grid(column=0,row=1, ipadx=41)
    histplot_btn.grid(column=0,row=2, ipadx=36)
    boxlot_btn.grid(column=0,row=3, ipadx=36)
    scatter_btn.grid(column=0,row=4, ipadx=18)
    massstart = [btn_back, barplot_btn, histplot_btn, boxlot_btn, scatter_btn]
def RedactWindow(root,db):
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        DataWindow(root, db)
    btn_back = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    tree_edit = Treeview(root)
    db_col = list(db.columns)
    verscrlbar = tki.Scrollbar(root,
                               orient="vertical",
                               command=tree_edit.yview)
    tree_edit["columns"] = db_col
    tree_edit['show'] = 'headings'
    for i in range(len(db_col)):
        tree_edit.column(db_col[i], width=15, anchor='c')
        tree_edit.heading(db_col[i], text=str(db_col[i]))
    for k in range(len(db)):
        tree_edit.insert("", 'end', values=(list(db.iloc[k])))
    tree_edit.grid(column=2, row=10, ipadx=200)
    verscrlbar.grid(column=3, row=10, ipady=86)
    tree_edit.configure(yscrollcommand=verscrlbar.set)
    btn_back.grid(column=0,row=0)
    def delete():
        selected=tree_edit.selection()
        for i in selected:
            tree_edit.delete(i)

    btn_delete = tki.Button(
        root,
        text='Удалить выбранное',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=delete)
    btn_delete.grid(column=1,row=0)
    massstart = [btn_back, btn_delete]
