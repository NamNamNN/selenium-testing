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

# Mở menu
driver.find_element(
    By.ID,
    "react-burger-menu-btn"
).click()

time.sleep(2)

# Logout
driver.find_element(
    By.ID,
    "logout_sidebar_link"
).click()

time.sleep(2)

# Kiểm tra đã quay về trang đăng nhập chưa
if "saucedemo.com" in driver.current_url:
    print("TC03 PASS - Dang xuat thanh cong")
else:
    print("TC03 FAIL")

driver.quit()