from tkinter import *

root = Tk()  # 初始化TK

# 创建label,labe2......
labe1 = Label(root, bitmap='error')
labe2 = Label(root, bitmap='hourglass')
labe3 = Label(root, bitmap='info')
labe4 = Label(root, bitmap='questhead')
labe5 = Label(root, bitmap='question')
labe6 = Label(root, bitmap='warning')
labe7 = Label(root, bitmap='gray12')
labe8 = Label(root, bitmap='gray25')
labe9 = Label(root, bitmap='gray50')
labe10 = Label(root, bitmap='gray75')


# 显示label
for i in range(1, 11):  # 循环显示labe1,labe2...
    ss = 'labe' + str(i)
    eval(ss).pack()  # eval去除左右两边引号,得到真正的数据类型


# 进入消息循环
root.mainloop()