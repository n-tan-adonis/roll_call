# Attendance by Face Recognition

## Project Overview

### 1 Goal

The goal of this project is to digitize attendance at schools, instead of teachers taking attendance by "calling names" as usual. 


### 2 Dependencies

* Python
* Numpy
* Face_recognition
* OpenCV

### 3 Project Structure

* *face_recognition.py*: is a main program to run
* *pic2*: folder used for store images which recognize student face
* *diemdanh.csv*: csv file used for save datetime when student roll-call

### 4 Usage

* Dowload project
* Install library: OpenCV, face_recognition
* Add student's face images to recognize into *pic2* folder
* Run *face_recognition.py* to roll-call
<img width="929" alt="anh_test" src="https://github.com/n-tan-adonis/roll_call/assets/127659484/2242a627-48ae-448a-9a74-91259ff3d849">

* The program will automatically save the names of faces appearing in the frame. The program only saves the names and datetime of people who have not been saved in the text file
* Press "e" to finish running the program


### 5 Result

<img width="383" alt="text_file" src="https://github.com/n-tan-adonis/roll_call/assets/127659484/1738c616-dd45-44d1-ac20-7756d49478f0">

