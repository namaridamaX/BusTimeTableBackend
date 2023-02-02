from selenium import webdriver

options = webdriver.ChromeOptions()

print('Connect remote browser...')

# 接続先のリモートサーバーをコンテナ名で指定
driver = webdriver.Remote(command_executor='172.18.0.2:4444/wd/hub', options=options)

driver.get('https://google.com')
print('current URL: ', driver.current_url)

driver.quit()