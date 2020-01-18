import tkinter as tk


class APP(object):
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.hi_there = tk.Button(frame, text='测试', fg='blue', command=self.say_ceshi())
        self.hi_there.pack()

    def say_ceshi(self):
        print("GUI编程测试")


st = tk.Tk()
app = APP(st)
st.mainloop()
