from flask_restx import fields

from .extensions import api 

course_model=api.model("Course",{
    "id":fields.Integer,
    "name":fields.String
})

student_model=api.model("Student",{
    "id":fields.Integer,
    "name":fields.String,
    "course":fields.Nested(course_model)
})

course_input_model=api.model("CourseImput",{
    "name":fields.String,
})
student_input_model=api.model("StudentImput",{
    "name":fields.String,
    "course":fields.String
})

login_model=api.model("LoginModel",{
    "userrname":fields.String,
    "password":fields.String
}
)

user_model=api.model("UserModel",{
    "id":fields.Integer,
    "userrname":fields.String

})