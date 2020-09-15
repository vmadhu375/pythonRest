from employeeapi.viewsets import EmployeeViewset,NotesViewSet,UserViewSet
 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)
router.register('notes',NotesViewSet)
router.register('users', UserViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive