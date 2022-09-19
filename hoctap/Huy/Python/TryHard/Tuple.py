#Khởi tạo tuple
print(tuple('BIMLab'))
#Sử dụng constructor Tuple (tuple(iterable))
tup = (i for i in range(10))
print(tuple(tup))

#Toán tử với Tuple
#Toán tử +
tup1=[1,2]
tup1 += (3,4)
print(tup1)
#Toán tử *
print(tup1 * 3)
#Toán tử in
bim = (1,0,2)
print(1 in bim)

#Indexing và cắt Tuple
tupl = (1, 2, 'a', 'b', [3, 4])
print(len(tupl),tupl[2],tupl[2:5],tupl[::-1])
#Thay đổi nội dung Tuple
'''
tupl[2]=3
print(tupl)
Lỗi - Không giống LIST (có thể thay đổi được)
'''
#Matrix
tupp = ((1, 2, 3), [4, 5])
print(tupp[0][0])

#hash object là một đối tượng bạn không thể thay đổi nội dung của nó
tupp[1][1]=4
print(tupp) #chỉ có thể thay đổi bên phải vì nó là 1 hashobject (list)

#Phương thức của Tuple
#Phương thức count
bimlab = (0, 3 , 9 , 7 , 9 ,4)
print(bimlab.count(9))
#Phương thức index (<Tuple>.index(sub[, start[, end]]))
print(bimlab.index(7))

'''
Khi nào thì chọn Tuple thay cho List?
Tuple khác List ở chỗ Tuple không cho phép bạn sửa chữa nội dung, còn List thì có. Vì đặc điểm đó, Tuple mạnh hơn List ở những điểm sau:

-> Tốc độ truy xuất của Tuple nhanh hơn so với List
-> Dung lượng chiếm trong bộ nhớ của Tuple nhỏ hơn so với List
-> Bảo vệ dữ liệu của bạn sẽ không bị thay đổi
-> Có thể dùng làm key của Dictonary 
(một kiểu dữ liệu sẽ được giới thiệu). Điều mà List không thể 
vì List là unhash object.
'''
