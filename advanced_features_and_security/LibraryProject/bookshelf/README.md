# Permissions and Groups Setup

- Custom permissions defined in `Book.Meta`:
  - can_view, can_create, can_edit, can_delete
- Groups created:
  - **Editors** → can_create, can_edit
  - **Viewers** → can_view
  - **Admins** → all permissions
- Enforced with @permission_required in `views.py`
- Test: Create users in Django Admin → assign to groups → confirm access restrictions
