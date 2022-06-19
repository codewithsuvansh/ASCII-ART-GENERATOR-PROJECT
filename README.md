# ASCII-ART-GENERATOR-PROJECT
PROJECT DESCRIPTION:
The ASCII stands for "American Standard Code for Information Interchange". It encodes certain characters and was mainly developed for electronic communication. In this project, we aim to convert an image (composed of pixels) into an ASCII art, which is an art, formed out of the ASCII encoded characters. Images, as you know are composed of pixels that can be assumed to be tiny-shaped squares containing some relevant information. In the case of a gray image, these pixels contain only one piece of information which in simple terms describes the intensity of the black shade. In the case of colored images, three types of information are contained within a pixel--(intensity of red color, intensity of green color, and intensity of blue color). The final colored image is formed by the overlapping of all these intensities. So, in ASCII art we map the relevant ASCII character to each pixel depending upon the value that it stores. Now the question arises, how can we proceed in the case of colored images. So there are many ways, one of which is to take the average of three intensities and proceed the same way as in the case of the gray image. The additional feature of this project is the generation of the ASCII ART video, which is nothing but a compilation of all the ASCII ART images of the input video frames.

HOW TO RUN THE PROJECT:
The first requirement for running the project is the installation of basic libraries like OpenCV, PIL, NumPy depending upon the requirement. After making sure all these libraries are installed, the next step is to open the python code in a suitable ide from which you can easily access other files (like images, videos, font files, etc). The downloaded zip folder from the GitHub repository should be carefully extracted and make sure no file is left missing. Once all the required files are present along with the python code in the same folder(since in code, the location of files is given relative to my computer's file's location), you are all set to run the python code. After code execution, the resultant video file will be generated in the same folder. A more detailed explanation is given in the video which is uploaded to the same Github repository.

THE INTERNAL WORKING OF THE PROJECT:
Firstly, the working libraries are imported into the python code which will allow us to perform the required operation in the project. Then the video whose ASCII video is to be made is taken as the input and a loop is run in which frames of images in the video are extracted at an equal interval of time. These image frames are stored in an empty folder(the folder was empty before the code's execution) called images. Next, the character list or set of ASCII ART characters is made which will be finally used to map with the resultant pixel value. The scale of the output image(corresponding to each frame) is set to minimize the computational steps and avoid large output ASCII ART. The font is set using the font folder which already contains some types of fonts. Then a function is run which will help to map the ASCII text's value to the pixel's value. The second loop is run to convert all the image frames stored in the "images" folder to ASCII art images and store them in a new folder called "ascii_images". In converting an image to an ASCII art image, each pixel's resultant value is mapped to the corresponding ASCII character and is drawn over a blank canvas(with initial black background(You can choose the background of your choice)). A final loop is run which appends all the ASCII images and results in the desired ASCII art video. 

LEARNINGS FROM THE PROJECT:
By getting involved in this project, I learned how images are formed from pixels. Also, I learned how pixel stores a particular value which is later used to map with the ASCII characters. I learned how to extract image frames from a video and how to append images to a video. Overall, it was a great experience doing this project. Thanks to all the members of TEAM ACM IITR for giving me this opportunity to work on this wonderful project.

ADDITIONAL TASK:
As mentioned earlier, the additional task I did was the incorporation of video to create a video containing ASCII art image frames. The rest of the details are already mentioned above. 

RESOURCES/REFERENCES:
* The slides provided by the team of ACM IITR and the workshops conducted by them. 
*  https://docs.opencv.org/4.x/
*  https://pillow.readthedocs.io/en/stable/
*  https://www.codegrepper.com/code-examples/python/convert+video+to+frames+python+opencv
* https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/
* https://github.com/joelibaceta/video-to-ascii

An explanation video is present in the zip folder itself, in which I have briefly explained my project.
