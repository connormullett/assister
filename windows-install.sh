
pip3 install -e .
pip3 install -r requirements.txt
$path='./assister/'
$file='todo.csv'
New-Item -path $path -Name $file -Value 'title,content,complete,due'

