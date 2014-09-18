import endpoints
import logging

from protorpc import messages
from protorpc import message_types
from protorpc import remote

from models import CourseEntity

rateCourse_api = endpoints.api(name='rateCourse',version='v1', description='A rest API for rate course applicaiton')

class CourseMessage(messages.Message):
	course_name = messages.StringField(1)
	course_code = messages.StringField(2)
	course_department = messages.StringField(3)

class CourseNameMessage(messages.Message):
	course_name = messages.StringField(1)
class DepartmentMessage(messages.Message):
	department = messages.StringField(1)
class ListCourseMessage(messages.Message):
	courses = messages.MessageField(CourseMessage, 1, repeated=True)

@rateCourse_api.api_class(resource_name='course')
class RestCourse(remote.Service):

	@endpoints.method(CourseMessage, CourseMessage,
		name='insert',
		path='course/insert',
		http_method='POST'
		) 
	def course_insert(self, request):
		# logging.info(request)
		# request.course_name
		# request.course_code

		# talk to datastore
		# create a new entity for course
		# course = CourseEntity(course_name = request.course_name, course_code = request.course_code)
		course = CourseEntity(id= request.course_name, course_name = request.course_name, 
							course_code = request.course_code, course_department = request.course_department)
		course.put()

		return CourseMessage(course_name=request.course_name, course_code=request.course_code, course_department=request.course_department)


	@endpoints.method(CourseNameMessage, CourseMessage,
		name='get',
		path='course/get',
		http_method='GET'
		) 
	def course_get(self, request):
		# request.course_name
		course = CourseEntity.get_by_id(request.course_name)
		if course:
			return CourseMessage(course_name=course.course_name, course_code=course.course_code, course_department=course.course_department)
		else:
			raise endpoints.NotFoundException('Course information not found')


	@endpoints.method(DepartmentMessage, ListCourseMessage,
		name='listbydepartment',
		path='course/listbydepartment',
		http_method='GET'
		) 
	def course_listbydepartment(self, request):

		# request.department

		query = CourseEntity.query(CourseEntity.course_department == request.department)
		courses = query.fetch()
		course_list = []
		for course in courses:
			cm = CourseMessage(course_name = course.course_name, course_code = course.course_code, course_department = course.course_department)
			course_list.append(cm)
		return ListCourseMessage(courses = course_list)

	@endpoints.method(CourseNameMessage, CourseMessage,
		name = 'delete',
		path = 'course/delete',
		http_method = 'DELETE'
		)
	def course_delete(self, request):
		course = CourseEntity.get_by_id(request.course_name)
		course_m = CourseMessage(course_name = course.course_name, course_code=course.course_code, course_department=course.course_department)
		course.key.delete()
		return course_m

