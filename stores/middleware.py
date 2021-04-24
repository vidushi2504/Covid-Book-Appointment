from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect

class LogInRequiredMiddleware:

	def __init__(self, get_response):
		self.get_response=get_response

	def __call__(self, request):
		response=self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		url=request.path
		if request.user.is_authenticated and (url in settings.EXEMPT_FOR_AUTHENTICATED_URLS):
			return redirect("account", request.user.id)

		if not request.user.is_authenticated and (url in settings.EXEMPT_FOR_NON_AUTHENTICATED_URLS):
			return redirect("/")