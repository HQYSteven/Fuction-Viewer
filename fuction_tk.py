import tkinter

class fuctionImageViewer(tkinter.Frame):
    def __init__(self):
        self.realx = -25
        self.x =-1100
        self.max = 1100
        self.minus = -1100
        self.root = tkinter.Tk()
        self.screen = tkinter.Frame(self.root,width=300,height=300)
        self.screen.pack()
        self.bloodDock = tkinter.Frame(self.root)
        self.bloodDock.pack(side = "bottom")
        bar = tkinter.Scrollbar(self.screen,relief="flat")
        bar.pack(fill = "both",side = "right")
        hbar = tkinter.Scrollbar(self.screen,orient="horizontal",
                                 )
        self.canvas = tkinter.Canvas(self.screen,
                                confine=False,
                                xscrollincrement=50,
                                yscrollincrement=50,
                                width = 500,
                                bg='white',cursor="cross",
                                height=500,
                                yscrollcommand=bar.set,
                                xscrollcommand=hbar.set)
        hbar.config(command=self.canvas.xview)
        hbar.pack(side = "bottom",fill="x")
        self.canvas.pack(side = "right")
        self.canvas.create_line(0,250,500,250)
        self.canvas.create_line(250,-500,250,500)
        
        bar.config(command=self.canvas.yview)
        startButtton = tkinter.Button(self.bloodDock,text='Start',
                                      command = lambda :fuctionImageViewer.
                                      view(self,self.x),relief="flat")
        addButton_x = tkinter.Button(self.bloodDock,text = '+',relief="flat"
                                     ,command=lambda :fuctionImageViewer.add(self,0))
        self.xLabel = tkinter.Label(self.bloodDock,text="x(minus)",)
        minusButton_x = tkinter.Button(self.bloodDock,text = '-',relief="flat"
                                    ,command=lambda :fuctionImageViewer.minus(self,0))
        minusButton_x.pack(side = 'left')
        self.xLabel.pack(side = "left")
        addButton_x.pack(side="left")
        addButton_x_2 = tkinter.Button(self.bloodDock,text = '+',relief="flat"
                                       ,command=lambda :fuctionImageViewer.add(self,1))
        self.xLabel_2 = tkinter.Label(self.bloodDock,text="x(max)",)
        minusButton_x_2 = tkinter.Button(self.bloodDock,text = '-',relief="flat"
                                    ,command=lambda :fuctionImageViewer.minus(self,1))
        minusButton_x_2.pack(side = 'right')
        self.xLabel_2.pack(side = "right")
        addButton_x_2.pack(side="right")
        startButtton.pack(
                          side="right",fill="x")
        
        tkinter.mainloop()
    def minus(self,label):
        if label == 0:
            self.minus -=1
            self.realx -=1
            self.xLabel['text'] = self.minus
        if label == 1:
            self.max -=1
            self.xLabel_2['text'] = self.max
    def add(self,label):
        if label == 0:
            self.realx +=1
            self.minus +=1
            self.xLabel['text'] = self.minus
        if label == 1:
            self.max +=1
            self.xLabel_2['text'] = self.max
    def fuc(x):
        if x != 0:
            y= 1000/x+2/x+1.5*x
        else:
            y=0
        y = 250-y
        x+=250
        return x,y
    def view(self,x):
        for self.realx in range(self.minus,self.max):
            x,y = fuctionImageViewer.fuc(self.realx)
            x1,y1 = fuctionImageViewer.fuc(self.realx+1)
            self.canvas.create_line(x,y,x1,y1)



fuctionImageViewer()