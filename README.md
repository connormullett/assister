
# Assister

Python CLI Tool to simplify computing and enhance productivity

## Coming Soon
- [ ] WebScraper
- [ ]Folder remover

## Prerequisites
- Git (if contributing)
- Python3

## Install

`pip install assister`

If you would like to contribute  
- fork the repository and run the following commands after cloning
- `python3 setup.py install`
- `python3 setup.py -e .`

Running the install steps will allow you to call `ass` from your terminal

## Commands
### Examples
example command - `ass todo create` 

- `TODO` manages todos  
    - `view` - view todos  
    - `del {todo_id}` - delete todo by id  
    - `create` - create a todo using a series of prompts  
    - `mc {todo_id}` - mark todo complete  
    - `mi {todo_id}` - mark todo incomplete  
- `API` consume APIS, Headers optional
    - `get {url} {headers}`
    - `post {url} {body} {headers}`
    - `put {url} {body} {headers}`
    - `del {url} {body} {headers}`
- `DIR` build directories  
    - `dir {folder name} {files}`  
        - where files can be as many as needed  
    - Other commands coming soon  

