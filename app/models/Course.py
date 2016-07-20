
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def create(self, info):
        query = "INSERT INTO courses (course_name, description, date_added) VALUES (:course_name, :description, NOW())"
        data = {
            'course_name' : info['course_name'],
            'description' : info['description']
        }
        return self.db.query_db(query, data)

    def get_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_user_by_id(self, id):
        query = "SELECT * FROM courses WHERE id = :id"
        data = {'id' : id}
        return self.db.query_db(query,data)

    # def update(self, info, id):
    #     query = "UPDATE courses SET name = :name, email = :email, updated_at = NOW() WHERE id = :id"
    #     data = {
    #         'name' : info['name'],
    #         'email' : info['email'],
    #         'id' : id
    #     }
    #     return self.db.query_db(query, data)

    def destroy(self, id):
        query = "DELETE FROM courses WHERE id = :id"
        data = {'id' : id}
        return self.db.query_db(query, data)

    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """