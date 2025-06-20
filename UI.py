from customtkinter import CTk, CTkButton, CTkLabel, CTkTextbox, CTkFrame, CTkCheckBox
from data_man import DataManager

app = CTk()
app.title("Student Course Manager")
app.geometry("800x500")

mn_frm = CTkFrame(app, width=800, height=500)
mn_frm.pack(fill="both", expand=True)

title_label = CTkLabel(mn_frm, text="Student Course Manager", font=("Oswald", 36))
title_label.pack(pady=20)

chk = CTkCheckBox(mn_frm, text="Input Data", font=("Oswald", 16), hover_color='#6c6a6a', fg_color='#6c6a6a')
chk.pack(pady=10)

entry = CTkTextbox(mn_frm, border_color='#b8b6b6', border_width=2, width=400, height=100)
entry.pack(pady=30)

dm = DataManager(entry.get("1.0", "end-1c"), chk.get())

submit_btn = CTkButton(mn_frm, text="Submit", font=("Oswald", 16), command=dm.add_course)
submit_btn.pack(pady=10)

app.mainloop()