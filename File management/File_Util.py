
# Python program to create  
# a file explorer in Tkinter 
   
# import all components 
# from the tkinter library 
from ast import copy_location
from tkinter import *
import os
import time 
# import filedialog module 
from tkinter import filedialog
from tkinter.ttk import *
import time




#Pre Program window builder check

prewindow = Tk()
prewindow.title("Options")


detailcheck = BooleanVar()
FolderCheck = BooleanVar()
PrefixCheck = BooleanVar()
StartingPoint = ""
NumberOfFiles = ""
Details_Filelist = []
WorkingDir ="" 
def Close(x,y):
        x.destroy
        y.destroy        
        exit()





def movealong():
   
    prewindow.destroy()
    direct = ""   


    # Function for opening the  
    # file explorer window 
    def browseFiles(): 

        window.directory = filedialog.askdirectory()       
        # Change label contents 
        label_selected_folder.configure(text=window.directory) 
        WorkingDir =(window.directory)


    def details():
        window.Details_File = filedialog.askopenfilename( 
                                              title = "Select a File", 
                                              filetypes = (("Text files", 
                                                            "*.txt*"), 
                                                           ("all files", 
                                                            "*.*"))
                                                                    )
        label_selected_details.configure(text = window.Details_File)
        DetailLoc = (window.Details_File)


    def createFolder(directory):
         
                    os.makedirs(window.directory+"/"+directory)
                    

    def start():
        NumberOfFiles = Input_NumberOfFiles.get()
        StartingPoint = Input_StartingPoint.get()
        if (NumberOfFiles.isdigit() == False) or (StartingPoint.isdigit() == False):
            error = Tk()
            error.title("An error has occurred")
            label_error_reason = Label(error,
                                        text="You must enter whole numbers only!")
            button_error_ok = Button(error,
                                    text= "ok",
                                     command= error.destroy)
            label_error_reason.grid(column=0,row=0)
            button_error_ok.grid(column=1,row=1)
            error.mainloop()
        
        
        
        if FolderCheck.get() == False:
            createFolder(Input_Practice_Name.get())
       
       
       
       # ProgressBarval = IntVar()
        #prog = Tk()
        #prog.title("Progress")
        #prog.geometry(Input_NumberOfFiles.get()+"x50")
      #  progress = Progressbar(prog, 
       #                        orient = HORIZONTAL, 
        #                       length = int(Input_NumberOfFiles.get())-int(Input_StartingPoint.get()),
         #                      mode = 'determinate',
          #                     variable= ProgressBarval,
           #                    maximum=int(Input_NumberOfFiles.get())-int(Input_StartingPoint.get())
            #                    )
        #progress.grid(column=0,row=0)
        #prog.mainloop

        if detailcheck.get() == True:
                #progress.start()
                Details_File = open(window.Details_File)
                Details_Filecontent = Details_File.readlines()
                for line in Details_Filecontent:
                        Current_Detail = line[:-1]
                        Details_Filelist.append(Current_Detail)
                for i in range((int(Input_StartingPoint.get())), (int(Input_NumberOfFiles.get())+int(StartingPoint))):
                                file = open((window.directory)+"/"+Input_Practice_Name.get+"/"+Input_Prefix.get()+str(i)+".py", "+w")
                                file.write("#Practice Name: "+Input_Practice_Name.get() + "\n#Question Number: " + str(i)+"\n\n#TODO: enter question detail here\n\n\n"+"#"+Details_Filelist[i-int(Input_StartingPoint.get())]+"\n\n#Date and time Created:" + str(time.localtime(time.time())[0])+"-"+str(time.localtime(time.time())[1]) + "-" + str(time.localtime(time.time())[2])+""+str(time.localtime(time.time())[3])+":"+str(time.localtime(time.time())[4])+"\n\n\n")
                               # ProgressBarval.set(progress,i) 
                                #time.sleep(0.05)
        elif detailcheck.get() ==False:
            
            for i in range((int(Input_StartingPoint.get())), (int(Input_NumberOfFiles.get())+int(Input_StartingPoint.get()))):                       
                        file = open((window.directory)+"/"+Input_Practice_Name.get()+"/"+Input_Prefix.get()+str(i)+".py", "+w")
                        file.write("#Practice Name: "+Input_Practice_Name.get() + "\n#Question Number: " + str(i)+"\n\n#TODO: enter question detail here\n\n\n"+"#Date and time completed:" + str(time.localtime(time.time())[0])+"-"+str(time.localtime(time.time())[1]) + "-" + str(time.localtime(time.time())[2])+""+str(time.localtime(time.time())[3])+":"+str(time.localtime(time.time())[4])+"\n\n\n")
                        #ProgressBarval.set(i) 
                      #  progress.update_idletasks()

            Success = Tk()
           # progress.destroy
            Success.title("File Creation successful") 
            Success.geometry("150x150")           
            label_file_Success = Label(Success,
                                        text= "File Creation was successfull.")
            button_exit = Button(Success,  
                     text = "Exit", 
                     command = exit)
            label_file_Success.grid(column=2,row=1)
            button_exit.grid(column=2,row=2)
            Success.mainloop()

    # Create the root window 
    window = Tk()  
    window.title('File Explorer') 

    # Create a File Explorer label 
    label_file_explorer = Label(window,  
                            text = "Please select a working directory:"
                            ) 
    label_selected_folder = Label(window,
                              text= ""
                              )
    button_explore = Button(window,  
                        text = "Browse Folders", 
                        command = browseFiles)  
    label_details_selector = Label(window,
                                text ="Select a file with details in it."
                                )
    button_Details = Button(window,
                         text = "Browse Files",
                         command = details )
    label_selected_details = Label(window,
                               text = ""
                               )
    button_create = Button(window,
                    text = "Start File creation",
                    command = start)
    button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  
    
    label_NumberOfFiles = Label(window,
                            text = "Enter the number of files")
    Input_NumberOfFiles = Entry(window)

    label_StartingPoint = Label(window,
                                text = "Enter the starting Point for the files")
    Input_StartingPoint = Entry(window)
    
    label_Prefix = Label(window,
                        text = "File prefix ")
    Input_Prefix = Entry(window)

    label_Practice_Name = Label(window, 
                                text="Enter the practice name")
    Input_Practice_Name = Entry(window)
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
   
    label_file_explorer.grid(column = 0, row = 1) 
    button_explore.grid(column = 1, row = 1) 
    label_selected_folder.grid(column=2,row=1)   
    
    if detailcheck.get() == True:
        label_details_selector.grid(column=0,row=2)
        button_Details.grid(column=1,row=2)
        label_selected_details.grid(column=2,row=2)
    
    if FolderCheck.get() == False:
        label_Practice_Name.grid(column=0,row=3) 
        Input_Practice_Name.grid(column=1,row=3)

    label_NumberOfFiles.grid(column=0,row=4)
    Input_NumberOfFiles.grid(column=1,row=4)
    
    label_StartingPoint.grid(column=0,row=5)
    Input_StartingPoint.grid(column=1,row=5)
   
    if PrefixCheck.get() == True:
        label_Prefix.grid(column=0,row=6)
        Input_Prefix.grid(column=1,row=6)
    
    button_create.grid(column = 1, row = 8)
    button_exit.grid(column = 1,row = 9)    
    # Let the window wait for any events 
    window.mainloop() 







def clicked():
    
    print(detailcheck.get())
def clicked1():
     print(FolderCheck.get())
def clicked2():
      print(PrefixCheck.get())

label_title = Label(prewindow,
                     text="Please select all that apply.")
Premade_Folder = Checkbutton(prewindow,
                                 text="Is there a premade folder?",
                                 variable = FolderCheck,
                                 onvalue = 1,
                                 offvalue = 0,
                                 command = clicked1
                                 )
Details_Check = Checkbutton(prewindow,  
                                text = "Do you have a .txt file containing details for each file?", 
                                variable = detailcheck, 
                                onvalue = 1, 
                                offvalue = 0,
                                command= clicked
                                )
Prefix_Check = Checkbutton(prewindow,
                                text = "Do you want a file prefix",
                                variable= PrefixCheck,
                                onvalue = 1,
                                offvalue=0,
                                command = clicked2
                                )

button_set = Button(prewindow,
                        text="Continue",
                        command = movealong)

label_title.grid(column=2,row=0)
Premade_Folder.grid(column=2,row=1)
Details_Check.grid(column=2,row=2)
Prefix_Check.grid (column=2,row=3)
button_set.grid(column=2,row=4)

prewindow.mainloop()

