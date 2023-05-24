import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
import tkinter as tk
from tkinter import ttk
from datetime import date

localtime = date.today()
localtime = localtime.strftime("%d/%m/%Y")

df = pd.read_csv("C:\world_pop.csv")
df_country = df["country"].tolist()

# Creating tkinter window
window = tk.Tk()
window.geometry('400x120')
window.title("Population graph                           "+localtime)
# Label
ttk.Label(window, text="Select the Country :", font=("Times New Roman", 10)).grid(column=0, row=0, padx=10, pady=25)
n = tk.StringVar()
countrychoosen = ttk.Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
countrychoosen['values'] = df_country
countrychoosen.grid(column=1, row=0)

# Shows default value
countrychoosen.current(1)
# country = countrychoosen.get()

def clicked():
    plt.close()
    country = countrychoosen.get()
    df = pd.read_csv("C:\world_pop.csv")
    df = df.loc[df["country"] == country]
    df = df.iloc[:, 2:]
    number = df.index.values.astype(int)[0]
    df.columns = df.columns.str.replace('year_', '')
    df = df.convert_dtypes()
    plt.figure(figsize=(10, 6))
    plt.title(country+" Population 1960-2020")
    plt.ticklabel_format(useOffset=False, style='plain')
    ax = df.loc[number].plot(kind="line")
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    plt.xticks(rotation=35)
    plt.xlabel("years")
    plt.ylabel("population")
    plt.show()

btn = ttk.Button(window, text="Plot", command=clicked)
btn.grid(column=0, row=1, columnspan=2)
window.mainloop()
