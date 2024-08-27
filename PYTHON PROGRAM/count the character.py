count_string = "captain america "
print("the original string is :"+str(count_string))
res = len([ele for ele in count_string if ele.isalpha()])
print("count alphabets :"+str(res))
