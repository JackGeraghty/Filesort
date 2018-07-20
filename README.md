# Filesort
A short python script for sorting files into sub-folders based on prefixs.

## What is it?
At the end of my second year exams my desktop was littered with random lecture notes and assignments. Rather than just make a folder and sort them individually I decided to test out what I had learned about python during the year and write a script that would do it for me then and again anytime I needed to sort my university work.

## How does it work?
FileSort works by initially creating a text file in a main folder e.g. Computer Science. Then the user types in the names of the folders they want to split the files into, E.g.

- Data Structures
- Software Engineering Project
- Databases
- Unix Programming
- etc.

Once these are entered into the text file it's just a matter of having named the files to be sorted with the prefixs of the folder names. Then once the script is run again it will see that there is a filePrefixs.txt file and sort all the files into those specified folders.

**Notes** 
- It sorts the files that are on the desktop
- I am currently still working on improving it, I hope to add user specified directories for sorting and easier execution of the script. 
