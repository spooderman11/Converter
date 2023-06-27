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

import sys, subprocess, platform, time, os, imageio

class ConsoleClear:
    def clear(self):
        if platform.system() == "Windows":
            subprocess.call("cls", shell=True)
        else:
            subprocess.call("clear", shell=True)

try:
    imageio.plugins.ffmpeg.download()
except:
    pass

ConsoleClear().clear()
print("Welcome to spoodermans image/video to gif converter!")
time.sleep(3)
ConsoleClear().clear()

try:
    os.mkdir("files")
except:
    pass

input_file = input("Please enter the name of the image/video file you want to convert (including extension): ")
if not os.path.exists(f"files/{input_file}"):
    print("Error: File not found, please make sure the file is in the 'files' folder")
    sys.exit()

output_file = input("Please enter the name of the output gif file (including .gif extension): ")
if os.path.exists(f"files/{output_file}"):
    print("Error: File already exists, please choose a different name")
    sys.exit()
elif output_file[-4:] != ".gif":
    print("Error: File extension is not .gif, please add the .gif extension")
    sys.exit()

duration = input("Please enter the duration of each frame in milliseconds (if its a video, otherwise leave blank) (1000 = 1 second): ")

ConsoleClear().clear()

try:
    reader = imageio.get_reader(f"files/{input_file}")
    if duration == "":
        writer = imageio.get_writer(f"files/{output_file}")
    else:
        writer = imageio.get_writer(f"files/{output_file}", duration=float(duration)/1000)
    total_frames = reader.count_frames()
    for i, im in enumerate(reader):
        progress = (i + 1) / total_frames * 100
        sys.stdout.write('\r' + f"Converting... {i+1}/{total_frames} frames ({progress:.2f}%)")
        sys.stdout.flush()
        writer.append_data(im)
    writer.close()
    print("\nDone! Please check the following path for your gif: " + f"files/{output_file}")
    time.sleep(3)
    ConsoleClear().clear()
    print("Thank you for using spoodermans image/video to gif converter! You can now press the little enter key to exit")
    input("Press the little tiny enter key to exit")
except Exception as e:
    print("Error: ", e)
    sys.exit()
