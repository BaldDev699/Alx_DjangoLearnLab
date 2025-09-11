# Permissions and Groups Setup Guide

This application uses Django's built-in permissions and groups to manage access control for users. Below is a summary of how permissions and groups are set up and used:

## Permissions
- **can_create**: Allows users to create new objects (e.g., books, records).
- **can_edit**: Allows users to edit existing objects.
- **can_delete**: Allows users to delete objects.
- **can_view**: Allows users to view objects.

These permissions are typically defined in the model's `Meta` class or assigned via Django's admin interface or migrations.

## Groups
- **Librarians**: Users in this group usually have `can_create`, `can_edit`, `can_delete`, and `can_view` permissions.
- **Members**: Users in this group typically have only `can_view` permission.

Groups are used to bundle permissions and assign them to users more efficiently.

## Usage in Code
- Permissions are checked using Django's `user.has_perm('app_label.can_edit')` or similar methods.
- Groups are assigned to users via the admin interface or programmatically using `user.groups.add(group)`.

## Example
```python
# Check if a user can edit
if user.has_perm('bookshelf.can_edit'):
    # Allow editing
    pass

# Assign user to Librarians group
from django.contrib.auth.models import Group
librarians = Group.objects.get(name='Librarians')
user.groups.add(librarians)
```

## Notes
- Make sure to create the permissions and groups either via migrations, admin, or Django shell.
- Always use the variable names as defined above (e.g., `can_edit`, `can_create`).
- Refer to Django documentation for advanced permission and group management.


# Changes made to secure the application

This Django project is configured for production security as follows:

1. **HTTPS Enforcement**
   - `SECURE_SSL_REDIRECT = True`: All HTTP requests are redirected to HTTPS.
   - `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True`: Cookies are only sent over HTTPS.

2. **Cookie Security**
   - `CSRF_COOKIE_HTTPONLY = True` and `SESSION_COOKIE_HTTPONLY = True`: Cookies are inaccessible to JavaScript.

3. **HSTS (HTTP Strict Transport Security)**
   - `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for 1 year.
   - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
   - `SECURE_HSTS_PRELOAD = True`: Allows site to be included in browser preload lists.

4. **XSS and Content-Type Protections**
   - `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS filter.
   - `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents content type sniffing.
   - `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking by denying framing.

5. **Password Validation**
   - Multiple validators are enabled to enforce strong passwords.

6. **Debug Mode**
   - `DEBUG = False`: Debug mode is disabled for production.

7. **Allowed Hosts**
   - `ALLOWED_HOSTS` should be set to your domain(s) in production.

> Review and update `ALLOWED_HOSTS` and `SECRET_KEY` before deploying to production.

For more details, see Django's official security documentation:
https://docs.djangoproject.com/en/5.2/topics/security/
