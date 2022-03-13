# Dictionaries: dùng như sau: distionaries_name = {Key : Value}, key và value phải nằm trong ngoặc nhọn, phân biệt nhau bằng dấu ":", có thể có nhiều key và value trong dictionaries, cách nhau bỏi dấu ",".
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}
# Để lấy các items từ trong dictionaries ra, ta dùng cách sau: dictionaries_name[Key]. Lưu ý là phải nhậpđúng key có trong dictionaries nếu sai có lỗi KeyError.

# print(programming_dictionary["Bug"])

# Nếu Key đang ở kiểu dữ liệu nào thì ta nhập key ở kiểu dữ liệu đó.

# Thêm items mới vào dictionary.
# dictionary_name[Key] = Value. Dictionary mới sẽ thêm vào ở cuối dictionary_name.
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Tạo 1 dictionary trống:
empty_dictionary = {}

# Xóa các Key và Value trong Dictionary đi bằng cách tạo 1 dictionary trống mới trùng tên với dictionary cần xóa.

# Chỉnh sửa 1 item trong Dictionary: dictionary_name[Key] = Value cần sửa
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Lặp trong Dictionary: chỉ lấy được các Key ra
for key in programming_dictionary:
  print(key)
  # Kết quả lệnh in chỉ là: Bug, Function, Loop
  # Để lấy các Value:
  print(programming_dictionary[key])

# Nesting:Ta có 1 Dictionary cơ bản có 1 cặp Key và Value, ta có thể tạo 1 dictionary trong đó có 1 [List] đi với Key1, 1 dictionary khác đi với Key2:
# { 
# Key1: [List]
# Key2: {Dictionary}
# }

capitals = {
  "France": "Paries",
  "Germany": "Berlin"
}
# Nesting a list in Dictionary:
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in Dictionary:
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 7},
  "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 4}
}

# Nesting multiple Dictionaries ina single List:

travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 7
  },
  {
    "country":"Germany",
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 4
  },
]
