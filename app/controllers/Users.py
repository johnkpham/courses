
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('Course')
   
    def index(self):
        courses = self.models['Course'].get_courses()
        return self.load_view('/courses/index.html', courses = courses)

    def new(self):
        return self.load_view('/courses/new.html')

    def create(self):
        info = {
            'course_name' : request.form['course_name'],
            'description' : request.form['description']
        }
        self.models['Course'].create(info)
        return redirect('/')

    def show(self, id):
        user = self.models['Course'].get_user_by_id(id)
        #user is a list; we just want the first element, hence user[0]
        return self.load_view('/courses/show.html', course = user[0])

    def update(self, id):
        info = {
            'course_name' : request.form['course_name'],
            'description' : request.form['description']
        }
        self.models['Course'].update(info, id)
        return redirect('/')    

    def remove(self, id):
        user = self.models['Course'].get_user_by_id(id)
        return self.load_view('/courses/remove.html', course = user[0])

    def destroy(self, id):
        self.models['Course'].destroy(id)
        return redirect('/')



    # def edit(self, id):
    #     user = self.models['Course'].get_user_by_id(id)
    #     return self.load_view('/courses/edit.html', user = user[0])



"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""

