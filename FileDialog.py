
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from turtle import position
from urllib import response
import logger
import os
import time


class Dialogs():
    def __init__(self,ent,master):
        self.ent = ent
        self.master = master


    def new(self):
        if len(self.ent.get('1.0',END)) <= 0:
            pass
        if len(self.ent.get('1.0',END)) > 1:
            response = messagebox.askyesnocancel('Save File','Do you want to save file?')
            
            try:
                if str(response) == 'True':
                    
                    fileName = fd.asksaveasfilename(initialdir=os.getcwd,title='Save',
                    filetypes=(('text files','*txt'),('python files','*py',),
                                            ('html file','*.html'),('css file','*.css')))

                    try:
                        with open(fileName,'w') as f:
                            f.write(self.ent.get('1.0',END))
                            f.close()
                    except Exception as e:
                        logger.logger.error(e)
    
                elif str(response) == 'False':
                    self.ent.config(state='normal')
                    self.ent.delete('1.0',END)
                   
                else:
                    pass

            except Exception as e:
                logger.logger.error(e)

    def open(self):
        try:
            fileName = fd.askopenfilename(initialdir=os.getcwd,title='Open',
                filetypes=(('text files','*txt'),('python files','*py',),
                                            ('html file','*.html'),('css file','*.css')))
            with open(fileName,'r') as f:
                try:
                    content = f.read()
                    f.close()
                except Exception as e:
                    logger.logger.error(e)
                
                self.ent.config(state='normal')
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT,content)
            
        except Exception as e:
            logger.logger.error(e)



    def save(self):
        if len(self.ent.get('1.0',END)) <= 1:
            messagebox.showinfo('Empty Feild','The entry feild seem empty,fill the entry with some text and try to save it again')
        else:
            try:
                fileName = fd.asksaveasfilename(initialdir=os.getcwd,title='Save',
                    filetypes=(('text files','*txt'),('python files','*py',),
                                                ('html file','*.html'),('css file','*.css')))
                with open(fileName,'a') as f:
                    try:
                        f.write(self.ent.get('1.0',END))
                        f.close()
                    except Exception as e:
                        logger.logger.error(e)
                
            except Exception as e:
                logger.logger.error(e)


    def saveas(self):
        try:
            fileName = fd.asksaveasfilename(initialdir=os.getcwd,title='Save',
                filetypes=(('text files','*txt'),('python files','*py',),
                                            ('html file','*.html'),('css file','*.css')))
            with open(fileName,'w') as f:
                f.write(self.ent.get('1.0',END))
                f.close()
        except Exception as e:
            logger.logger.error(e)

    def page_setup(self):
        pass


    def Print(self):
        pass


    def undo(self):
        pass
    
    def cut(self,event):
        #check if text is selected
        if self.ent.selection_get():
            #save selected text to variable
            self.selected = self.ent.selection_get()
            #delete selected text
            self.ent.delete('sel.first','sel.last')  
        self.ent.bind("<Control-x>",self.cut)


    def copy(self,event):
        #check if text is selected
        if self.ent.selection_get():
            #save selected text to variable
            self.selected = self.ent.selection_get()
        self.ent.bind("<Control-c>",self.copy)
        

    def paste(self,event):
        if self.selected:
            position = self.ent.index(INSERT)
            self.ent.insert(position,self.selected)
        self.ent.bind("<Control-v>",self.paste)

    def delete(self):
        pass

    def googleQuery(self):
        pass

    def find():
        pass

    def findNext(self):
        pass

    def findPrevious(self):
        pass

    def goto(self):
        pass

    def selectAll(self):
        pass

    def timedate(self):
        pass

    def wordWrap(self):
        pass

    
    def zoom(self):
        pass

    def statusBar(self):
        pass

    def helper(self):
        pass

    def feedback(self):
        pass

    def About(self):
        try:
            if len(self.ent.get('1.0',END)) <= 1:
                try:
                    with open('About CubeEdit.txt','r') as f:
                        txt = f.read()

                        self.ent.insert(INSERT,txt)
                        self.ent.config(state='disabled')
                except Exception as e:
                    logger.logger.error(e)

            elif len(self.ent.get('1.0',END)) > 1:
                response = messagebox.askyesnocancel('Save file','Do you want to save file?')

                if str(response) == 'True':
                    fileName = fd.asksaveasfilename(initialdir=os.getcwd,title='Save',
                        filetypes=(('text files','*txt'),('python files','*py',),
                                            ('html file','*.html'),('css file','*.css')))

                    try:
                        with open(fileName,'w') as f:
                            f.write(self.ent.get('1.0',END))
                            f.close()
                    except Exception as e:
                        logger.logger.error(e)
                    
                elif str(response) == 'False':
                    try:
                        with open('About CubeEdit.txt','r') as f:
                            txt = f.read()

                        self.ent.delete('1.0',END)
                        self.ent.insert(INSERT,txt)
                        

                    except Exception as e:
                        logger.logger.error(e)

                else:
                    pass
                    

        except Exception as e:
            logger.logger.error(e)