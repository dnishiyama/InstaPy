#!/bin/bash
source /home/ubuntu/.cronrc
cd /home/ubuntu/InstaPy
/home/ubuntu/anaconda3/bin/python ./etymologyexplorer.py > /home/ubuntu/InstaPy/logs/cron_log 2>/home/ubuntu/InstaPy/logs/cron_log
