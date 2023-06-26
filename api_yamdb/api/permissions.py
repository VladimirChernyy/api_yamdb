from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем неаутентифицированным пользователям выполнять
        # безопасные методы (GET, HEAD, OPTIONS)
        if not request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS
        # Разрешаем аутентифицированным пользователям выполнять
        # любые безопасные методы, запрещаем доступ
        # для них к небезопасным методам, если они не являются администраторами
        elif request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_admin


class IsAdminModeratorAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin
                )


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_admin or request.user.is_superuser))
