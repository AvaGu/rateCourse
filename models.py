from google.appengine.ext import ndb

class CourseEntity(ndb.Model):
	course_name = ndb.StringProperty()
	course_code = ndb.StringProperty()
	course_department = ndb.StringProperty()


