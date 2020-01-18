import tkinter as tk

app = tk.Tk()  # 实例化
app.title("Tkinter编程")  # 设置标题栏
the_label = tk.Label(app, text='第一个窗口程序!')  # 显示文本，图标，图片
the_label.pack()  # 自动调节主键的尺寸和位置
app.mainloop()  # 窗口的主设键循环
