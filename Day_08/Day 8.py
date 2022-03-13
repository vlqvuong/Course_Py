# Function:
# Tạo 1 function tên great() sau đó viết 3 lệnh print. Sau đó gọi function great()

# def great():
#     print("Hello")
#     print("I'm Vuong")
#     print("I'm 24 years old")
# great()

# Function with input:
# def my_function(something)
# Do this with something
# Then do this with something
# Finally do this with something

# def great_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"I'm 24 years old. And you, {name}")
# great_with_name("Quynh")

# Functions with more than input:

def great_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

great_with("Nowhere", "Quynh")

# Phải đảm bảo rằng thứ tự của các biến đặt trong ngoặc tròn() trong hàm phải đúng với thứ tự ta mong muốn nhập vào.

# Keyword Argument: ta có thế xáo trộn vị trí mà không làm thay đổi các lệnh cần thực thi khác với ý muốn bằng cách khi gọi hàm ta gán trực tiếp giá trị vào luôn.

great_with(location = "Nowhere", name = "Quynh")