from enum import Enum

class itemEnum(Enum):
    # 书籍简介 作者 更新时间
    BQGBookInfo = 1
    # 书籍内容 章节 章节内容
    BQGBookContent = 2
    # 内容抓取失败
    BQGBookCententFail = 3