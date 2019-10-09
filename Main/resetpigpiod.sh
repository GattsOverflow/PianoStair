echo "23" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio23/direction
gpio -g write 23 1


#echo "21" > /sys/class/gpio/export
#echo "out" > /sys/class/gpio/gpio21/direction
#gpio -g write 21 1
