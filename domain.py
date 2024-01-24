import tkinter as tk
from tkinter import scrolledtext
import requests

def domain_lookup(api_key, domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {"APIKEY": api_key}
    response = requests.get(url, headers=headers)
    return response.json()
    
def show():
    url = entry.get()
    api_key = 'API_KEY' #Register with SecurityTrails API and paste your API Key Here
    res = domain_lookup(api_key, url)
    
    if "Error : " in res:
        result.config(state=tk.NORMAL)
        result.delete(1.0,tk.END)
        result.insert(tk.END ,res)
        result.config(state=tk.DISABLED)
    else:
        result.config(state=tk.NORMAL)
        result.delete(1.0,tk.END)
        result.insert(tk.END, f"Details of {url} : \n\n{res}")
        result.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Domain Lookup")

root.geometry("530x750")
root.resizable(False,False)
root.configure(bg="blue")

custom_font = ("Monotype Corsiva",12)
label = tk.Label(root , text="Enter Your Domain",font = custom_font)
label.grid(row = 0, column= 1, padx = 15 , pady = 15)

entry = tk.Entry(root, width=40)
entry.grid(row=1 ,column=1 ,padx=15 ,pady=15)

button = tk.Button(root, text="Get HTML Source",font = custom_font , command=show)
button.grid(row=2, column=1, padx=15, pady=15)

result = scrolledtext.ScrolledText(root, wrap=tk.WORD , width = 60, height =35)
result.grid(row=3,column=1,padx =15 ,pady =15)
result.config(state=tk.DISABLED)

root.mainloop()