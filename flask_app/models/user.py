from config.mysqlconnection import connectToMySQL


class User:
    db = 'new_schema1'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'select * from users;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = 'select* from users where id = %(id)s;'
        user_data = connectToMySQL(cls.db).query_db(query, data)
        return cls(user_data[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name,email,created_at,updated_at) VALUES ( %(fname)s ,  %(lname)s  %(ema)s, NOW(), NOW());'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'update users set first_name = %(fname)s, last_name = %(lname)s,email = %(ema)s where id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = ' update users set first_name = %(fname)s, last_name = %(lname)s, email = %(ema)s where id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
