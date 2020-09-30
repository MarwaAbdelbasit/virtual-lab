from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Devices, Experiments, Reservation, FAQ , Plan ,Contact_Us

User = get_user_model()



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
       ('Personal Info', {'fields': ('full_name', 'university', 'faculty', 'date_of_birth',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class DevicesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    class Meta:
        model = Devices

admin.site.register(Devices, DevicesAdmin)

class ExperimentsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    class Meta:
        model = Experiments

admin.site.register(Experiments, ExperimentsAdmin)


class ReservationAdmin(admin.ModelAdmin):
    search_fields = ['Device']
    class Meta:
        model = Reservation

admin.site.register(Reservation, ReservationAdmin)


class FAQAdmin(admin.ModelAdmin):
    search_fields = ['Question']
    class Meta:
        model = FAQ

admin.site.register(FAQ, FAQAdmin)

class PlanAdmin(admin.ModelAdmin):
    search_fields = ['plan_name']
    class Meta:
        model = Plan

admin.site.register(Plan, PlanAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    search_fields = ['Subject']
    class Meta:
        model = Contact_Us

admin.site.register(Contact_Us, ContactUsAdmin)
