"""
    Source code for spoodermans image/video to gif converter

    This code is licensed under the MIT license, please see the LICENSE file for more information
    The code under is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
    In no event shall the authors or copyright holders be liable for any claim, damages or other liability.
    You are free to modify the code, as long as you give credit to the original author(s) and provide a link to the original source code.

    Explanation of the code:
    This code is a simple image/video to gif converter, it uses the imageio package to convert the image/video to a gif
    The code is pretty simple, it first checks if the imageio package is installed, if not it will ask you if you want to install it
    If you choose to install it, it will check if you are on windows or linux, and then install the package using pip or pip3
    After that it will check if the 'files' folder exists, if not it will create it and tell you to put your files in there
    If the folder exists it will ask you for the file name of the image/video you want to convert, and the name of the gif you want to create
    It will then check if the output file already exists, if it does it will tell you to choose a different name
    It will also check if the output file has the .gif extension, if it doesn't it will tell you to add the .gif extension
    After that it will ask you for the duration of each frame in milliseconds, if you leave it blank it will use the default duration
    Then it will check if the input file exists, if it doesn't it will tell you that the file doesn't exist
    If the file exists it will start converting the image/video to a gif, it will show you the progress in the console
    After it is done it will tell you where the gif is located, and then it will exit
    And finally it will thank you for using the program

    If you have any questions, feel free to contact me on discord: @copyrightclaim.
"""


import sys, subprocess, platform, time, os

class ConsoleClear:
    def clear(self):
        if platform.system() == "Windows":
            subprocess.call("cls", shell=True)
        else:
            subprocess.call("clear", shell=True)

try:
    import imageio
except ImportError:
    print("Package(s) missing, would you like to install them? (y/n)")
    install = input("Install?(y/n): ")
    if install == "y":
        if platform.system() == "Windows":
            subprocess.call("pip install imageio", shell=True)
            subprocess.call("pip install imageio[ffmpeg]", shell=True)
            ConsoleClear().clear()
            try:
                import imageio
                pass
            except ImportError:
                print("Error: Package(s) not installed, please install them manually")
                sys.exit()
        else:
            subprocess.call("pip3 install imageio", shell=True)
            subprocess.call("pip3 install imageio[ffmpeg]", shell=True)
            ConsoleClear().clear()
            try:
                import imageio
                pass
            except ImportError:
                print("Error: Package(s) not installed, please install them manually")
                sys.exit()
    else:
        sys.exit()

ConsoleClear().clear()
print("Welcome to spoodermans image/video to gif converter!")

time.sleep(3)

ConsoleClear().clear()

try:
    print("checking for PATH...")
    if not os.path.exists("files"):
        os.mkdir("files")
        print("PATH not found, PATH has been created, please put your files in the 'files' folder")
        time.sleep(3)
        sys.exit()
    else:
        print("PATH found!")
        ConsoleClear().clear()
        pass    
except Exception as e:
    print("Error: ", e)
    sys.exit()


print("Please enter the file name that you put in the 'files' folder")
print("Example: 'spooderman.jpg' or 'spooderman.mp4'")
try:
    input_file = input("File name: ")
except KeyboardInterrupt:
    ConsoleClear().clear()
    print("\nKeyboardInterrupt, exiting...")
    sys.exit()

ConsoleClear().clear()

print("Please enter the name of the gif you want to create")
print("Example: 'spooderman.gif'")
try:
    output_file = input("File name: ")
except KeyboardInterrupt:
    ConsoleClear().clear()
    print("\nKeyboardInterrupt, exiting...")
    sys.exit()

# output file exists check
try:
    open("files/" + output_file)
    ConsoleClear().clear()
    print("Error: File already exists, please choose a different name")
    sys.exit()
except FileNotFoundError:
    pass

# extension check
if output_file[-4:] != ".gif":
    ConsoleClear().clear()
    print("Error: File extension is not .gif, please add the .gif extension")
    sys.exit()

ConsoleClear().clear()

try:
    duration = input("Please enter the duration of each frame in milliseconds (if its a video, otherwise leave blank) (1000 = 1 second): ")
except KeyboardInterrupt:
    ConsoleClear().clear()
    print("\nKeyboardInterrupt, exiting...")
    sys.exit()

ConsoleClear().clear()

try:
    reader = imageio.get_reader("files/" + input_file)
except Exception as e:
    print("Error: ", e)
    sys.exit()

if duration == "":
    writer = imageio.get_writer("files/" + output_file)
else:
    writer = imageio.get_writer("files/" + output_file, duration=float(duration)/1000)

for i,im in enumerate(reader):
    sys.stdout.write('\r' + "Converting... " + str(i) + " frames. Do not panic if it looks like its stuck. (note: Interupting the process will result in a corrupt gif)")
    sys.stdout.flush()
    writer.append_data(im)

writer.close()
print("\nDone! Please check the following path for your gif: " + "files/" + output_file)
time.sleep(3)
ConsoleClear().clear()
print("Thank you for using spoodermans image/video to gif converter! You can now press the little enter key to exit")
input("Press the little tiny enter key to exit")
