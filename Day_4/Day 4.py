# import random
# # Phải dùng import để nhập giá trị vào module random
# rand_int = random.randint(1,20)
# print(rand_int)
# # cách dùng hàm random integer: random.randint(a,b): cho 1 số nguyên ngẫu nhiên trong khoản a:b 
# rand_float = random.random()
# print(rand_float)
# # random.random() sẽ cho 1 số thập phân ngẫu nhiên từ 0.0 đến 1.0
# # random 1 số thập phân ngẫu nhiên từ 0 đến 5
# rand_float1 = random.uniform(0,5)
# print(rand_float1)
# # hoặc có thể dùng random.random() * 5

# List: cách dùng: Tên List = [a, b, c, .... ] các thành phần trong list có thể là strings, number or boolean. các thành phần cách nhau bởi dấu ",". list có thể được lưu lại để có thể sử dụng về sau.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# states_of_america[0]
# dòng code trên để lấy Delaware, tương tự, muốn lấy Pennsylvania thì thay 0 trong ngoặc vuông thành 1, muốn lấy các strings tiếp theo thì tăng dần số thứ tự lên. [0,1,2....] tương ứng với các thứ tự số 1, 2, 3.... trong list.
# Nếu các số trong ngoặc vuông là -1,-2,-3 thì lấy từ list ra theo tứ tự từ cuối list đến đầu list

# states_of_america[0] = "ABC"
# Dòng lệnh trên thay đổi Delaware thành ABC
# states_of_america.append("DEF")
# dùng append("A") để thêm A vào cuối list
print(states_of_america)
# Dùng list.extend(iterable) để thêm 1 lisr khác vào cuối list
# Dùng list.insert(i,x) để chèn x vào vị trí i trong list
# Dùng list.remove(x) để bỏ x ra khỏi list
# states_of_america.pop(2)
# Dùng list.pop(i) để bỏ vị trí i trong list, nếu chỉ goxlisst.pop() thì sẽ bỏ vị trí cuỗi cùng trong list