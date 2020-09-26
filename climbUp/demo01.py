from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path = r'/home/tarena/桌面/geckodriver-v0.27.0-linux32/geckodriver')
driver.implicitly_wait(20) # 隐性等待，最长等20秒

driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)
for i in range(0,3):
    # 下滑到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 转换iframe，再找到查看更多，点击
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
    print("123")
    load_more = driver.find_element_by_css_selector('div.more-wrapper')
    load_more.click()
    # 把iframe又转回去
    driver.switch_to.default_content()
    time.sleep(2)
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)