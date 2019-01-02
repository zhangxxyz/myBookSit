


from urllib import request
from http import cookiejar
import selenium.webdriver as  web

def getCookie():
    ur = "http://www.baidu.com"
    driver = web.PhantomJS()
    # driver.implicitly_wait(10)
    x = driver.get(ur)
    # 获取cookie列表
    cookie_list = driver.get_cookies()
    print(cookie_list)
    # 格式化打印cookie
    # for cookie in cookie_list:
    #     print(cookie)
    # print(cookie_dict)
    print('-----------------------------------------------')
    cookie = cookiejar.CookieJar()
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
        # 此处的open方法打开网页
    response = opener.open(ur)
        # 打印cookie信息
    for item in cookie:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)






getCookie()