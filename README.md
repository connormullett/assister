
# Assister

Python CLI Tool to simplify computing and enhance productivity

## Coming Soon
- Todo
- Directory Building tool
- API Consumption tool (similar to curl)
- WebScraper

## Prerequisites
- Git
- Python3

## Install

- `git clone https://github.com/connormullett/assister.git`
- `cd assister`
- `sudo python3 setup.py install`
- `sudo pip3 install -e .`



Running the install steps will allow you to call `assister` from your terminal
You will also have a new `todo.csv` file in the project base directory. This will hold all of the todos

## Commands
### Examples
example command - `ass todo create` 

- `TODO` manages todos  
    - `view` - view todos  
    - `del {todo_id}` - delete todo by id  
    - `create` - create a todo using a series of prompts  
    - `mc {todo_id}` - mark todo complete  
    - `mi {todo_id}` - mark todo incomplete  
- `API` consume APIS  
    - `get {url} {headers}` - perform a get request to target url  
    - Other commands are not complete  
- `DIR` build directories  
    - `dir {folder name} {files}`  
        - where files can be as many as needed  
    - Other commands coming soon  

