from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permition_classes = [permissions.IsAdminUser, IsStaffEditorPermission]