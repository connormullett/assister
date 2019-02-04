
pip3 install -e --user .
pip3 install -r requirements.txt --user
touch assister/todo.csv
chmod 644 assister/todo.csv
echo 'title, content, complete, due' > assister/todo.csv

