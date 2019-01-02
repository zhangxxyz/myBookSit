from DBUtils.PooledDB import PooledDB
import mysql
import pymysql

path = "mysql+mysqlconnector://root:123456@47.97.111.175:3306/user?charset=utf8mb4"

class my_sql(object):
    __pool = None
    def __init__(self):
        self._conn = my_sql.__getConn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getConn():
        if my_sql.__pool is None:
            my_sql.__pool = PooledDB(creator = pymysql,mincached=1 , maxcached=20,maxusage = 50,
                            host="47.97.111.175",user="root",passwd="123456",db="myBook",
                            port=3306, charset="utf8mb4"
                          )

        return my_sql.__pool.connection()

    # def getOne(self, sql, params=()):
    #     result = None
    #     try:
    #         count = self._cursor.execute(sql, params)
    #         result = self.cursor.fetchone()
    #         self.close()
    #     except Exception, e:
    #         print
    #         e.message
    #     return result
    #
    # def get_all(self, sql, params=None):
    #     list = ()
    #     try:
    #         self.connect()
    #         self.cursor.execute(sql, params)
    #         list = self.cursor.fetchall()
    #         self.close()
    #     except Exception, e:
    #         print
    #         e.message
    #     return list
    # params : list[[list],[list]]
    def insert(self, sql, params=[]):
        print(sql,params)
        print('数据库开始插入')
        try:
            if len(params) == 0:
                print('555555')
                self._cursor.execute(sql)
            if len(params) >1:
                self._cursor.executemany(sql,params)
            # print(sql,params)
            print('数据库插入')
            self.commit()

        except Exception as Error:

            self.Error_log(sql,error=Error)

        # return self.__edit(sql, params)

    # def update(self, sql, params=()):
    #     return self.__edit(sql, params)
    #
    # def delete(self, sql, params=()):
    #     return self.__edit(sql, params)
    #
    # def __edit(self, sql, params):
    #     count = 0
    #     try:
    #         self.connect()
    #         count = self.cursor.execute(sql, params)
    #         self.conn.commit()
    #         self.close()
    #     except Exception, e:
    #         print
    #         e.message
    #     return count
    def commit(self):
        self._conn.commit()
        self.close()

    def close(self):
        self._cursor.close()
        self._conn.close()

    def Error_log(self,sql,error):
        errorStr = '数据库错误,\n错误语句:{}\n错误信息:{}\n'.format(sql,error)
        print(error)
        self._conn.rollback()
        self.close()
