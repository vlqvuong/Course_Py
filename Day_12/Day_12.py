# Scope: 

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# lệnh in đầu tiên kết quả là 2 còn lệnh in thứ 2 thì kết quả là 1.

# Local Scope: Nếu tạo 1 biến nằm trong 1 Function thì biến đó chỉ có giá trị bên trong function đó, còn nếu ở ngoài function ta gọi biến đó ra thì sẽ có lỗi name error: và lý do là không thể xác định được tên biến đó. Local Scope tồn tại cùng với 1 function
# Nếu bạn tạo 1 biến nằm bên trong 1 function nào đó, biến đó chỉ có thể sử dụng bên trong function đó mà thôi.

# Global Scope: Ta có 1 biến được tạo ở bên ngoài function, biến đó có thể sử dụng cả bên trong funcion đó được, đó gọi là Global Scope. Nhưng ta không thể thực hiện các thao tác khác làm thay đổi giá trị của biến đó được, vì khi muốn thay đổi giá trị của biến trong function, bắt buộc ta phải khai báo biến đó ở trong function đó, khi đó biến được khai báo sẽ khác với biến ta muốn thay đổi.

# Vì vậy modify global scope bên trong 1 function nào đó, ta thực hiện như sau:

# change = 1
# def increase_change():
#   global change
#   change += 1
# increase_change()
# print(change)
# change bây giờ có thể được modify bên trong function, và khi ta in giá trị change thì nó có giá trị như khi ta thay đổi trong function modify_change

# Nhưng ta nên hạn chế dùng modify global scope vì rất dễ gây nên lỗi và bug. Khi cần thay đổi global scope bằng function ta nên dùng return. Chẳng hạn:

# change = 1
# def increase_change():
#   return change + 1
# change = increase_change()
# print(change)

# Nó có kết quả tương tự. và mỗi lần muốn thay đổi, ta chỉ đơn giản gọi hàm increase_change ra mà thôi, và ta biết chính xác được lúc nào change thay đổi.

# Global Constants:

# Ta muốn khai báo 1 biến nào đó mà muốn giá trị của nó không thay đổi hoặc muốn nó không thể chỉnh sửa được, ta hãy viết hoa hết các chữ cái của biến đó.

# EX:

PI = 3.1416