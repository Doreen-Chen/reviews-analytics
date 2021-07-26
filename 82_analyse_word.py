# 82. [程式練習] 一百萬筆留言中最常出現哪些字
# 
#
#   1)來源檔續用課程 54,55 的 reviews.txt
#     D:\Python\messages\reviews.txt
#
#   2)程式續用 55_read_message.py
#     D:\Python\Projects\reviews-analytics

# 每行留言存入清單
data = []  # 空清單
int_count = 0
with open('D:/Python/messages/reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

        #print(len(data))  # 印出目前解析筆數 # 但是印到CMD是耗資源的且會拖慢系統速度

        # 改成每10000筆再印出筆數
        int_count += 1
        if int_count % 100000 == 0:  # 餘數 %
            print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆')

# 印第一筆
print(data[0])
print('===========================================')




# 求平均長度
int_sum_len = 0
for s in data:
    int_sum_len += len(s)

print('總字數是 ', int_sum_len)
print('===========================================')
print('平均長度是', int_sum_len/len(data))
print('===========================================')

##### 56. 清單的篩選
# 篩選小於100字
lst_new = []
for s in data:
    if len(s) < 100:
        lst_new.append(s)

print('留言小於100字的筆數 :', len(lst_new), '筆')
print('===========================================')
#print(lst_new[0])


# 篩選字串裡關鍵字 : good
lst_good = []
for s in data:
    if 'good' in s:
        lst_good.append(s)
print('有關鍵字good的留言數 :', len(lst_good))
print('===========================================')



print('=== 以下是: 課程 82 文字計數 ========================================')
### 文字計數 ==> 課程 82 重點

# 新取得的word設定為Key,並開始計次
#     for loop逐一判斷是否有符合的字
wc = {} # word_count
int_word_count = 0
for d in data:
    words = d.split(' ') # 每行以空格分隔 # split回傳清單存入words
    #print(words)
    
    for word in words: # 讀取每行裡的每字
        ### 補充: Not用法 ==> if word not in wc:
        # 字如果
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  # add new key into wc(Dictionary)


# 印出統計結果
#print(wc)
int_loop = 0
for word in wc:
    # (1) 限制印前50筆
    #print('key--> ', word, '\t\tcount--> ', wc[word] )
    #int_loop += 1
    #if int_loop >= 50:
    #    break

    # (2) 印出筆數大於n
    if wc[word] >= 1000000:
        print('key--> ', word, '\t\tcount--> ', wc[word] )



# 印出 100萬筆留言有多少個字
print('100萬筆留言有多少個字: ', len(wc))
# 是否有key叫作'Doreen'
print(' Doreen 出現 ', wc['Doreen'], ' 次') # 有區分大小寫,用doreen查詢0筆

# 統計後,提供查詢
while True:
    #pass  # 程式迴圈什麼也不作, 僅先定義此架構
    query_word = input('請輸入欲查詢的字是 :')
    if query_word == 'q':
        print('感謝使用查詢功能, 查詢結束 !')
        break
    else:
        if query_word in wc:
            print( query_word, ' 在留言檔出現的次數為 ', wc[query_word])
        else:
            print( query_word, ' 在留言檔出現的次數為 0')





