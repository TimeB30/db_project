import psycopg2
from datetime import datetime
class Database:
    def __init__(self, params):
        self.params = params
    def get_user_info(self,user_login):
        with psycopg2.connect(**self.params) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT users.user_id, users.user_role, users.user_name, user_block.block_id, dorm_block.dorm_id FROM users "
                               "LEFT JOIN user_block ON users.user_id = user_block.user_id "
                               "LEFT JOIN dorm_block ON user_block.block_id = dorm_block.block_id "
                               "WHERE users.user_login = %s",(user_login,))
                return cursor.fetchone()
    def get_users_info(self,block_id):
        with psycopg2.connect(**self.params) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT users.user_id, users.user_role, users.user_name, user_block.block_id, dorm_block.dorm_id FROM users "
                    "LEFT JOIN user_block ON users.user_id = user_block.user_id LEFT JOIN dorm_block ON user_block.block_id = dorm_block.block_id "
                    "WHERE user_block.block_id = %s", (block_id,))
                return cursor.fetchall()
    def get_user_tasks(self,user_id):
        with psycopg2.connect(**self.params) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT user_task.task_id, tasks.task_name  FROM user_task JOIN tasks USING(task_id) WHERE user_task.user_id  = %s ORDER BY task_id;", (user_id,))
                return cursor.fetchall()

    def is_user(self,user_login):
        with psycopg2.connect(**self.params) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT user_login from users WHERE user_login = %s", (user_login,))
                return (cursor.fetchone() != None)
    def insert_user(self, user_name, user_surname, user_middle_name, user_login, user_password):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    if (user_middle_name == ""):
                        user_middle_name = None
                    cursor.execute("INSERT INTO users (user_name, user_surname, user_middle_name, user_login, user_password) "
                                   "VALUES (%s, %s, %s, %s, %s) RETURNING user_id",(user_name, user_surname, user_middle_name, user_login,user_password,))
                    return cursor.fetchone()[0]
        except:
            return 0
    def get_user_password(self,user_login):
        with psycopg2.connect(**self.params) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT user_password FROM users WHERE user_login = %s", (user_login,))
                return cursor.fetchone()
    def task_done(self,user_id,task_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT task_type FROM tasks WHERE task_id = %s",(task_id,))
                    task_type = cursor.fetchone()[0]
                    if (task_type == "single"):
                        cursor.execute("DELETE FROM user_task WHERE user_id = %s AND task_id = %s",(user_id,task_id,))
                    else:
                        cursor.execute("SELECT block_id FROM user_block WHERE user_id = %s")
                        user_block_id = cursor.fetchone()[0]
                        cursor.execute("SELECT user_id FROM user_block WHERE user_id > %s AND block_id = %s ORDER BY user_id LIMIT 1", (user_id,user_block_id,))
                        next_user_id = cursor.fetchone()
                        if next_user_id == None:
                            cursor.execute("SELECT user_id FROM user_block WHERE block = %s ORDER BY user_id LIMIT 1",(user_block_id,))
                            next_user_id = cursor.fetchone()[0]
                        else:
                            next_user_id = next_user_id[0]
                        cursor.execut("UPDATE user_task SET user_id = %s WHERE user_id = %s",(next_user_id,user_id,))
                        return 1
        except:
            return 0
    def add_history(self,user_id,block_id,dorm_id,action):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO history(user_id,block_id,dorm_id,action) "
                                   "VALUES (%s,%s,%s,%s)",(user_id,block_id,dorm_id,action,))
                    return 1
        except Exception as e:
            print(e)
            return 0
    def make_task(self,task_type,task_name,sender_info):
        try:
            block_id = sender_info.block_id
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    task_type_for_db = "single"
                    if (task_type == "cycled"):
                        task_type_for_db = "cycled"
                    cursor.execute("INSERT INTO tasks (task_name,task_type) VALUES (%s,%s) RETURNING task_id",(task_name,task_type_for_db,))
                    task_id = cursor.fetchone()[0]
                    cursor.execute("SELECT user_id FROM user_block WHERE block_id = %s ORDER BY user_id",(block_id, ))
                    users_id = cursor.fetchall()
                    if (task_type == "for_all"):
                        for i in users_id:
                            user_id = i[0]
                            cursor.execute("INSERT INTO user_task (user_id,task_id) VALUES (%s,%s)",(user_id,task_id,))
                    elif (task_type == "cycled"):
                        user_id = users_id[0][0]
                        cursor.execute("INSERT INTO user_task (user_id,task_id) VALUES (%s,%s)", (user_id, task_id,))
                    else:
                        user_id = task_type
                        cursor.execute("INSERT INTO user_task (user_id,task_id) VALUES (%s,%s)", (user_id, task_id,))
            return 1
        except Exception as e :
            print (e)
            return 0
    def get_block_tasks(self,block_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT user_block.user_id, users.user_name, users.user_surname, user_task.task_id, tasks.task_name FROM user_block "
                                   "JOIN user_task ON user_block.user_id = user_task.user_id "
                                   "JOIN tasks ON tasks.task_id = user_task.task_id "
                                   "JOIN users ON users.user_id = user_block.user_id WHERE user_block.block_id = %s "
                                   "ORDER BY users.user_id ",(block_id,))
                    return cursor.fetchall()
        except Exception as e:
            print(e)
            return []
    def delete_task(self,task_id,user_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM user_task WHERE task_id = %s AND user_id = %s",(task_id, user_id,))
                    return 1
        except:
            return 0
    def get_block_history(self,block_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT history.dorm_id, history.block_id, history.user_id, users.user_name, users.user_surname, history.action "
                                   "FROM history JOIN users USING(user_id) ORDER BY date_time DESC")
                    return cursor.fetchall()
        except:
            return 0
    def get_dorms_blocks(self,free=1):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    nt = ""
                    if (free):
                        nt = "NOT"
                    cursor.execute("SELECT dorms.dorm_id, dorms.dorm_name, dorm_block.block_id, blocks.block_number FROM dorms "
                                   "JOIN dorm_block ON dorms.dorm_id = dorm_block.dorm_id "
                                   "JOIN blocks ON blocks.block_id = dorm_block.block_id "
                                   f"WHERE dorm_block.block_id {nt} IN (SELECT DISTINCT block_id FROM user_block) "
                                   "ORDER BY dorms.dorm_id, dorm_block.block_id")
                    return cursor.fetchall()
        except Exception as e:
            print(e)
            return 0
    def AddUser(self,user_id,user_role,block_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO user_block(user_id,block_id) VALUES(%s, %s)",(user_id,block_id,))
                    cursor.execute("UPDATE users SET user_role = %s WHERE user_id = %s",(user_role,user_id,))
                    return 1
        except Exception as e:
            print(e)
            return 0
    def add_request(self,dorm_id, block_id, user_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO requests(dorm_id,block_id,user_id) "
                                   "VALUES (%s, %s, %s) "
                                   "RETURNING request_id ",(dorm_id,block_id,user_id,))
                    return cursor.fetchone()[0]
        except:
            return 0
    def cancel_request(self,request_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM requests WHERE request_id = %s",(request_id,))
                    return 1

        except:
            return 0
    def delete_requests(self,block_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM requests WHERE block_id = %s",(block_id,))
                    return 1

        except:
            return 0
    def get_request(self,user_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT requests.request_id, requests.dorm_id, dorms.dorm_name, "
                                   "requests.block_id, blocks.block_number, requests.status "
                                   "FROM requests LEFT JOIN dorms ON dorms.dorm_id = requests.dorm_id "
                                   "LEFT JOIN blocks ON blocks.block_id = requests.block_id "
                                   "WHERE requests.user_id = %s",(user_id,))
                    return cursor.fetchone()

        except:

            return []
    def get_requests(self,block_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT requests.request_id, requests.user_id, users.user_name, users.user_surname, users.user_middle_name "
                                   "FROM requests "
                                   "JOIN users ON users.user_id = requests.user_id "
                                   "WHERE requests.block_id = %s",(block_id,))
                    return cursor.fetchall()

        except Exception as e:
            return []
    def kick_user(self,user_id, block_id):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM user_block WHERE user_id = %s AND block_id = %s",(user_id,block_id,))
                    return 1
        except:
            return 0
    def change_role(self,user_id,role):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE users SET user_role = %s WHERE user_id = %s",(role,user_id))
                    return 1
        except:
            return 0
    def set_request_status(self,request_id,status):
        try:
            with psycopg2.connect(**self.params) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE requests SET status = %s WHERE request_id = %s",(status,request_id))
                    return 1
        except:
            return 0