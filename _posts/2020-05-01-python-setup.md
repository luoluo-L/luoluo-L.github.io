---
title: 'Automatic python script start setup'
date: 2020-05-01
permalink: /posts/2020/05/blog-post-1/
tags:
  - automatic start
  - task scheduler
  - bat
  - Windows
---

A simple tutorial on how to host a python service on a server using bat script and task scheduler.

Automatic start method
======
There are two major steps to achieve this. 1: Write a .bat file; 2. Set up windows task scheduler

Step1: Prepare Bat File
======

Following examples with virtual environment created by anaconda, with python installed under virtual environment. 

1.1 identify virtual enviroment dir
------
Open anaconda prompt, and type:
```conda env list```, to view the virtual environment names and pathes.


1.2 identify the path of activate.bat in virtual envoriment. 
------
In windows, it is usually under ```env_dir\Lib\venv\scripts\nt```.
In Linux system, this file is usually under ```env_dir\Scripts```.

1.3 identify python path 
------
```python where```

1.4 Set up Bat Script
------
We here provide a sample Bat Script ```foo.bat``` to help you set up.

```bat
REM reset path and activate the virtual environment 
set original_dir = %CD%
REM os
set venv_root_dir= "virtual env path from 1.1\Lib\venv\scripts\nt"
cd %venv_root_dir%
call %venv_root_dir%\activate.bat

REM run python under the virtual environment 
Path_to_anaconda\Anaconda3\envs\virtual_env_name\python.exe 
```
Since windows cannot automatically change disk, if python env is installed 
in a different disk than the python code. Then manually switching is needed.
For example, python code is under D disk and env is under C disk, here we do: ```D:``` before running the python code. 

```bat
REM run the python code
Path_to_code\sample_code.py

REM Deactivate the environment
call %venv_root_dir%\deactivate.bat
cd original_dir
exit /B 1
```

1.5 Debugging tips
------
- Close python program. Double click the bat file and see whether it will automatically triggers the program before move 
to next steps.
- If it doesn't work, copy .bat file command line  by line to Command window(CMD) and debug thru error messages.
- Common issues: incorrect path settings;
  some packages in virtual enviroment may crushes and usually reinstalling them will solve the problem. 


Step2: Step up windows task Scheduler
======
2.1. Open **Task Scheduler** App, select **Actions: Create Task**. 

2.2 In pop-up window, fill in task details including **Name, Description, Security Options**.

2.3 Select Triggers (add **New**) and from **Begin the task** dropdown manu, select **At startup**.

2.4 Select **Actions** tabl, select **New** and 
**add an action: Start a program**.

Select **Browse** and add the path of the bat file.


Done! Congrats! You can restart your computer and test.