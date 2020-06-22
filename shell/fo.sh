#! /bin/bash

# ==================
hint()
{
    echo 使用方法
    echo 
    echo cpp/c: fo FILENAME EXENAME 
    echo "  fo 1.cpp 1 ==> g++ -g -o 1 1.cpp"
    echo 
    echo py:    fo  FILENAME Version
    echo "  fo 1.py 2 ==> python 1.py"
    echo "  fo 1.py 3 ==> python3 1.py"
    echo
    echo sh:    fo FILENAME 
    echo "  fo 1.sh ===> sh 1.sh"
    echo
    echo php:   fo FILENAME 
    echo "  fo 1.php ===> php 1.php"
    echo
}
!
# ==================
# 判断是否有参数
if [ ! $1 ];then
    echo "[-] No usage...."
    hint
    exit 0
fi

# ==================
# get suffix
Name=$1
li=(${Name//./ })
suffix=(${li[-1]})


echo "[+] Runing $suffix file...."

if [ "$suffix" = "cpp" ];then
    echo cpp coming 
    g++ -g -o $2 $1
elif [ "$suffix" = "c" ];then
    g++ -g -o $2 $1
elif [ "$suffix" = "py" ];then
    if [ "$2" = 2 ];then
        python $1
    elif [ "$2" = 3 ];then
        python3 $1
    else
        echo "[-] FILE ERROR!!!"
    fi
elif [ "$suffix" = "sh" ];then
    sh $1
elif [ "$suffix" = "php" ];then
    php $1
else
    echo "[-] FILETYPE ERROR"
fi
