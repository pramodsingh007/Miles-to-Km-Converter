from tkinter import *



fonts = ("Arial",15,"bold")

class Miles_to_Km():
    
    def calculate(self):

        root = Tk()
        root.title("Miles to KM Converter")
        root.wm_minsize(width=500,height=300)


        ##################entry for miles
        miles = Entry()
        miles.focus()
        miles.place(x=200,y=60)
        miles_text =  Label(text="Miles",font=fonts)
        miles_text.place(x=280,y=55)
        ############################### Entry for KM
        kilometers =  Label(text="0",font=fonts)
        kilometers.place(x=200,y=90)
        kilometers_text = Label(text="Kilometers",font=fonts)
        kilometers_text.place(x=280,y=90)
        def Miles_converter():
            m =  int(miles.get())
            result = m*1.6
            kilometers.config(text='%.2f'%result)

        #################################
        convert =  Button(text="Convert",command=Miles_converter)
        convert.place(x=180,y=130)

        ######################################clear button
        def clean():
            miles.delete(0,END)
            kilometers.config(text=0)

        clear = Button(text="Clear",command=clean)
        clear.place(x=270,y=130)


        root.mainloop()



test = Miles_to_Km()
test.calculate()