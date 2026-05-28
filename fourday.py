def removeElement(nums,val):
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x
            k = k+1
    return k
print("挑战一:力扣第27题《移除元素》测试开始")
test_nums = [3,2,2,3,1,3.4]
bad_val = 3
result_k = removeElement(test_nums,bad_val)
print(f"1.过滤后剩下的合格品数量:{result_k}个")
print(f"2.提纯后的合格品列表展示:{test_nums[:result_k]}")
print("---------------------------------------------------")
print("--- ⚖️ 挑战二：力扣第 709 题《转换成小写字母》测试开始 ---")
def toLowerCase(s):
    result = ""
    for char in s:
        if "A" <= char <= "Z":
            lower_char = chr(ord(char) + 32)
            result = result + lower_char
        else:
            result = result + char
    return result
print("--- ⚖️ 挑战二：力扣第 709 题《转换成小写字母》测试开始 ---")
test_str = "Bigdta-Study-2026"
result_ek = toLowerCase(test_str)
print(f"原始文本为:{test_str}")
print(f"清洗后的数据为:{result_ek}")
    
