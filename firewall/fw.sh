#!/bin/bash
NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)


red()
{
	echo -e "$RED$1$NORMAL"
}
yellow()
{
	echo -e "$YELLOW$1$NORMAL"
}
green()
{
	echo -e "$GREEN$1$NORMAL"
}
blue()
{
	echo -e "$BLUE$1$NORMAL"
}
magenta()
{
	echo -e "$MAGENTA$1$NORMAL"
}
cyan()
{
	echo -e "$CYAN$1$NORMAL"
}
catlog()
{
cyan "0:退出程序"
cyan "1:打开防火墙"
cyan "2:关闭防火墙"
cyan "3:防火墙状态"
cyan "4:开放某端口"

}
port_done()
{
	echo "请输入需要开放的端口"
}
while ((1))
do
catlog
read id;
if [ $id == 0 ]
then
	break
elif [ $id == 1 ]
then
	echo "cmd : systemctl start firewalld"
	# systemctl start firewalld
elif [ $id == 2 ]
then
	echo "cmd : systemctl stop firewalld"
	# systemctl stop firewalld
elif [ $id == 3 ]
then 
	echo "cmd : systemctl status firewalld"
	# systemctl status firewalld
elif [ $id == 4 ]
then
port_done
else
	echo "???"
fi
done

