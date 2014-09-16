import endpoints
import logging

from protorpc import messages
from protorpc import message_types
from protorpc import remote

rateCourse_api = endpoints.api(name='rateCourse',version='v1', description='A rest API for rate course applicaiton')

class CourseMessage(messages.Message):
	course_name = messages.StringField(1)
	course_code = messages.StringField(2)


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
		return CourseMessage(course_name=request.course_name, course_code=request.course_code)
