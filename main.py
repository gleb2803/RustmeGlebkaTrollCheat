import tkinter
from tkinter import ttk
import psutil


#   Задаём переменые
inject = False
espOn = False
aimBotOn = False
tracersOn = False
antiKnockBackOn = False
freeCamOn = False

#   Создаём фунции
def TestIfRustmeRun():
    global inject
    global espOn
    global aimBotOn
    global tracersOn
    global antiKnockBackOn
    global freeCamOn
    if inject:
        inject = False
        espOn = False
        aimBotOn = False
        tracersOn = False
        antiKnockBackOn = False
        freeCamOn = False
        injectbtn.configure(text="not injected")
        espbtn.configure(text="esp off")
        aimbotbtn.configure(text="aimBot off")
        trasersbtn.configure(text="tracers off")
        AKBbtn.configure(text="antiKnockBack off")
        FCbtn.configure(text="freeCam off")

        return
    for proc in psutil.process_iter():
        name = proc.name()
        print(name)
        if name == "javaw.exe":
            StatusLab.configure(text="")
            injectbtn.configure(text="injected")
            inject = True
            return
    StatusLab.configure(text="Rustme not run")

def donate():
    webbrowser.open("https://www.donationalerts.com/r/gleb2803",new=0,autoraise=True)

def esp():
    if not inject:
        return
    global espOn
    if espOn:
        espbtn.configure(text="esp off")
        espOn = False
        return
    espbtn.configure(text="esp on")
    espOn = True
    return

def aimBot():
    if not inject:
        return
    global aimBotOn
    if aimBotOn:
        aimbotbtn.configure(text="aimBot off")
        aimBotOn = False
        return
    aimbotbtn.configure(text="aimBot on")
    aimBotOn = True
    return

def trasers():
    if not inject:
        return
    global tracersOn
    if tracersOn:
        trasersbtn.configure(text="tracers off")
        tracersOn = False
        return
    trasersbtn.configure(text="tracers on")
    tracersOn = True
    return

def akb():
    if not inject:
        return
    global antiKnockBackOn
    if antiKnockBackOn:
        AKBbtn.configure(text="antiKnockBack off")
        antiKnockBackOn = False
        return
    AKBbtn.configure(text="antiKnockBack on")
    antiKnockBackOn = True
    return

def freeCam():
    if not inject:
        return
    global freeCamOn
    if freeCamOn:
        FCbtn.configure(text="freeCam off")
        freeCamOn = False
        return
    FCbtn.configure(text="freeCam on")
    freeCamOn = True
    return

def settings():
    settingsRoot = tkinter.Tk()



    settingsRoot.mainloop()

def rickroll():
    memeRoot = tkinter.Tk()

    memeRoot.geometry("640x480")
    memeRoot.title("Rickroll")

    memeRoot.mainloop()


#   Создаём окно
root = tkinter.Tk()

#   Задаём настройки
root.geometry("320x240")
root.title("RGTC")
root.resizable(False, False)
root.iconbitmap('skeleton.ico')

#   Создаём кнопки
espbtn = ttk.Button(text="esp off", width=50, command=esp)
aimbotbtn = ttk.Button(text="aimBot off", width=50, command=aimBot)
trasersbtn = ttk.Button(text="tracers off", width=50, command=trasers)
AKBbtn = ttk.Button(text="antiKnockBack off", width=50, command=akb)
FCbtn = ttk.Button(text="freeCam off", width=50, command=freeCam)
injectbtn = ttk.Button(text="not injected",width=50,command=TestIfRustmeRun)
SettingsBtn = ttk.Button(text="Settings",width=50, command=settings)
donateBtn = ttk.Button(text="Donate", width=50, command=donate)

#   Создаём табличку статуса
StatusLab = ttk.Label(font=("Arial", 24),foreground="red")

#   Пакуем все
espbtn.pack()
aimbotbtn.pack()
trasersbtn.pack()
AKBbtn.pack()
FCbtn.pack()
injectbtn.pack()
StatusLab.pack()
donateBtn.pack()
SettingsBtn.pack()

#   Запускаем основной цикл
root.mainloop()