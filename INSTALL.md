Step to install the Code

1. Create an organization on Github.
2. Create a repo in that organization. Make it public.
3. Find the big green CODE button. Create a new codespace on the main.
4. Check you have the latest Python (3.13)
   If not, then in the terminal, install python3.13 by running the following command (it is all on one line).
   sudo apt update -y; sudo  apt upgrade -y; sudo apt install software-properties-common -y; sudo add-apt-repository ppa:deadsnakes/ppa -y ; sudo apt update -y ; sudo apt install python3.13 -y
5. Then check you have python3.13 with the command below.
   python3.13 -B --version
6. Write a short Python program (10 lines) and add an error.
7. From the command line, run that file.
   python3 myfile.py
You should see errors on the command line.
8. VSCode should now be asking if you want Python support installed. Do it.
9. Run the code again. Take your mouse and point to one of the errors on the screen. Observe how it highlights like a hyperlink.
