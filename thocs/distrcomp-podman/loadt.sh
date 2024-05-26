max=100000
for i in `seq 2 $max`
do
  curl http://localhost:8080 > /dev/null
done
