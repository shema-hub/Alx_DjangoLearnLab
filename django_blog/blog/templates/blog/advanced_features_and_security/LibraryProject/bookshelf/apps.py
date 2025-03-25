from django.apps import AppConfig
import threading

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        """Ensure groups and permissions are created after Django loads all models."""
        threading.Thread(target=self.create_groups_and_permissions, daemon=True).start()

    def create_groups_and_permissions(self):
        """Creates groups and permissions only when models are fully loaded."""
        from django.db.utils import OperationalError, ProgrammingError
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from bookshelf.models import Book  # Import here to avoid premature loading

        try:
            book_content_type = ContentType.objects.get_for_model(Book)

            # Define permissions
            permissions = {
                "can_view": "Can view books",
                "can_create": "Can create books",
                "can_edit": "Can edit books",
                "can_delete": "Can delete books",
            }
            for codename, name in permissions.items():
                Permission.objects.get_or_create(codename=codename, content_type=book_content_type, name=name)

            # Define groups and assign permissions
            groups = {
                "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
                "Editors": ["can_view", "can_create", "can_edit"],
                "Viewers": ["can_view"],
            }
            for group_name, perms in groups.items():
                group, _ = Group.objects.get_or_create(name=group_name)
                group.permissions.set(Permission.objects.filter(codename__in=perms))

            print("Groups and permissions successfully created.")

        except (OperationalError, ProgrammingError):
            print("Warning: Run migrations first before executing this function.")
