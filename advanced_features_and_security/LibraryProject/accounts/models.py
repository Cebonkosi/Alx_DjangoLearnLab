from django.conf import settings

# Example usage:
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
