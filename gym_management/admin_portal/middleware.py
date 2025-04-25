from django.http import HttpResponseForbidden
from django.urls import reverse


class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        admin_paths = ['/admin-portal/', '/manage-permissions/', '/audit-logs/']

        if any(request.path.startswith(path) for path in admin_paths):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required")

            if not request.user.role in ['SUPER_ADMIN', 'ADMIN_TEAM']:
                return HttpResponseForbidden("Insufficient privileges")