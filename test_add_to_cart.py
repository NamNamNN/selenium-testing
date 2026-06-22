from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

# Đăng nhập
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Thêm sản phẩm vào giỏ hàng
driver.find_element(
    By.ID,
    "add-to-cart-sauce-labs-backpack"
).click()

time.sleep(2)

# Kiểm tra số lượng trong giỏ hàng
cart = driver.find_element(
    By.CLASS_NAME,
    "shopping_cart_badge"
).text

if cart == "1":
    print("TC02 PASS - Them san pham vao gio hang thanh cong")
else:
    print("TC02 FAIL")

driver.quit()