# gym_management/middleware.py
from django.shortcuts import redirect

class AdminAccessMiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        admin_paths = ['/admin-portal/']
        login_path = '/admin-portal/login/'

        if request.path == login_path:
            return None

        if any(request.path.startswith(path) for path in admin_paths):
            if not request.user.is_authenticated:
                return redirect('admin_portal:admin_login')
            if request.user.user_type != 'ADMIN':
                messages.error(request, "You don't have admin privileges!")
                return redirect('home')
            # Super Admin exclusive paths
            if 'super-admin-only' in request.path and request.user.role != 'SUPER_ADMIN':
                return HttpResponseForbidden("Super Admin access required")