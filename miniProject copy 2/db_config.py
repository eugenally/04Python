import pymysql

def get_conn():
    return pymysql.connect(
        host='localhost',
        user='sample_user',
        password='1234',
        database='data_list_db',
        charset='utf8'
    )