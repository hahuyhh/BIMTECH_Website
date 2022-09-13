#PART 3
#Toán tử %s, %d
a = 'My name is %s'%('Hahuy')
print(a)

s = '%s %d %.2f%s'
result = s%('Có',3,0.25,'kđ') 
print(result)
 # %d không phù hợp cho số thực --> dùng %f,%f có khả năng làm tròn lấy số thực, rút gọn số thập phân (%2.f)

#Định dạng bằng chuỗi f(f-string)

m='------------------'
print(m)

# f'gttri trong chuỗi' - Maybe thay thế được cho format nhưng không nhanh bằng
print(f'a\tb')

# Khác biệt
HH = 'HaHuy'
result = f'{HH} - okelah chưa'
print(result)
# Vidu
name = ''
address = ''
phone = ''
result = f'Student:{{name}}\nAddress:{{address}}\nPhone:{{phone}}'
print(result)

m='------------------'
print(m)

#Định dạng bằng format - tốt về nội dung, thẩm mỹ
#Với format không quá khắc khe như các toán thử %s %d mà có thể cho dư giá trị
print('only one value: {},{}'.format(1,2))

#Căn lề
	#Căn lề trái: {:(c)<n}
	#Căn lề giữa: {:(c)^n}
	#Căn lề phải: {:(c)>n}
a ='+ {:-<10} + {:-^20} + {:->15} +'.format('','','')
b ='| {: <10} | {: ^20} | {: >15} |\n'*3
d= (a + '\n' + b.format('ID','HOVATEN','NOISINH','123','HAHUY','BIENHOA','321','HUYHA','DONGNAI') + a)
print(d)