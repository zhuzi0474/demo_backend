### This is the back_end of the interview task
    1. Adopted tornado which is a python based web framework,
	   and I enhanced it to handle web requests with coroutine and multi threads python features.
    2. I wrote one ut case and one interation test for this app, sure they are quit simple.
    3. CRUD data are stored in memory. So if we restart tornado server, we gonna lose the data.
    4. There are two design patterns here,
	   a. Factory pattern: I establish a configuration factory to satisfy multi deploy envrionments.
	   b. Decretor pattern: I wrote a decretor to monitor code execution efficiency.
    5. I set up a Jenkins locally, and created a pipeline for this app. You can see the jenkinsfile in the root
       Directory. With that I deployed app to my personal aws ec2 instance.
    6. Cause’s it’s quit simple, I didn’t adopte inheritance, polymorphism etc. Object oriented technologies here,
       Sorry about that.
    7. front_end: https://github.com/zhuzi0474/demo_frontend
