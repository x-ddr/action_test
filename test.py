import os


Wps_id = os.environ['WPS_KEY']


print(Wps_id)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("test.txt", "w")
str = Wps_id
fo.write( str )

# 关闭文件
fo.close()