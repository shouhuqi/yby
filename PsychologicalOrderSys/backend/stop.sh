pid=`netstat -anp | grep 5000 | awk '{print $7}' | awk -F'/' '{print $1}'`
echo $pid
kill -9 $pid
sleep 3
