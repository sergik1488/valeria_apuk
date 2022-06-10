import tkinter as tki
import pandas as pd
import numpy as np
import os.path
import sys
import MainWindow as mw

def Main():
    root = tki.Tk()
    root.geometry("1280x720")
    root.title("Project Sem")
    mw.start(root)
    root.mainloop()
    sys.exit()
if __name__ == '__main__':
    Main()
