#Các phương thức biến đổi
HH = 'BIMLab in SG'
#capitalize
print(HH.capitalize())
#upper
print(HH.upper())
#Lower
print(HH.lower())
#Swapcase
print(HH.swapcase())
#Title
print(HH.title())
#Các phương thức định dạng 
#Center (<chuỗi>.center(width, [fillchar]))
print('HH'.center(10,'h'))
#Rjust - Ljust (<chuỗi>.rjust(width, [fillchar]))
print('HH'.ljust(10,'h'))
#Phương thức xử lí (<chuỗi>.encode(encoding=’utf-8’, errors=’strict’))
ec = 'Một hai ba bốn năm sáu'.encode()
print(ec)
    #Các tham số (encoding, error) cũng tương tự như với phương thức encode.
#Phương thức decode(<chuỗi (đã mã hóa)>.decode(encoding=’utf-8’, errors=’strict’))
print(ec.decode())
#Phương thức join (<kí tự nối>.join(<iterable>)) -  các phần tử trong iterable buộc phải "thuộc lớp str"
print(' '.join(['1', '2', '3'])) # iterable ở đây là list ['1', '2', '3'])
print(' '.join((('1', '2', '3')))) # iterable ở đây là tuple ['1', '2', '3'])
#Phương thức replace (<chuỗi>.replace(old, new, [count]))
print('BIMLab is my home'.replace('home', 'house'))
print("Call it BIM, don't call it BIMer because it doesn't make sense".replace('BIM', 'BIMLab', 1))
#Phương thức strip (<chuỗi>.strip([chars]))
print('hahuyahhh'.strip('h')) #đầu-cuối
#Phương thức rstrip-lstrip (<chuỗi>.rstrip-lstrip)
print('hhhhhhhhahuyyyy'.lstrip('h'))
#Phương thức removeprefix (<chuỗi>.removeprefix([prefix]))
    #khắc phục cho pt lstrip
print('hhhhhhhhahuy'.removeprefix('hhhhhhh'))
#Phương thức removesuffix (<chuỗi>.removesuffix([suffix]))
    #khắc phục cho pt rstrip
print('hahuyyyy'.removesuffix('yyy'))