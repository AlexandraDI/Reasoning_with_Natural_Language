
# Natural Language Reasoner

This project researches the task of reasoning with constrained natural language (CNL).

## Setup

In order to run this project you can either use docker or install the dependencies
and run the app.py file.  

This project was made in python 3.8.8 no other versions were tested.   
In order to install the dependencies run:  
`pip install -r requirements.txt`

With the command:  
`python ./src/app.py`  
you can start the local server.

You can also use the docker to run the server.

## Changes on the Web Interface

The web interface is setup as a Vue.js project and lies in the folder clr-client. In order to start the development server, install npm and the required dependencies and execute `npm run serve` in the nlr-client folder. To apply these changes to the python server, please execute the script build_prod_and_copy_to_server.cmd. This compiles the Vue project and copies the results into the python server project so that the server can deliver it.

# [Project Report](https://github.com/AlexandraDI/Reasoning_with_Natural_Language/blob/master/Reasoning__with_NL_Report.pdf)
https://github.com/AlexandraDI/Reasoning_with_Natural_Language/blob/master/Reasoning__with_NL_Report.pdf
