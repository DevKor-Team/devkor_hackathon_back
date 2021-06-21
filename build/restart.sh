pid=`sudo netstat -tnlp | grep :8000 | awk '{ print $7 }' | cut -f 1 -d '/'`
kill -9 $pid
python3 manage.py runserver
