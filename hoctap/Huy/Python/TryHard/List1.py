#Khởi tạo list

#List Comprehension
print([ha for ha in range(3)])
print([[n,n**2,n**3] for n in range(1,6)])
#Constructor List (list (iterable))
print(list('BIMLab-baLMIB'))

#Toán tử với List

#Indexing & cắt List
lst = 'baLMIB'
print(list(lst)[::-1])
#Thay đổi nội dung List
lst = [1, 'two', 3]
lst[1]=2
print(lst)
#Ma trận
lst = [[1, 2, 3], [4, 5, 6]]
print(lst[0][0:2])
'Không được phép gán List này qua List kia nếu không có chủ đích'
#Toán tử is -> Kiểm tra A và B có cùng chỉ đến 1 đối tượng không
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #-> không cùng chỉ đến 1 đối tượng
'----------------'
a=b
print(a is b)#-> cùng chỉ đến 1 đối tượng
'''Nếu 2 biến cùng chỉ đến 1 đối tượng thì việc thay đổi giá
trị bên trong 1 biến thì biến kia cũng thay đổi. Nhưng nếu thay đổi
hoàn toàn 1 trong 2 biến thì biến còn lại sẽ không thay đổi 
-> do vậy chúng ta nên copy list'''
lstt = [[1, 2, 3], [4, 5, 6]]
lst_copy_1 = lstt[:]
lst_copy_1[0] = 'ok'
print(lst_copy_1,'\n',lstt)
'Nhưng nếu thay đổi giá trị bên trong thì biến đầu tiên cũng sẽ bị ảnh hưởng'
lstt = [[1, 2, 3], [4, 5, 6]]
lst_copy_1 = lstt[:]
lst_copy_1[0][1] = 'two'
print(lst_copy_1,'\n',lstt)

#Củng cố
'''
Tìm các cách khởi tạo List hợp lệ dưới đấy
 -list(list(list('abc'))
 -[1, 2, 3] + list(4)
 --list()
 --[0] * 3
'''
# Với chuỗi s dưới đây lấy mật mã, biết mật mã nằm giữa && và %%
s = 'aaaaaaaAAAAAa&&&&TTT%%%aa//12312&ABC%%3//000000//&&TTT%%abcxyznontqfadf'
#NHỚ QUAY LẠI LÀM
'''
Cái này em chạy O(n) là giải ra. Cho vòng while điều kiện len(str) > 4,
mỗi vòng lặp split chuỗi đầu tiên hợp điều kiện, 
lưu vào mảng sau đó tạo chuỗi mới bỏ str đầu ra
'''