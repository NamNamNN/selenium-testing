# Selenium Automation Testing

## Thông tin sinh viên

* Họ và tên: ...
* MSSV: ...

## Website kiểm thử

https://www.saucedemo.com

## Công cụ sử dụng

* Python
* Selenium
* ChromeDriver
* VS Code

## Test Case

### TC01 - Login thành công

* Nhập username và password hợp lệ
* Nhấn Login
* Kết quả mong đợi: Chuyển đến trang Inventory

### TC02 - Add To Cart

* Đăng nhập
* Thêm sản phẩm vào giỏ hàng
* Kết quả mong đợi: Giỏ hàng hiển thị số lượng 1

### TC03 - Logout

* Đăng nhập
* Chọn Logout
* Kết quả mong đợi: Quay về màn hình đăng nhập

## Cách chạy

pip install selenium

python test_login.py

python test_add_to_cart.py

python test_logout.py
