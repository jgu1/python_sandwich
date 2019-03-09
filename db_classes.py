import MySQLdb
class DAO(object):
    db = None
    def __init__(self):
        self.db = MySQLdb.connect(host="genomesvr2", # your host, usually localhost
                    user="es", # your username
                    passwd="detective", # your password
                    db="ES_OUTPUT") # name of the data base

    def exec_fetch_SQL(self,sql_template):
        cur = self.db.cursor()
        cur.execute(sql_template)
        rows = cur.fetchall()
        return list(rows)

    def get_bread_calorie(self):
        # use_case_0: string literal
        sql_template = 'select type,calorie from bottom_bread;'
        # use_case_1: calling a function, although a mysterious one, it is a function after all
        rows = self.exec_fetch_SQL(sql_template)
        # use_case_2: define an empty list
        type_calorie_list = []
        # use_case_3: loop
        for row in rows:
            bread_type = row[0]
            bread_calorie = row[1]
            type_colorie_pair = [bread_type,bread_calorie]
            # use_case_2.5: append to list
            type_calorie_list.append(type_colorie_pair)
        return type_calorie_list    
