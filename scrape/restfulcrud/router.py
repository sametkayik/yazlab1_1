from notebookapi.viewsets import NotebookViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notebook', NotebookViewset)

