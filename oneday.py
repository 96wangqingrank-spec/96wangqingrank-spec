price_a = 120
price_b = 45
price_c = 105
if price_a >= 100:
    final_a = price_a - 20
else:
    final_a = price_a
if price_b >= 100:
    final_b = price_b - 20
else:
    final_b = price_b
if price_c >= 100:
    final_c = price_c - 20
else:
    final_c = price_c
total_pay = final_a + final_b + final_c
print(f"wqr最终应支付：{total_pay}元")
request_ip = "192.168.1.50"
request_text = "温馨提示：后台数据库危险操作"
if request_ip != "127.0.0.1":
    print("【系统提示】 检测到外网ip访问，进入安全审查...")
    if request_text == "温馨提示：后台数据库危险操作":
        print("【高危警告】检测到黑客攻击行为，已强行拦截！")






