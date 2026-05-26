def calculate_double_11(goods_name,original_price):
    if original_price >= 100:
        final_price = original_price - 20
        print(f"【系统提示】商品[{goods_name}]满100减20成功!")
    else:
        final_price = original_price
        print(f"【系统提示】商品[{goods_name}]未满100，维持原价")
    return final_price
print("---欢迎使用拼多多大数据价格计算引擎")
price1 = calculate_double_11("极寒羽绒服",159)
print(f"最终付款额 1:{price1}元\n")
price2 = calculate_double_11("纯棉防臭袜",25)
print(f"最终付款额 2:{price2}元\n")
price3 = calculate_double_11("机械键盘",299)
print(f"最终付款额 3:{price3}元\n")



       
       