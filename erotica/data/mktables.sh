#!/bin/bash

file=$1
dir=$2

cat $file | wordf | grep -v --text ",1\|,2\|,3\|,4\|,5\|,6\|,7\|,8\|,9\|,0\|the\|,be\|,to\|,of\|,and\|,a\|,in\|,that\|,have\|,i\|,it\|,for\|,not\|,on\|,with\|,he\|,as\|,you\|,do\|,at\|,this\|,but\|,his\|,by\|,from\|,they\|,we\|,say\|,her\|,she\|,or\|,an\|,will\|,my\|,one\|,all\|,would\|,there\|,their\|,what\|,so\|,up\|,out\|,if\|,about\|,who\|,get\|,which\|,go\|,me\|,when\|,make\|,can\|,like\|,time\|,no\|,just\|,him\|,know\|,take\|,person\|,into\|,year\|,your\|,good\|,some\|,could\|,them\|,see\|,other\|,than\|,then\|,now\|,look\|,only\|,come\|,its\|,over\|,think\|,also\|,back\|,after\|,use\|,two\|,how\|,our\|,work\|,first\|,well\|,way\|,even\|,new\|,want\|,because\|,any\|,these\|,give\|,day\|,most\|,us\|,was\|,had\|,-\|,same" > $dir/$(basename $file)
