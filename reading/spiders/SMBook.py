# 神马搜索渠道的小说  用来更新用

SMURL = 'https://m.sm.cn/s?q='



class search(object):
    # def __init__(self,searchName = None):
    #     print('走了init')
    #

    @classmethod
    def getSearchURl(cls,name):
        searchURL = '{}{}'.format(SMURL, name)
        return searchURL










