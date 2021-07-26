# 55.[程式練習] 留言分析程式 & 56. 清單的篩選 & 57. [微進階!] List Comprehension (清單快寫法)

data = []  # 空清單
int_count = 0
with open('D:/Python/messages/reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

        #print(len(data))  # 印出目前解析筆數  # 但是印到CMD是耗資源的且會拖慢系統速度

        # 改成每10000筆再印出筆數
        int_count += 1
        if int_count % 100000 == 0:  # 餘數 %
            print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆')
# 印出 list 長度
#print(len(data))
# 印出 list 所有內容 --> 不要隨便使用
#print(data)
# 印出 index=0 element
#print(data[0])  
#print('---------------------')
# 印出 index=1 element
#print(data[1])

# 求平均長度
int_sum_len = 0
for s in data:
    int_sum_len += len(s)

print('總字數是 ', int_sum_len)
print('---------------------')
print('平均長度是', int_sum_len/len(data))
print('---------------------')

##### 56. 清單的篩選
# 篩選小於100字
lst_new = []
for s in data:
    if len(s) < 100:
        lst_new.append(s)

print('留言小於100字的筆數 :', len(lst_new), '筆')
print('---------------------')
#print(lst_new[0])


# 篩選字串裡關鍵字 : good
lst_good = []
for s in data:
    if 'good' in s:
        lst_good.append(s)
print('有關鍵字good的留言數 :', len(lst_good))
print('---------------------')
#print(lst_good[0])


##### 57. [微進階!] List Comprehension (清單快寫法)
#  說明
#               運算         變數        清單        篩選條件
#                ↓            ↓           ↓            ↓
#  output = [(number-1) for number in reference if number %2 == 0]
#  完全取代前述篩選的4行程式
#
lst_good = [s for s in data if 'good' in s]  # 第1個s即 append(s)的s
print('list comprehension 有關鍵字good的留言數 :', len(lst_good))
print('---------------------')

# 更改運算 : 每筆留言是否有'bad', 將True/False放在 lst_bad中, 筆數仍會是100萬筆
lst_bad = ['bad' in s for s in data]  # 後面沒有篩選, 所以100萬筆都會判斷
print('關鍵字bad留言數', len(lst_bad), '筆')
