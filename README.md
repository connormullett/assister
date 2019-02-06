
# Assister

Python CLI Tool to simplify computing and enhance productivity

## Coming Soon
- Todo
- Calculator
- Script Manager

## Prerequisites
- Git
- Python3
- virtualenv

## Install
- `git clone https://github.com/connormullett/assister.git`
- `cd assister`
- `virtualenv -p {/path/to/python3} venv`
- `source venv/bin/activate`
- `sh install.sh`

### Dependancies are currently in the process of being removed and will
### no longer need a virtualenv

Running the install steps will allow you to call `assister` from your terminal
You will also have a new `todo.csv` file in the project base directory. This will hold all of the todos

## Commands
### Example
`assister -t create` 

`-t` - manages todos
    - `view` - view todos
    - `del {todo_id}` - delete todo by id
    - `create` - create a todo using a series of prompts

### Upcoming commands
 - mark complete / incomplete
 - update elements

