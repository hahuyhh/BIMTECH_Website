#PART 2

#chuỗi trần, sử dụng thường xuyên khi làm việc với BIỂU THỨC CHÍNH QUY
print(r'Haizz, \neu mot ngay nao do')
m='------------------'
print(m)

x = 'có gì đâu'
y = 'mà thấy khó'

#Toán tử cộng (nối các chuỗi)
print(x + ' ' +y)
m='------------------'
print(m)

#Toán tử nhân (Giúp tạo ra 1 chuỗi lặp đi lặp lại số chuỗi)
print((x+' ')*4)
m='------------------'
print(m)

#Toán tử in (nhận 1 trong 2 đáp án TRUE or FALSE)
k = x in y
print(k)
m='------------------'
print(m)

#Indexing
h = y[3]
print(h)
m='------------------'
print(m)
#Cắt chuỗi
h = y[0:5]
j = y[0:None]
g = y[None:7:2]
print(h)
print(j)
print(g)
m='------------------'
print(m)

#Ép kiểu chuỗi -> số
a = int('69') + 5
print(a)
b = float('6.9') + 5
print(b)
#Ép kiểu số -> chuỗi
c = str(69) + '5'
print(c)
m='------------------'
print(m)

#INDEXING
strA = 'HaHuy'
#strA = strA[None:1] + '4' + strA[2:None]
print(strA.replace('a','4'))
print(hash(strA))
#Mã hash (hashable object là hằng, một giá trị không bao giờ thay đổi. Và có một vài trường hợp bắt buộc bạn phải sử dụng kiểu dữ liệu là hashable object điển hình như khóa (key) trong kiểu dữ liệu Dict của Python (một kiểu dữ liệu sẽ được Kteam giới thiệu ở bài DICTONARY TRONG PYTHON).)
