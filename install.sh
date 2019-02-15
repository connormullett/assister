
pip3 install -e --user .
pip3 install -r requirements.txt
touch assister/todo.csv
chmod 0755 assister/todo.csv
echo 'title, content, complete, due' > assister/todo.csv

