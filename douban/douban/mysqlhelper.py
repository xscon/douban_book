import pymysql

class MysqlHelper(object):
    # 需要有mysql的链接
    # 还需要有 cursor 游标
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                                    user='root', passwd='root',
                                    db='douban', charset='utf8mb4')
        self.cursor = self.conn.cursor()

    def execute_modify_sql(self, sql, data):
        self.cursor.execute(sql, data)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    helper = MysqlHelper()
    insert_sql = 'INSERT INTO douban_book(content) VALUES(%s)'
    data = ('dfasfsdf',)
    helper.execute_modify_sql(insert_sql, data)