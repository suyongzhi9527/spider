import webbrowser
import tkinter as tk
import requests
import re

resp = requests.get("http://qmaile.com")
resp.encoding = "utf-8"
text = resp.text
# 数据提取
url = re.compile('<option value="(.*?)" selected="">')
urls = re.findall(url, text)
one = urls[0]
two = urls[1]
three = urls[2]
four = urls[3]
five = urls[4]
six = urls[5]

# 界面
# 画板
root = tk.Tk()
root.title("vip电影播放")
root.geometry('500x250+100+100')
l1 = tk.Label(root, text='播放接口:')
l1.grid()
l2 = tk.Label(root, text='播放链接:')
l2.grid(row=6, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)

var = tk.StringVar()
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=four)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='播放接口5', variable=var, value=five)
r5.grid(row=4, column=1)
r6 = tk.Radiobutton(root, text='播放接口6', variable=var, value=six)
r6.grid(row=5, column=1)


def bf():
    """
    打开浏览器，进入链接
    """
    webbrowser.open(var.get() + t1.get())


b1 = tk.Button(root, text='播放', width=8, command=bf)
b1.grid(row=7, column=1)


def del_text():
    """
    删除文本
    """
    t1.delete(0, 'end')


b2 = tk.Button(root, text='清除', width=8, command=del_text)
b2.grid(row=8, column=1)

# 消息循环
root.mainloop()
