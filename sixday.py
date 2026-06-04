data_list = [
   {"id": "DEV-01", "flow": "350"},
    {"id": "DEV-02", "flow": "ERROR_ATTACK"},
    {"id": "DEV-03", "flow": "120"},
    {"id": "id-04", "flow": "0"},
    {"id": "DEV-05", "flow": "abc"}
           ]
ok_cnt = 0
err_cnt = 0
print("--- ⚖️ 步骤1：数据清洗流水线启动（全防御模式） ---")
with open("clear_db.txt","w",encoding = 'utf-8')as f_db:
    with open("alert.log","w",encoding = "utf-8")as f_err:
        for item in data_list:
            try:
                traffic = int(item["flow"])
                dev_id = item["id"]
                ok_cnt = ok_cnt + 1
                f_db.write(f"【设备:[{dev_id}]】安全洗净流量:{traffic}GB\n")
                print(f"【洗净】设备[{dev_id}]提纯流量 {traffic}GB 成功")
                
            except Exception as e:
                err_cnt = err_cnt + 1
                dev_id = item["id"]
                bad_raw = item["flow"]
                print(f"🚨【拦截】设备 [{dev_id}] 脏数据 [{bad_raw}]！原因: {e}")
                f_err.write(f"【高危】设备 [{dev_id}] 投毒数据 [{bad_raw}]，报错: {e}\n")
print(f"\n--- 📊 步骤2：流水线清洗报告 ---")
print(f"⚖️  洗净入库设备: {ok_cnt} 台")
print(f"🚨  成功拦截设备: {err_cnt} 台")
print("--- 系统稳健运行，未发生任何崩溃！第一阶段圆满通关！ ---")