# 笔趣阁手机版的
# q 书名 t = m 手机版
URL = 'https://sou.xanbhx.com/search?siteid=xsla&q='



class MBGSearch():
    @classmethod
    # 返回搜索url
    def getUrl(cls,Name):
        searchName = '{}{}'.format(URL, Name)
        return searchName



