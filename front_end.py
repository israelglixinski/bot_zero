
##### * RESPONSIBLE FOR COMMUNICATION WITH THE USER

import tkinter
from datetime import datetime
from pkg_resources import resource_filename

class monitor():
    """ 
        # DESCRIPTION
        * MONITORS LOCAL LOG FILE AND DISPLAYS ON SCREEN
        
        # PARAMETERS
        * xtitle:   NAME OF THE WINDOW THAT WILL BE EXECUTED
        * xdescri:  window description
    """
    
    def __init__(self,xtitle='',xdescri='No windows selected'):
        self.xtitle = xtitle
        self.xdescri = xdescri
        self.play_pause = 'Pause monitor'
        self.create()
        
    def create(self):
        """ * CREATES A MONITOR WITH DEFAULT SETTINGS"""

        def exec_play_pause():
            """ * TEXT FLOW CONTROL"""
            if self.play_pause == 'Pause monitor':
                change = 'Play monitor'
            if self.play_pause == 'Play monitor':
                change = 'Pause monitor'
            self.play_pause = change
            btnPlayPause.config(text=self.play_pause)

        ##### * MAIN WINDOW CONFIG
        xwindow = tkinter.Tk()
        xicon = resource_filename(__name__, './assets/tentacle.ico')
        xwindow.iconbitmap(xicon)
        xwindow.title(self.xtitle)
        xwindow.resizable(False,False)
        xwindow.geometry("670x440")
        # xwindow.config(bg="#25292e") ##### * TO DARK MODE
        
        ##### * A LABEL WITH WINDOW DESCRIPTION
        frameLabel = tkinter.Frame(xwindow,padx=0,pady=5)
        # frameLabel.config(bg="#25292e") ##### * TO DARK MODE
        frameLabel.pack(fill=tkinter.X)
        lblDescri = tkinter.Label(frameLabel,text=self.xdescri)
        # lblDescri.config(bg="#25292e",fg="#FFFFFF") ##### * TO DARK MODE
        lblDescri.pack(side=tkinter.LEFT)
        btnPlayPause = tkinter.Button(frameLabel, text= self.play_pause ,command=exec_play_pause ,height=1 ,width=20)
        btnPlayPause.pack(side=tkinter.RIGHT)

        ##### * CREATE A FRAME TO STORE THE TEXT BOX
        frameText = tkinter.Frame(xwindow)
        # frameText.config(bg="#25292e") ##### * TO DARK MODE
        frameText.pack(fill=tkinter.X)

        ##### * CREATE THE TEXT BOX TO DISPLAY THE LOGS
        self.txtResult = tkinter.Text(frameText)
        # self.txtResult.config(bg="#25292e",fg="#FFFFFF") ##### * TO DARK MODE
        self.txtResult.pack(side=tkinter.LEFT)
        
        ##### * CREATE A SCROLLBAR FOR THE TEXT BOX
        scrl = tkinter.Scrollbar(frameText,command=self.txtResult.yview)
        scrl.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.txtResult["yscrollcommand"] = scrl.set        
            
        def verify():
            """ * UPDATE TEXT INFORMATION"""
            if self.play_pause == 'Pause monitor':
                self.txtResult.delete('1.0',tkinter.END)
                dtm = datetime.now().strftime('%Y%m%d')
                try:
                    ##### * checks if there is a log file with the name of the open window
                    ##### * in addition to the window name we also have the log date
                    recover = open(f'LOG_{self.xtitle}_{dtm}.txt','r')
                    self.txtResult.insert('1.0', recover.read())
                    self.txtResult.see('end')
                    recover.close()
                except:
                    ##### * and if no log file exists, one will be created
                    info = 'no previous logs found'
                    recover = open(f'LOG_{self.xtitle}_{dtm}.txt','a')
                    print (info,file=recover)
                    recover.close()
                    self.txtResult.insert('1.0', info)
            else:
                ##### * if the monitor is paused it will not bring new texts
                pass    
                
            xwindow.after(200,verify)

        verify()        
        xwindow.mainloop()

