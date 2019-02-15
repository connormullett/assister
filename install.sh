
pip3 install -e .
pip3 install -r requirements.txt
touch assister/todo.csv
chmod 644 assister/todo.csv
echo 'title, content, complete, due' > assister/todo.csv

