from django.urls import path

from d2e_share_splitter.users.views import CreateUser
from d2e_share_splitter.users.views import DeleteUser
from d2e_share_splitter.users.views import UpdateUser
from d2e_share_splitter.users.views import UsersLog
from d2e_share_splitter.users.views import UsersView
from d2e_share_splitter.users.views import user_detail_view
from d2e_share_splitter.users.views import user_redirect_view
from d2e_share_splitter.users.views import user_update_view

app_name = "users"
urlpatterns = [
    path("list/", UsersView.as_view(), name="list_users"),
    path("log/", UsersLog.as_view(), name="log_users"),
    path("create/", CreateUser.as_view(), name="user_create"),
    path("delete/", DeleteUser.as_view(), name="user_delete"),
    path("update/", UpdateUser.as_view(), name="user_update"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    # Django Ajax CRUD Operations
]
