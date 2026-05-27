raw_logs = [
    "2026-5.27 10:00:01 INFO : 用户[张三]登录成功\n",
    "2026-5.27 10:01:45 ERROR: 数据库连接超时，尝试重连...\n",
    "2026-5.27 10:02:10 INFO: 商品数据流入 HDFS 成功\n",
    "2026-5.27 10:03:59 ERROR: 用户[李四]付款失败。余额不足！\n",
    "2026-5.27 10:05:00 INFO: 触发定时垃圾回收机制\n"
]
with open("server.log", "w", encoding="utf-8") as f_write:
    for line in raw_logs:
        f_write.write(line)
print("\n--- 步骤1:Linux原始日志`server.log`生成完毕 ---")
error_count = 0
print("\n步骤2 ：大数据清洗流水线启动")
with open ("server.log","r",encoding = "utf-8")as f_read:
    with open("clean_eerror.txt","w",encoding = "utf-8")as f_clean:
        for line in f_read:
            if "ERROR" in line:
                error_count = error_count +1
                f_clean.write(line)
                print(f"抓获内鬼数据 -> {line.strip}")
print(f"\n---步骤3:清洗聚合完毕！共抓获{error_count}条高危报错")



            



