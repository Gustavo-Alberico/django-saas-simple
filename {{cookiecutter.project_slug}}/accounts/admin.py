from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Tenant, User


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by",)
    list_display = ("name", "paid_until")


from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    readonly_fields = ("tenant",)

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "tenant",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "tenant")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "tenant")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "tenant",
                ),
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(User, UserAdmin)
