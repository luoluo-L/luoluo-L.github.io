---
title: 'Chat-GPT assists programming tasks (a simple demo included)'
date: 2023-02-15
permalink: /posts/2023/02/blog-post-1
tags:
  - cool posts
  - category1
  - category2
---

How Chat-gpt from Open-AI going to affect our day-to-day work?

If you need to program in your day to day work, consider having ChatGPT as part of it.
If you have not tried it yet, it will be fun to give it a try! 
**Chat-GPT can help you write and Debug code!**

Here is a figure comparing conventional developer workflow. 

<br/><img src='/images/chat_gpt/flowchart_chatgpt_program.png' width="500" >


Demo time :) 
---
A simple task is used to test the ability of ChatGPT. The task is to ask ChatGPT to generate **an index page of a folder of html web pages** by automatically looping the html files of a specified folder. 

I create a simulation as the following: 

1. ask chat-GPT to generate a sample html webpage file. Here is the output of that file.

<br/><img src='/images/chat_gpt/example.PNG' width="500" >

2. generate multiple coples of the sample file and put it in a folder named ``` test_folder_html_files ```. 
  
  ``` test_folder_html_files ```
   <br/>``` --> sample_html_1.html ```
   <br/>``` --> sample_html_2.html ```
   <br/>``` --> sample_html_3.html ```
   <br/> ``` --> sample_html_4.html ```
    

 <!-- Here is a picture of the example folder:
 
  <br/><img src='/images/chat_gpt/folder.PNG' width = "300"> 
-->
 
 Next, I start with 

 <br/><img src='/images/chat_gpt/chat_gpt_request.PNG' width = "500"> 

 
3. Here is the generated index page after running the python code ChatGPT creates:

 <br/><img src='/images/chat_gpt/first.PNG' width = "500"> 


4. It looks great!! However, **BUG** find by clicking it!
 <br/><img src='/images/chat_gpt/not_found.PNG' width = "500"> 


5. I checkek and the problem for providing the path incorrectly. 

6. Debug through chatGPT by asking for fixing the problem by providing the absolute path.

 <br/><img src='/images/chat_gpt/chat_gpt_debug.PNG' width = "500"> 

Bug fixed! Index page successfully links to webpages!

 <br/><img src='/images/chat_gpt/first.PNG' width = "300">  <img src='/images/chat_gpt/revisied.PNG' width = "300"> 
