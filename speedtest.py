##
## Originally created by https://www.reddit.com/user/AlekseyP
## Seen at: https://www.reddit.com/r/technology/comments/43fi39/i_set_up_my_raspberry_pi_to_automatically_tweet
##

#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
 
#Configuration
# Twitter
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""
CONSUMER_KEY=""
CONSUMER_SECRET=""
# Minimum network speed
min_net_speed = 10
# Speedtest client absolute path
speedtest_path = "/home/pi/Scripts/SpeedTest/speedtest-cli"

def test():
 
        #run speedtest-cli
        print 'running test'
        a = os.popen("python %s --simple"%(speedtest_path)).read()
        print 'ran'
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u
        #save the data to file for local network plotting
      ##  out_file = open('/var/www/assets/data.csv', 'a')
      ##  writer = csv.writer(out_file)
      ##  writer.writerow((ts*1000,p,d,u))
      ##  out_file.close()
 
        my_auth = twitter.OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
        twit = twitter.Twitter(auth=my_auth)
 
        #try to tweet if speedtest couldnt even connet. Probably wont work if the internet is down
        if "Cannot" in a:
                try:
                        tweet="Hey @Comcast @ComcastCares why is my internet down? I pay for 150down\\10up in Washington DC? #comcastoutage #comcast"
                        twit.statuses.update(status=tweet)
##			print tweet
                except:
                        pass
 
        # tweet if down speed is less than whatever I set
        elif eval(d)<min_net_speed:
                print "trying to tweet"
                try:
                        # i know there must be a better way than to do (str(int(eval())))
                        tweet="Hey @Comcast why is my internet speed " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up when I pay for 150down\\10up in Washington DC? @ComcastCares @xfinity #comcast #speedtest"
                        twit.statuses.update(status=tweet)
##			print tweet
                except Exception,e:
                        print str(e)
                        pass
        return
       
if __name__ == '__main__':
        test()
        print 'completed'
