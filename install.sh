
pip3 install -e .
pip install -r requirements.txt
touch assister/todo.csv
chmod 644 assister/todo.csv
echo 'id, title, content, complete, due' > assister/todo.csv

