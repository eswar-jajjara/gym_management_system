from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import render

def admin_portal_home(request):
    return render(request, 'admin_portal/home.html')  # Ensure this template exists

@login_required
def admin_dashboard(request):
    if request.user.role not in ['SUPER_ADMIN', 'ADMIN_TEAM']:
        return redirect('home')

    # Real-time metrics
    context = {
        'total_members': CustomUser.objects.filter(role='MEMBER').count(),
        'active_trainers': CustomUser.objects.filter(role='TRAINER').count(),
        'monthly_revenue': Subscription.objects.filter(
            start_date__month=timezone.now().month
        ).aggregate(Sum('price'))['price__sum'],
        'class_occupancy': Schedule.objects.values('gym_class__name')
        .annotate(total=Count('members'))
    }

    @login_required
    def manage_permissions(request):
        if request.user.role != 'SUPER_ADMIN':
            return HttpResponseForbidden()

        if request.method == 'POST':
            form = PermissionForm(request.POST)
            if form.is_valid():
                # Handle permission updates
                AuditLog.objects.create(
                    user=request.user,
                    action="Updated permissions",
                    affected_model="CustomUser",
                    object_id=form.cleaned_data['user_id']
                )
                return redirect('admin_dashboard')

        # Show permission management interface

    return render(request, 'admin_portal/dashboard.html', context)