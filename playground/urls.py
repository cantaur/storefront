from django.urls import path
from . import views

urlpatterns = [

    #path(route: str, view: (*args: Any, **kwargs: Any) -> HttpResponseBase, kwargs: Dict[str, Any] = ..., name: str = ...) -> URLPattern
    #kwargs :  keyword argument
    
    # URL config module
    path('hello/', views.say_hello),
]