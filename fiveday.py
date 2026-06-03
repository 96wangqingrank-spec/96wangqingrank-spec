data_stream = ["120","45","ERROR","105","abc"]
print("-- ⚖️ 步骤1：大数据高并发清洗线启动（神盾局防御模式） --")
with open("hack_alert.txt","a",encoding = "utf-8")as f_alert:
    for data in data_stream:
        try:
            clean_number = int(data)
            print(f"【正常入库】提纯后的数字资产:{clean_number}")
        except Exception as e:
            print(f"【拦截成功】发现投毒数据[{data}]!报错原因:{e}")
            f_alert.write(f"警告：检测到非法数据[{data}],底层错误类型:{e}\n")
print("\n--- 📊 步骤2：全量数据流处理完毕，系统稳健运行，未发生崩溃！ ---")



                             

