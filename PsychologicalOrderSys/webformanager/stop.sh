pid=`ps x | grep npm | grep -v "grep" |  awk '{print $1}'`
echo $pid
kill -9 $pid
sleep 3
