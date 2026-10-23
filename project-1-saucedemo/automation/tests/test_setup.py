from selenium import webdriver

def test_opens_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title
    driver.quit()
    