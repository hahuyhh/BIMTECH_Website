#Phương thức tách chuỗi

#Phương thức split-rsplit (<chuỗi>.split(sep=None, maxsplit=-1))
a='BIMLab is a Building Infomation a Modeling'
print(a.split( ),'\n', a.split('a'))
#Phương thức splitlines (<chuỗi>.splitlines(keppends=False))
print('a\nb\nc\nd\ne'.splitlines()) #các phần tử được chia tách bằng “\n”
print('a\nb\nc\nd\ne'.splitlines(True)) #keppends được cung cấp giá trị True, các phần tử khi được phân tách cũng sẽ có kí tự “\n” theo sau.
#Phương thức partition-rpartition (<chuỗi>.partition(sep))
print(a.partition('a'))

#Phương thức tiện ích

#Phương thức count (<chuỗi>.count(sub, [start, [end]]))
x = 'BIMLabbalMIB'
print( x.count('B'),'\n',x.count('B',3),'\n',x.count('B',1,5))
#Phương thức startswith (<chuỗi>.startswith(prefix[, start[, end]]))
print(x.startswith('ab',4))
    #Trả về  giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix
#Phương thức endswith
print(x.endswith('IB',4))
    #Trả về  giá trị True nếu chuỗi đó kết thúc bằng chuỗi prefix
#Phương thức find-rfind (<chuỗi>.find(sub[, start[, end]]))
print(x.find('BI',3))
    #Nếu sub không có trong chuỗi, kết quả sẽ là -1
#Phương thức index-rindex (<chuỗi>.index(sub[, start[, end]]))
print(x.index('BI',0)) #Tương tự như index

#Các phương thức xác thực

#Phương thức islower (<chuỗi>.islower())
print('hahuy'.islower())
#Phương thức isupper (<chuỗi>.isupper())
print('HAHUY'.isupper())
#Phương thức istitle
print('Hahuy'.istitle())
#Phương thức isidentifier
print('_Client'.isidentifier(), 'code'.isidentifier(), '@ads'.isidentifier(), '25%'.isidentifier())
'''
- Chuỗi phải được bắt đầu bằng dấu gạch dưới (_) hoặc các kí tự chữ cái
- Chuỗi không được chứa bất kì khoảng trắng nào
- Không được chứa các kí tự đặc biệt (_, %, $, _...) 
ngoại trừ việc kí tự đầu tiên có thể là dấu gạch dưới.
'''
#Phương thức isdigit (<chuỗi>.isdigit()) ~ isnumeric
print('0123'.isdigit(), '123'.isdigit(), '-123'.isdigit())
#Phương thức isspace (<chuỗi>.isspace()) 
#->Trả về True nếu tất cả các kí tự trong chuỗi đều là kí tự khoảng trắng
print('    '.isspace(), '   h   '.isspace())
#Phương thức iskeyword (Thuộc thư viện keyword)
'''
import keyword
keyword.iskeyword(<chuỗi>)
'''
import keyword
print(keyword.iskeyword('def'),keyword.iskeyword('class'),keyword.iskeyword('clas'))

#Củng cố
s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
print(s.lower().lstrip('ao').rstrip('a').title())

print(s[12:-7].title())