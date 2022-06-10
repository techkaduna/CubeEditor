
from tkinter import *
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import FileDialog 
from tkinter import ttk


root = Tk()

class Editor():
    def __init__(self,master):
    
        self.master = master
        #setting basic window
        self.master.title('CubeEdit')
        self.master.geometry('1000x600')
        self.master.resizable(0,0)
        self.master.configure(bg='lightgrey')
        self.master.iconbitmap('cubeicon.ico')

        #text area
        self.text = ScrolledText(self.master)
        self.text.config(width=950,height=35)
        self.text.pack()


        #modules
        mod = FileDialog.Dialogs(self.text,self.master) 


        #MENU__WORKS
        self.mymenu = Menu(self.master)
        root.config(menu=self.mymenu)
        self.file = Menu(self.mymenu)
        self.edit = Menu(self.mymenu)
        self.format = Menu(self.mymenu)
        self.veiw = Menu(self.mymenu)
        self.help = Menu(self.mymenu)

        #self.MenuItems

        self.mymenu.add_cascade(label='File',font=('Railway',18),menu=self.file)

        self.file.add_command(label='New        Ctrl+N',font=("Railway",10),command=mod.new)
        self.file.add_command(label='New Window Ctrl+Shift+N',font=("Railway",10),command=self.new_window)
        self.file.add_command(label='Open       Ctrl+O',font=("Railway",10),command=mod.open)
        self.file.add_command(label='Save',font=("Railway",10),command=mod.save)
        self.file.add_command(label='Save As    Ctrl+S',font=("Railway",10),command=mod.saveas)
        self.file.add_separator()
        self.file.add_command(label='Page setup',font=("Railway",10))
        self.file.add_command(label='Print  Ctr+P',font=("Railway",10))
        self.file.add_command(label='Exit   Ctrl+F4',font=("Railway",10), command= root.destroy)


        #EDIT MEUN OPTIONS
        self.mymenu.add_cascade(label='Edit',menu=self.edit)
        
        self.edit.add_command(label='Undo     Ctrl+Z',font=("Railway",10))
        self.file.add_separator()
        self.edit.add_command(label='Cut Ctrl+X',font=("Railway",10),command=lambda:mod.cut(False))
        self.edit.add_command(label='Copy       Ctrl+C',font=("Railway",10),command=lambda:mod.copy(False))
        self.edit.add_command(label='Paste     Ctrl+V',font=("Railway",10),command=lambda:mod.paste(False))
        self.edit.add_command(label='Delete',font=("Railway",10))
        self.edit.add_separator()
        self.edit.add_command(label='Search with google',font=("Railway",10))
        self.edit.add_command(label='Find',font=("Railway",10))
        self.edit.add_command(label='Find Next',font=("Railway",10))
        self.edit.add_command(label='Find Previous',font=("Railway",10))
        self.edit.add_command(label='Replace',font=("Railway",10))
        self.edit.add_command(label='Go to',font=("Railway",10))
        self.edit.add_separator()
        self.edit.add_command(label='Select All',font=("Railway",10))
        self.edit.add_command(label='Time Date',font=("Railway",10))


        #FORMAT MENU OPTIONS
        self.mymenu.add_cascade(label='Format',menu=self.format)

        self.format.add_command(label='Word Wrap',font=("Railway",10))
        self.format.add_separator()
        self.format.add_command(label='Font',font=("Railway",10),command=self.font)
        
        #VEIW MEUN OPTIONS
        self.mymenu.add_cascade(label='Veiw',menu=self.veiw)

        self.veiw.add_command(label='Zoom',font=("Railway",10))
        self.veiw.add_command(label='Status Bar',font=("Railway",10))
        
        #HELP MENU OPTIONS
        self.mymenu.add_cascade(label='Help',menu=self.help)

        self.help.add_command(label='Veiw Help',font=("Railway",10))
        self.help.add_command(label='Send Feedback',font=("Railway",10))
        self.help.add_separator()
        self.help.add_command(label='About CubeEdit',font=("Railway",10),command=mod.About)


        
        
        self.master.mainloop()

    def new_window(self):
        top = Toplevel(root)
        Editor(top)

    def font(self):
        global FONT,FONT_SIZE
    
        top = Toplevel(root)
        top.title('select font')
        top.geometry('400x250')
        top.resizable(0,0)
        #top.configure(bg='lightgrey')
        top.iconbitmap('cubeicon.ico')

        #frames
        frame1 = Frame(top)
        frame1.pack()
        frame2 = Frame(top)
        frame2.pack()
        frame3 = Frame(top)
        frame3.pack()
        frame4 = Frame(top)
        frame4.pack(fill='x')

        #labels
        lbl_font  = Label(frame1,text='Font',font=('Railway',10))
        lbl_font.grid(row=0,column=0,pady=5)
        lbl_fontstyle = Label(frame1,text='Font-style',font=('Railway',10))
        lbl_fontstyle.grid(row=0,column=1,padx=90,pady=5)
        lbl_fontsize = Label(frame1,text='Size',font=('Railway',10))
        lbl_fontsize.grid(row=0,column=2,padx=5,pady=5)

        def preview(event):
            FONT = choose_font.get()
            FONT_SIZE = choose_size.get()
            txtarea.config(font=(FONT,int(FONT_SIZE)),width=25,height=5)
            txtarea.delete('1.0',END)
            txtarea.insert(INSERT,f'SAMPLE TEXT WITH {FONT.upper()} WITH A SIZE OF {str(FONT_SIZE)}')
            

        def okbtn(self):
            print('i am working')
            
            

        FONT = ''
        FONT_SIZE = int()

        options = [
            'AcadEref',
            'Aeolus',
            'Arial',
            'Arial black',
            'Artistik',
            'Banschrift',
            'Basque',
            'Brush Script MT',
            'Bradley Hand ITC',
            'Book Antiqua',
            'BalloonDroShaD',
            'Calibri',
            'Collage',
            'CommercialScript ',
            'Consolas',
            'EuroRoman',
            'Railway',
            'Ravie',
            'SansSerif',
            'Times New Roman',
            'Viner Hand ITC'
        ]

        sizes = [i for i in range(5,101)]

        styles = [
            'Regular',
            'Bold',
            'Italic',
            'Bold Italic'
        ]
        choose_font = StringVar()
        choose_size = IntVar()
        
        font_combo = ttk.Combobox(frame2,value=options)
        font_combo.set(options[0])
        font_combo.config(textvariable=choose_font) #,state='readonly'
        font_combo.bind('<<ComboboxSelected>>',preview)
        font_combo.grid(row=0,column=0)

        style_combo = ttk.Combobox(frame2,value=styles)
        style_combo.set(styles[0])
        #myCombo.bind('<<ComboboxSelected>>',comboed)
        style_combo.grid(row=0,column=1,padx=3)

        size_combo = ttk.Combobox(frame2,value=sizes)
        size_combo.set(sizes[14])
        size_combo.config(width=5,textvariable=choose_size)
        #size_combo.bind('<<ComboboxSelected>>',preview)
        size_combo.grid(row=0,column=2,padx=3)

        #sample text area

        txtarea = Text(frame3)
        txtarea.config(font=('Arial',14),width=25,height=5)
        txtarea.insert(INSERT,f'SAMPLE TEXT WITH {FONT}')
        txtarea.pack(side='right',pady=10)

        #buttons
        btn_okay = Button(frame4,text='OK',relief='flat')
        btn_okay.grid(row=0,column=0,padx=20)

        btn_cancel = Button(frame4,text='CANCEL',relief='flat',command=top.destroy)
        btn_cancel.grid(row=0,column=1,padx=20)

        top.mainloop()



if __name__ == "__main__":
    Editor(root)
