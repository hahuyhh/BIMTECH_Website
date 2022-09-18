#Các phương thức tiện ích

#Phương thức count (<List>.count(sub, [start, [end]]))
print([[1, 5, 1, 6, 2, 7].count(5)])
#Phương thức index (<List>.index(sub[, start[, end]]))
print([[1, 5, 1, 6, 2, 7].index(6)])
#Phương thức copy(<List>.copy())
a = [1, 5, 1, 6, 2, 7]
b=a.copy()
b[1]=1
print(b,a)
#Phương thức clear(<List>.clear())
print([1, 5, 1, 6, 2, 7].clear())

#Các phương thức cập nhật
#Phương thức append(<List>.append(x))
z=['B','I','M','L','a']
print(z.append('b'),z)
x = [1,2]
print(x.append(3),x)
#Phương thức extend (<List>.extend(iterable))
print(x.extend('b'),x)
print(x.extend([[5,6],'c']),x)
#Phương thức insert (<List>.insert (i, x))
print(x.insert(5,6),x) # thêm phần tử 8 vào trong List kteam ở vị trí 5
y=[1, 2, 3]
print(y.insert(-1, 4),y) # thêm vào vị trí (-1 – 1) là -2
#Phương thức pop (<List>.pop([i]))
t=[1,2, 3, 5, 6]
print(t.pop(-3),t)
#Phương thức remove (<List>.remove(x))
u=[1, 5, 6, 2, 1, 7]
print(u.remove(5),u)

#Các phương thức xử lí

#Phương thức reverse(<List>.reverse())
print(u.reverse(),u)
#Phương thức sort (<List>.sort(key=None, reverse=False))
print(u.sort(reverse=False),u)
'''
False nhỏ > lớn
True lớn > nhỏ
# không đưa giá trị cho reverse thì mặc định là False
'''
lst = ['a', 1, 'b', 2, 2, 'b']
print(lst.sort(key=str),lst)

#Củng cố
'''
1 Chuyện gì xảy ra khi ta dùng phương thức pop lên một List rỗng
--> Kết quả trả ra là rỗng
2 Ta có thể sắp xếp được List dưới đây bằng phương thức sort hay không?
--> được 
'''
ex = [[1, 2], ['abc', 'def']]
print(ex.sort(key=len),ex)