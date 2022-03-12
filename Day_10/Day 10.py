# Function with output: cho phép có 1 output khi kết thúc Function.
# def function_name():
#   return 3
# output = function_name()
# Lệnh return giúp trả kết quả của function, giuos chúng ta có thể lấy kết quả trong function đó.

def format_name(f_name, l_name):
  """Hàm format_name() giúp ta viết hoa các chữ cái đầu tiên của f_name và l_name
  """
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  # title() là hàm giúp chuyển ký tự đầu tiên của từ thành chữ in hòa. Ví dụ: vuong.title() kết quả sẽ là: Vuong.
  return f"{formated_f_name} {formated_l_name}"
  # Trả về kết quả cho hàm này là 1 fstrings:f"{formated_f_name} {formated_l_name}"
formated_string = format_name("VO le QUOC", "VUOng")
print(formated_string)
# Kết quả sẽ là Vo Le Quoc Vuong
# Khi nhận lệnh return máy tính sẽ hiểu đây là kết thúc của function.
# Nếu Function có nhiều Output thì chỉ duy nhất 1 Output đủ điều kiện sẽ là Output cuối cùng của Function đó và sẽ thoát ra khỏi Function.

# Docstring:
# Ta có thể dùng Docstring để giải thích các chức năng của function mà ta tạo giống như các function sẵn có ví dụ hmaf len. Bằng cách thêm Docstring vào ngay dưới Function ta tạo. Cấu trúc của 1 Docstring: năm giữa cặp """a""". vừa rồi chính là 1 Docstring có nội dung là a. Và nếu ta đã thêm Docstring cho function ta đã tạo thì khi ta gọi hàm thì Docstring sẽ xuất hiện và giải thích chức năng của hàm như các hàm có sẵn như len()

# Điểm khác nhau giữa sử dụng Import và Print. khi chương trình có nhiều biến, và ta muốn sử dụng lại các kết quả tính toán lúc trươc thì import nên được sử dụng, vì ở lần gọi function đó, import là kết quả của lần gọi function đó, và kết quả đó ta có thể lưu vào 1 biến nào đó để sử dụng lại sau này. Còn nếu ta chỉ in ra và không lưu trên biến nào cả thì khi muốn sử dụng lại sẽ khó khăn hơn, và ta chỉ có thể gọi lại hàm đó 1 lần nữa.