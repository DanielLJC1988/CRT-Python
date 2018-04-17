import pymssql

conn = pymssql.connect(host="127.0.0.1:1433",user="sa",password="ex78684858EX",database="3GTraffic")
cur = conn.cursor()
if not cur:
    raise (NameError,"数据库连接失败")
date_start = input("请输入查询开始日期:(例如：2018-4-1):   ")
date_end = input("请输入查询结束日期:(例如：2018-4-30):   ")
cur.execute("select users,SUM(total)as 流量MB from TrafficCmiot where date >=" + "\'" + date_start + "\'" + " and date <=" + "\'" + date_end + "\'" + " group by users order by users")
resList = cur.fetchall()
conn.close()
for i in range(len(resList)):
	print(resList[i])
