# advanced_features_and_security/bookshelf/signals.py
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":
        Book = apps.get_model("bookshelf", "Book")

        # Ensure permissions exist
        perms = {
            "can_view": Permission.objects.get(codename="can_view"),
            "can_create": Permission.objects.get(codename="can_create"),
            "can_edit": Permission.objects.get(codename="can_edit"),
            "can_delete": Permission.objects.get(codename="can_delete"),
        }

        # Create groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Assign permissions
        editors.permissions.set([perms["can_create"], perms["can_edit"]])
        viewers.permissions.set([perms["can_view"]])
        admins.permissions.set([perms["can_view"], perms["can_create"], perms["can_edit"], perms["can_delete"]])
