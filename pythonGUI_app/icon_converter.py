from tkinter import *
App = Tk()
App.title("icon converter")



def open_img():
    from PIL import  Image
    from tkinter import filedialog  #import the filedialog module

    global img #global variable

    App.img_dir = filedialog.askopenfilename(title="Select an image",initialdir='C:', filetypes=(("png files", "*.png"), ("all files", "*.*")))  # opens a file dialog

    img = Image.open(App.img_dir)  # img.save("icon.png")


def convert_to_icon():
    from PIL import Image

    # img.save("icon.png")  # save the image as a png

    img.save(f'{ico_name}.ico', format='ICO' , sizes= [(ico_size, ico_size)])# save the image as a ico
    success = Toplevel() #create a new window
    success.title("Success") #set the title of the new window

    msg = Label(success, text="Successfully converted to icon") #create a label
    msg.pack()


    def preview():
        prev = Toplevel() #create a new window
        prev.title("Preview") #set the title of the new window
        prev.iconbitmap(f'{ico_name}.ico') #set the icon of the new window
        prev_label = Label(prev, text="Check icon") #create a label
        prev_label.pack()
        prev.mainloop()
