# import sqlite3
# import os
#
# home_location = os.environ['LINUX_TODO_APP']
#
#
# class TaskManager(object):
#     """ Class for interaction with database tables 'tasks' and 'lists'. """
#     LISTS_CREATION = 'CREATE TABLE IF NOT EXISTS lists(id INTEGER PRIMARY KEY, name TEXT)'
#     TASKS_CREATION = """CREATE TABLE if not exists tasks(id INTEGER PRIMARY KEY, list INTEGER NOT NULL,
#                         title TEXT NOT NULL, content TEXT, date TEXT, priority TEXT, is_complete TEXT NOT NULL,
#                         FOREIGN KEY(list) REFERENCES lists(id)
#                         ON UPDATE SET NULL
#                         ON DELETE CASCADE)"""
#
#     def __init__(self):
#         self.conn = sqlite3.connect(f'{home_location}/todos.db')
#         self.conn.execute('PRAGMA foreign_keys = 1')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute(self.LISTS_CREATION)
#         self.cursor.execute(self.TASKS_CREATION)
#         self.create_main_list()
#
#     def __str__(self):
#         return f'Task Manager for {self.conn}'
#
#     def __enter__(self):
#         self.init_cursor()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.commit()
#             print('Data stored successfully.' + '\n')
#         else:
#             self.commit()
#             print(f'File closed but an exception appeared: {str(exc_type)}')
#             return False
#
#     def create_main_list(self):
#         self.init_cursor()
#         if not self.cursor.execute('SELECT * FROM lists WHERE name="Main"').fetchone():
#             sql_command = 'INSERT INTO lists (name) VALUES(?)'
#             self.cursor.execute(sql_command, ('Main', ))
#             self.commit()
#
#     def create_new_list(self, list_name):
#         sql_command = 'INSERT INTO lists (name) VALUES (?)'
#         self.cursor.execute(sql_command, (list_name,))
#
#     def delete_list(self, list_name):
#         sql_command = 'DELETE FROM lists WHERE name=(?);'
#         self.cursor.execute(sql_command, (list_name,))
#
#     def get_table(self, table: str):
#         sql_command = f'SELECT * FROM {table}'
#         self.cursor.execute(sql_command)
#         return self.cursor.fetchall()
#
#     def get_tasks_by_list(self, from_list: str):
#         sql_command = 'SELECT * FROM tasks WHERE list=?'
#         self.cursor.execute(sql_command, (from_list,))
#         return self.cursor.fetchall()
#
#     def get_task_by_title(self, title):
#         sql_command = 'SELECT * FROM tasks WHERE title=?'
#         self.cursor.execute(sql_command, (title,))
#         return self.cursor.fetchone()
#
#     def get_task_by_id(self, task_id):
#         sql_command = 'SELECT * FROM tasks WHERE id=?'
#         self.cursor.execute(sql_command, (task_id,))
#         return self.cursor.fetchone()
#
#     def delete_task(self, task_id):
#         sql_command = 'DELETE FROM tasks WHERE id=?'
#         self.cursor.execute(sql_command, (task_id,))
#
#     def get_list_name(self, list_id):
#         sql_command = 'SELECT name FROM lists WHERE id=?'
#         self.cursor.execute(sql_command, (list_id,))
#         return self.cursor.fetchone()
#
#     def get_list_id(self, list_name):
#         sql_command = 'SELECT id FROM lists WHERE name=?'
#         self.cursor.execute(sql_command, (list_name,))
#         return self.cursor.fetchone()
#
#     def commit(self):
#         self.conn.commit()
#         self.conn.close()
#
#     def init_cursor(self):
#         self.conn = sqlite3.connect(f'{home_location}/todos.db')
#         self.conn.execute('PRAGMA foreign_keys = 1')
#         self.cursor = self.conn.cursor()
#
#
# task_manager = TaskManager()
