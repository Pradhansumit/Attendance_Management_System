# Attendance Management System

Attendance Management Software is a system management software that helps in handling the attendance of students in a dense class with ease. 

## How does it work?

Well, in this faculty member login to the system and select the department (say, MCA), and then choose which division it is (eg., A ). Finally faculty member unlocks the slot (i.e., the subject which s/he is teaching). 

This opens the portal where student, now, can login to the system. They now can see the slot has been opened for the particular subject. Clicking on the [MARK] button, then can mark their attendance. 

Finally, the faculty member, after providing enough time to mark attendance, will lock the slot. 

While the slots are locked, student(s) trying to login to system will not be able to bypass the login. And will be given warning **ATTENDANCE SLOT IS LOCKED**

## Installation

Create a virtual environment using virtualenv

```bash
virtualenv env
```

Activate the environment using:

for windows:
```bash
env/Scripts/activate
```

for Linux:
```bash
source env/bin/activate
```

install the packages

```bash
pip install -r requirements.txt
```