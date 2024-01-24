from tkinter import *
root = Tk()

#COLOR
MMD_BLUE        = "#3292e0"
MMD_DARK_GRAY   = "#0C0F0A"
MMD_GRAY        = "#f5f5f5"

#WINDOWS CONFIG
PROGRAM_NAME    = "Micro Medical Devices - Production Configuration"
WINDOW_MINSIZE  = {"width" : 1280, "height" : 720} 
#WINDOW_MAXSIZE = {"width" : 1920, "height" : 1080}


# Config Window
root.title(PROGRAM_NAME)
root.configure(background=MMD_DARK_GRAY)
root.minsize(WINDOW_MINSIZE["width"],WINDOW_MINSIZE["height"])
#root.maxsize(WINDOW_MAXSIZE["width"],WINDOW_MAXSIZE["height"])
root.geometry(f"{str(WINDOW_MINSIZE['width'])}x{str(WINDOW_MINSIZE['height'])}+50+50")  # "width_window x height_window + x_topLeftCorner + y_topLeftCorner" (no spaces)

#Create left Frame
left_frame = Frame(
    root, 
    width=200, 
    height = WINDOW_MINSIZE['height'], 
    bg=MMD_GRAY
)

left_frame.grid(
    row=0, 
    column=5, 
    padx=5, 
    pady=5
)

label = Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)


#Creat Right Frame
right_frame = Frame( 
    root, 
    width = (WINDOW_MINSIZE["width"] - 200), 
    height = WINDOW_MINSIZE['height'], 
    bg = MMD_GRAY
)

right_frame.grid(
    row=0, 
    column=2, 
    padx=5,
    pady=5
)


# loop infintity of functions use root.after(time ms, function)
# Example root.after(1000, infinite_loop) 1000ms == 1 sec
# Source: https://www.tutorialspoint.com/how-to-run-an-infinite-loop-in-tkinter


root.mainloop()
