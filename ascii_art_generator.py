#First, we import the required libraries for the correct execution of our project
#First two libraries are used for image processing
#The third library provides access to common math functions
import cv2
from PIL import Image, ImageDraw, ImageOps, ImageFont
import math

#We store the video object in a variable. "boune.mp4" is the video name which get stored. 
video_working_on=cv2.VideoCapture("boune.mp4")

#Number_of_frames variable stores the count of frames which are extracted from the video object
number_of_frames=0
boolean_value=1

#The below loops extracts the frames from the video and stores it in the file name called "images". Also upon entering each loop, the count of number_of_frames increases by 1
while boolean_value:
    boolean_value,image=video_working_on.read()
    try:
        cv2.imwrite("images/frame%d.jpg"%number_of_frames,image)
    except:
        break
    number_of_frames+=1


#The below characterset is used for mapping to pixels. The characters which occupy more space are arranged first. These characters are stored in a ist
complex="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
charset=list(complex)


#The image is resized and the height and widht is set accordingly to prevent the huge computatonal steps in large image
scalingFactor=0.2
Scaled_Width=10
Scaled_Height=12
font=ImageFont.truetype('fonts\DejaVuSansMono-Oblique.ttf',15)


#The below function will return an ascii character from charset corresponding to the ascii value of pixel
def getChar(inputInt):
    return charset[math.floor(inputInt*(len(charset)/256))]


#Now we run a loop and convert all the frame images(currently stored in images folder) to the ascii image and stores them in a new folder (say ascii_images)
for l in range(number_of_frames):
    image=Image.open("images/frame"+str(l)+".jpg")
    width,height=image.size
    image=image.resize((int(scalingFactor*width),int(scalingFactor*height*(Scaled_Width/Scaled_Height))),Image.NEAREST)
    pixel_value=image.load()
    width,height=image.size
    print("Running....images are being processed")#While this loop is running, this output line will indicate the correct execution of code.

    outputImage=Image.new('RGB',(Scaled_Width*width,Scaled_Height*height),color=(0,0,0))#background set as black 
    d=ImageDraw.Draw(outputImage)


#The following loops go though the entire mesh(each pixel) and collects the mean of rgb value of each pixel
    for i in range(height):
        for j in range(width):
            r,g,b=pixel_value[j,i]
            h=int((r+g+b)/3)
            pixel_value[j,i]=(h,h,h)
            d.text((j*Scaled_Width,i*Scaled_Height),getChar(h),font=font,fill=(r,g,b))

    outputImage.save("ascii_images/asciimg"+str(l)+".jpg")#The output images are saved in ascii_images folder. These will further be used as frames for the final output video



# Now in the final part of code, the image frames which are store in a folder called ascii_images will be merged together to create the final output video
ref_image=cv2.imread("ascii_images/asciimg1.jpg")#Used as a reference image for extracting the height and width in a single image frame
ref_height,ref_width,ref_rgb=ref_image.shape
vid_categ=cv2.VideoWriter_fourcc(*'mpv4')
video_final=cv2.VideoWriter("resssss.mp4",vid_categ,15,(ref_width,ref_height))
for i in range(number_of_frames):
    ith_image="ascii_images/asciimg"+str(i)+".jpg"
    video_final.write(cv2.imread(ith_image))
cv2.destroyAllWindows()
video_final.release()
