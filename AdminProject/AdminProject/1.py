# @Time    : 2019/5/17 9:20
# @Author  : 唐文杰
# @File    : 1.py
# @Software: PyCharm

# data=range(1000)
# page_size=10
# while True:
#     small_page=input(">>>")
#     big_page
# #small_page page_size       #pagedata
# #1              10         data[0:100]
# #2              10         data[0:100]
# #11             10         data[100:200]
# #21             10         data[200:300]
data=range(1000)
page_size=8
while True:
    small_page=int(input(">>"))
    big_page=small_page/8
    if big_page==int(big_page):
        big_page=int(big_page)
    else:
        big_page=int(big_page)+1
    big_range_start=(big_page-1)*100
    big_range_end=big_page*100
    big_range=data[big_range_start:big_range_end]

    small_range_number=small_page%page_size
    if small_range_number:
        small_range_start=(small_range_number-1)*10
        small_range_end=small_range_number*10
    else:
        small_range_start=9*10
        small_range_end=10*10
    small_range=big_range[small_range_start:small_range_end]
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("small_page:%s"%small_page)
    print("big_page:%s"%big_page)
    print("big_range:%s"%str(list(big_range)))
    print("small_range:%s"%str(list(small_range)))


