from django.core.management.base import BaseCommand
from subscriptions.models import Plan

class Command(BaseCommand):
    help = 'Populate the database with sample plans'

    def handle(self, *args, **kwargs):
        # Create sample plans
        Plan.objects.create(
            name="Basic",
            price=29.99,
            description="Access to gym facilities\nStandard equipment\n1 free personal training session"
        )

        Plan.objects.create(
            name="Premium",
            price=59.99,
            description="Access to gym facilities\nPremium equipment\n4 free personal training sessions\nAccess to group classes"
        )

        Plan.objects.create(
            name="VIP",
            price=99.99,
            description="Access to gym facilities\nAll premium equipment\nUnlimited personal training sessions\n24/7 priority support\nFree locker"
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated plans!'))