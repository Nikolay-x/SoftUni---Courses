from tkinter import *

from canvas import tk
from helpers import clean_screen


def render_products():
    clean_screen()
    Label(tk, text="Welcome to products screen").grid(row=3, column=3)
