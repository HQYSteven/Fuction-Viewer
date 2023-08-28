import tkinter
from tkinter import ttk


class fuctionViewer(tkinter.Frame):
    def __init__(self):
        self.realx = -25
        self.a = 0
        self.b = 0
        self.h = 0
        self.k = 0
        self.x = -1100
        self.modelType = 0
        self.max = 1100
        self.minu = -1100
        self.root = tkinter.Tk()
        self.screen = tkinter.Frame(self.root, width=300, height=300)
        self.root.title("Fuction Viewer")
        self.screen.pack()
        self.bloodDock = tkinter.Frame(self.root)
        self.bloodDock.pack(side="bottom")
        bar = tkinter.Scrollbar(self.screen, relief="flat")
        bar.pack(fill="both", side="right")
        hbar = tkinter.Scrollbar(self.screen, orient="horizontal",
                                 )
        self.canvas = tkinter.Canvas(self.screen,
                                     confine=False,
                                     xscrollincrement=50,
                                     yscrollincrement=50,
                                     width=500,
                                     bg='white', cursor="cross",
                                     height=500,
                                     yscrollcommand=bar.set,
                                     xscrollcommand=hbar.set)
        hbar.config(command=self.canvas.xview)
        hbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="right")
        self.canvas.create_line(0, 250, 500, 250)
        self.canvas.create_line(250, -500, 250, 500)
        tkinter.Button(self.bloodDock, text="OK", relief="flat",
                       command=lambda: fuctionViewer.edit_callbak(self)).pack(side="right")
        self.combe = ttk.Combobox(self.bloodDock, values=[
            "y = ax+b", "y = a(x+h)^2 + k", 'y = ax^2 + bx +k'])
        self.combe.pack(side="right")
        bar.config(command=self.canvas.yview)
        startButtton = tkinter.Button(self.bloodDock, text='Start',
                                      command=lambda: fuctionViewer.
                                      view(self, self.x), relief="flat")
        addButton_x = tkinter.Button(
            self.bloodDock, text='+', relief="flat", command=lambda: fuctionViewer.add(self, 0))
        self.xLabel = tkinter.Label(self.bloodDock, text="x(minus)",)
        minusButton_x = tkinter.Button(
            self.bloodDock, text='-', relief="flat", command=lambda: fuctionViewer.minus(self, 0))
        minusButton_x.pack(side='left')
        self.xLabel.pack(side="left")
        addButton_x.pack(side="left")
        addButton_x_2 = tkinter.Button(
            self.bloodDock, text='+', relief="flat", command=lambda: fuctionViewer.add(self, 1))
        self.xLabel_2 = tkinter.Label(self.bloodDock, text="x(max)",)
        minusButton_x_2 = tkinter.Button(
            self.bloodDock, text='-', relief="flat", command=lambda: fuctionViewer.minus(self, 1))
        minusButton_x_2.pack(side='right')
        self.xLabel_2.pack(side="right")
        addButton_x_2.pack(side="right")
        startButtton.pack(
            side="right", fill="x")

        tkinter.mainloop()

    def ax_h_2_k_ok(self, aspin, hspin, kspin) -> None:
        self.a = int(aspin.get())
        self.h = int(hspin.get())
        self.k = int(kspin.get())
        return None

    def ax_b_callback(self) -> None:
        win = tkinter.Tk()
        tkinter.Label(win, text="调整ax+b中a和b的数值", height=5).pack(fill="both")
        aSpin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        bspin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        tkinter.Label(win, text="调整ax+b中a的数值",).pack(fill="both")
        aSpin.pack()
        tkinter.Label(win, text="调整ax+b中b的数值",).pack(fill="both")
        bspin.pack()
        tkinter.Button(win, text="OK", relief="flat",
                       command=lambda:fuctionViewer.ax_b_ok(self, aSpin, bspin)).pack()
        tkinter.mainloop()

    def ax_b_ok(self, aspin, bspin) -> None:
        self.a = int(aspin.get())
        self.b = int(bspin.get())
        return None

    def ax_h_2_k_callback(self) -> None:
        win = tkinter.Tk()
        tkinter.Label(win, text="调整a(x+h)^2+k中a,h,k的数值",
                      height=5).pack(fill="both")
        aSpin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        hspin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        kspin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        tkinter.Label(win, text="调整a(x+h)^2+k中a的数值",).pack(fill="both")
        aSpin.pack()
        tkinter.Label(win, text="调整a(x+h)^2+k中h的数值",).pack(fill="both")
        hspin.pack()
        tkinter.Label(win, text="调整a(x+h)^2+k中k的数值",).pack(fill="both")
        kspin.pack()
        tkinter.Button(win, text="OK", relief="flat",
                       command=lambda:fuctionViewer.ax_h_2_k_ok(self, aSpin, hspin,kspin)).pack()
        tkinter.mainloop()

    def ax_2_bx_k_ok(self, aspin, bspin,kspin) -> None:
        self.a = int(aspin.get())
        self.b = int(bspin.get())
        self.k = int(kspin.get())
        return None

    def ax_2_bx_k_callback(self) -> None:
        win = tkinter.Tk()
        tkinter.Label(win, text="调整y = ax^2 + bx +k中a,b,k的数值",
                      height=5).pack(fill="both")
        aSpin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        bspin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        kspin = tkinter.Spinbox(win, from_=-100, to=100, relief="flat")
        tkinter.Label(win, text="调整y = ax^2 + bx +k中a的数值",).pack(fill="both")
        aSpin.pack()
        tkinter.Label(win, text="调整y = ax^2 + bx +k中b的数值",).pack(fill="both")
        bspin.pack()
        tkinter.Label(win, text="调整y = ax^2 + bx +k中k的数值",).pack(fill="both")
        kspin.pack()
        tkinter.Button(win, text="OK", relief="flat",
                       command=lambda:fuctionViewer.ax_h_2_k_ok(self, aSpin, bspin,kspin)).pack()
        tkinter.mainloop()
    def edit_callbak(self) -> None:
        '''
        The callback of the edit button
        '''
        formula = self.combe.get()
        if formula == self.combe["values"][0]:
            self.modelType = 0
            fuctionViewer.ax_b_callback(self)
            
        elif formula == self.combe["values"][1]:
            self.modelType = 1
            fuctionViewer.ax_h_2_k_callback(self)
            
        elif formula == self.combe["values"][2]:
            self.modelType = 2
            fuctionViewer.ax_2_bx_k_callback(self)
            

    def minus(self, label):
        if label == 0:
            self.minus -= 1
            self.realx -= 1
            self.xLabel['text'] = self.minus
        if label == 1:
            self.max -= 1
            self.xLabel_2['text'] = self.max

    def add(self, label):
        if label == 0:
            self.realx += 1
            self.minus += 1
            self.xLabel['text'] = self.minus
        if label == 1:
            self.max += 1
            self.xLabel_2['text'] = self.max

    def blender(x, y) -> list:
        y = 250-y
        x += 250
        return x, y

    def fuc(self, x):
        if self.modelType == 0:
            y = self.a*x+self.b
        if self.modelType == 1:
            y = self.a*((self.h+x)**2)+self.k
        if self.modelType == 2:
            y = (x**2)*self.a+self.b*x+self.k
        x, y = fuctionViewer.blender(x, y)
        return x,y

    def view(self, x):
        self.canvas.delete(tkinter.ALL)
        self.canvas.create_line(-10000, 250, 5000, 250)
        self.canvas.create_line(250, -5000, 250, 5000)
        for self.realx in range(self.minu, self.max):
            x, y = fuctionViewer.fuc(self, self.realx)
            x1, y1 = fuctionViewer.fuc(self, self.realx+1)
            self.canvas.create_line(x, y, x1, y1)

    class fuctions():
        def absolute_value(value: float) -> float:
            '''
            return the absolute value of the value
            '''
            return value if value >= 0 else -value

        def min(a: float, b: float) -> float:
            '''
            minus a with b
            '''
            return a-b

        def add(a: float, b: float) -> float:
            '''
            add a with b
            '''
            return a + b

        def multiplication(a: float, b: float) -> float:
            '''
            multiple a and b
            '''
            return a*b

        def division(a: float, b: float) -> float:
            '''
            return a/b
            '''
            return a / b

        def involution(a: float, b: int) -> float:
            return a ** b
fuctionViewer()
