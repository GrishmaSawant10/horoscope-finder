from tkinter import*
from tkinter import messagebox
from tkinter import Scrollbar,Text
import requests
from tkinter import filedialog
from datetime import datetime
import pytz

india = pytz.timezone("Asia/Kolkata")
today = datetime.now(india).strftime("%b %d, %Y")

root=Tk()
root.title ("Know Your Horoscope By Grishma Sawant")
root.geometry("1000x700+95+10")
f=("TIMES NEW ROMAN",30,"bold")
F=("TIMES NEW ROMAN",15,)

def horoscope():
	sign = ent_sign.get().strip().lower()
	if sign not in ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo','libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']:
		messagebox.showerror("Error", "Please enter a valid zodiac sign")
		return
	try:
		url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day=today"
		res = requests.get(url)
		if res.status_code != 200:
			messagebox.showerror("Error", f"API returned status code {res.status_code}")
			return
		data = res.json()
		date = data["data"]["date"]
		horoscope = data["data"]["horoscope_data"]
		msg = f"Date: {today}\n\n{horoscope}"
		txt_horoscope.delete(1.0, END)   # clear previous text
		txt_horoscope.insert(END, msg)   # insert new horoscope

	except Exception as e:
		messagebox.showerror("Error", f"Failed to fetch horoscope: {e}")

def clear_text():
	txt_horoscope.delete(1.0, END)

def save_text():
	content = txt_horoscope.get(1.0, END).strip()
	if not content:
		messagebox.showerror("Error", "No horoscope to save!")
		return

	# Ask user where to save
	file_path = filedialog.asksaveasfilename(defaultextension=".txt",
	                                         filetypes=[("Text files", "*.txt")])
	if file_path:
		with open(file_path, "w", encoding="utf-8") as file:
			file.write(content)
		messagebox.showinfo("Saved", "Horoscope saved successfully!")



lab_header= Label(root,bg='orange',text=" Wanna Know Your Horoscope? ",font=f, anchor='center')
lab_header.place(x=220,y=50)

lab_ent= Label(root,bg='yellow',text=" Enter Your Zodiac Sign!!! ",font=f, anchor='center')
lab_ent.place(x=265,y=135)
ent_sign=Entry(root,font=f)
ent_sign.place(x=300,y=221)


btn_submit=Button(root,text="Show Horoscope",font=f,width=12,anchor='center',command=horoscope)
btn_submit.place(x=360,y=300)

text_frame = Frame(root)
text_frame.place(x=190, y=400)

scroll = Scrollbar(text_frame, orient='vertical')
scroll.pack(side=RIGHT, fill=Y)

txt_horoscope = Text(text_frame, wrap='word', font=F,width=60, height=8, yscrollcommand=scroll.set)
txt_horoscope.pack()

scroll.config(command=txt_horoscope.yview)

btn_clear = Button(root, text="Clear", font=("Times New Roman", 18, "bold"), command=clear_text, bg="lightcoral")
btn_clear.place(x=220, y=610)

btn_save = Button(root, text="Save Horoscope", font=("Times New Roman", 18, "bold"), command=save_text, bg="lightgreen")
btn_save.place(x=580, y=610)



root.mainloop()