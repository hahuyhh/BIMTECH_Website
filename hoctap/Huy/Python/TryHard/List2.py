#PART 2

a = [1,2,3,4,1,6,7,8,9,10]

#Phương thức count (đếm số lần xuất hiện của phần tử)
print(a.count(1))

#Phương thức index (tìm ra vị trí của phần tử) 
print(a.index(3)) 

m = '-------------------' 
print(m)

#Phương thức copy (hàm copy, tạo ra 1 bản sao)
b = a.copy()
b[0] = 'Hahuy'
print(a)
print(b)

#Phương thức clear
c = a.clear()
print(a)
print(c)

m = '-------------------' 
print(m)

#Các phương thức cập nhật
#Phương thức append
x = [1,3,5]
x.append(7)
print(x)

'''Khi ta append một list vào chính nó, thì trên thực tế,
nó sẽ tạo ra một vòng lặp vô tận.
Trong ví dụ trên, khi ta append a vào list a,
thì nó sẽ truy xuất giá trị của a để có thể append.
Nhưng vì giá trị của a đang được thay đổi, nên nó sẽ lại append trước khi truy xuất.
Điều này sẽ lặp lại mãi mãi vì giá trị a sẽ luôn luôn được thay đổi.
Kết quả [1, 2, [...]] chính là đại diện cho sự lặp vô tận đó.'''

#Phương thức extend (Thêm từng phần tử một của iterable vào cuối List.)
y = [1, 2, 3]
y.extend([[4,5],6,7])
print(y) #xem sự khác biệt giữa append và extend

#Phương thức insert (<list>.insert(i,x)) (Thêm phần x vào vị trí i ở trong List.)
z = [1, 2, 3]
z.insert(0,7)
print(z)

m = '-------------------' 
print(m)

#Phương thức pop (Bỏ đi phần tử thứ i trong List và trả về giá trị đó)
#<List>.pop([i])
t = [1, 2, 3]
print(t)
t0 = t.pop(1)
print(t)
print(t0)

#Phương thức remove (Bỏ đi phần tử đầu tiên trong List có giá trị x)
#<List>.remove(x)
u = [0, 1, 2, 1, 3]
#print(u)
u.remove(1)
print(u)

#Các phương thức xử lí
#Phương thức reverse (Đảo ngược các phần tử ở trong List)
#<List>.reverse()
v = [1,4,6,1,7]
v.reverse()
print(v)

#Phương thức sort (Sắp xếp các phần tử từ bé đến lớn bằng cách so sánh trực tiếp.)
#<List>.sort(key=None, reverse=False)
m = [1,4,6,1,7]
m.sort()
print(m)














