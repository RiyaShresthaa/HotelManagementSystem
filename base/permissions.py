from rest_framework.permissions import BasePermission

class FrontDeskUserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'Frontdesk':
            return True
        
class AccountingUserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'Accounting':
            return True


class RestaurantUserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'Restaurant':
            return True
        

class ManagementUserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'Management':
            return True
        