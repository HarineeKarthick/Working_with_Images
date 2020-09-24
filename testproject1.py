import sys
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox  
# loading Python Imaging Library 
from PIL import ImageTk, Image,ImageOps  
  
# To get the dialog box to open when required  
from tkinter import filedialog 

# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 

# Create a windoe 
root = Tk() 

# Set Title as Image Loader 
root.title("Image Loader") 

# Set the resolution of window 
root.geometry("1000x1000") 

# Allow Window to be resizable 
root.resizable(width = True, height = True) 

# declaring string variable 
# for storing name and password 
width_var=StringVar() 
height_var=StringVar()
 
# creating a label for 
# width using widget Label 
width_label = Label(root, text = 'Width(in pixels)',font=('calibre',10, 'bold')) 

# creating a entry for input 
# width using widget Entry 
width_entry =Entry(root,textvariable = width_var,font=('calibre',10,'normal')) 

# creating a label for height 
height_label =Label(root,text = 'height(in pixels)',font = ('calibre',10,'bold')) 
 
# creating a entry for height 
height_entry=Entry(root,textvariable = height_var,font = ('calibre',10,'normal')) 

global transposed_img
edit=None

def resizing():
	if open_btn["state"]=="normal":
		open_btn["state"]="disabled"
	 
	sub_btn=Button(root,text = 'OK',command =lambda:sizeok()) 
  
	width_label.grid(row=3,column=0) 
	width_entry.grid(row=3,column=1) 
	height_label.grid(row=4,column=0) 
	height_entry.grid(row=4,column=1) 
	sub_btn.grid(row=5,column=1)        

def sizeok(): 
	global img
	w=width_var.get() 
	h=height_entry.get() 
	last=x.rindex("/")
	
	s=x[last+1:]
	stop=s.rindex(".")
	new_name=s[:stop]+"copy"+s[stop:]
	
	
	print("The width is : " + w) 
	print("The height is : " + h) 
	#img=Image.open(x)
	copy=img.resize((int(w),int(h))) 
	img=copy
	#copy.save(new_name)
	#save_btn1=Button(root,text = 'SAVE',command = lambda:saving(copy)).grid(row = 5, column=2)	
	width_var.set("") 
	height_var.set("")
	

 

def SIZE():
	if open_btn["state"]=="normal":
		open_btn["state"]="disabled"
	w,h=img.size
	messagebox.showinfo("ImageSize", "width : "+str(w)+"  "+"height : "+str(h)) 
	
	

def flip():
	if open_btn["state"]=="normal":
		open_btn["state"]="disabled"
	global img,panel,panel1
	img=ImageOps.flip(img)	
	s=img
	img2= s.resize((200,200), Image.ANTIALIAS) 
	img2 = ImageTk.PhotoImage(img2)
	panel1 = Label(root, image = img2) 
	panel1.image = img2 
	panel1.grid(row = 0,column=9)
	save_btn=Button(root,text = 'save',command = lambda:save_changes()).grid(row=10,columnspan=4)
	

def mirror():
	if open_btn["state"]=="normal":
		open_btn["state"]="disabled"
	global img,panel,panel1
	
	img = img.transpose(Image.FLIP_LEFT_RIGHT)
	#print(transposed_img)
	#transposed_img = Image.open(transposed_img)	
	s=img
		
	# resize the image and apply a high-quality down sampling filter 
	img2= s.resize((200,200), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img2 = ImageTk.PhotoImage(img2) 

	# create a label 
	panel1 = Label(root, image = img2) 
	
	# set the image as img 
	panel1.image = img2 
	panel1.grid(row = 0,column=9)
	
	save_btn=Button(root,text = 'save',command = lambda:save_changes()).grid(row=10,columnspan=4)

def Black_White():
	if open_btn["state"]=="normal":
		open_btn["state"]="disabled"
	global edit,img,count,panel,panel1
	img=img.convert('L')
	bw=img
	img2=bw.resize((200,200), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img2 = ImageTk.PhotoImage(img2) 

	# create a label 
	panel1 = Label(root, image = img2) 
	
	# set the image as img 
	panel1.image = img2 
	panel1.grid(row = 0,column=9)
	save_btn=Button(root,text = 'save',command = lambda:save_changes()).grid(row=10,columnspan=4)
	
	#img.save("savedimg2.png")		

def save_changes():
	global panel,panel1
		 
	file=asksaveasfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	if not file:
		return
	img.save(file)
	if open_btn["state"]=="disabled":
		open_btn["state"]="normal"
	

def exitme():
	sys.exit(0)

def open_img(): 
	global img,pic,x,count,color,panel
	# Select the Imagename from a folder
	count=0 
	x = filedialog.askopenfilename(title ='Choose Image')
	
	# opens the image 
	img = Image.open(x)
	color,pic=img,img      
	
		
	# resize the image and apply a high-quality down sampling filter 
	img1= pic.resize((400,400), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img1 = ImageTk.PhotoImage(img1) 

	# create a label 
	panel = Label(root, image = img1) 
	 
	panel.image = img1 
	panel.grid(row = 0)
	
	resize_btn=Button(root,text = 'Resize Image',command = lambda:resizing()).grid(row=2,column=3,columnspan=10) 
	size_btn= Button(root, text ='Image Size', command =lambda: SIZE()).grid(row = 6,column=3, columnspan=10)
	mirror_btn=Button(root,text='Mirror Image',command=lambda:mirror()).grid(row=7,column=3,columnspan=10)  
	blackwhite_btn= Button(root,text='Black&White',bg="pink",command=lambda:Black_White()).grid(row=8,column=3,columnspan=10) 
	flip_btn=Button(root,text = 'FlipImage',command = lambda:flip()).grid(row=9,column=3,columnspan=10) 	
	
open_btn = Button(root, text ='Open Image', command = open_img,height=3,width=8)
open_btn.grid(row = 1, columnspan = 4)
exit_btn=Button(root,text = 'exit',command = lambda:exitme(),height=3,width=8).grid(row=15,columnspan=4)	

root.mainloop()
