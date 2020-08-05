from django.contrib import admin
from .models import Request, Volunteer
from django.forms import TextInput, Textarea
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe

class RequestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id','created_date', 'last_edit', 'status','requester_link','phone','city','items_list','urgency',)
    list_display_links = ('id',)
    list_filter = ('status','city', 'volunteer_status')
    list_editable = ('status','items_list')
    search_fields = ('id','requester__first_name','requester__last_name','phone','address1','city','zip_code',)
    list_per_page = 25
    readonly_fields = ('requester_link',)

    def requester_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.requester._meta.app_label,  obj.requester._meta.model_name),  args=[obj.requester.id] ),
            obj.requester
        ))
    requester_link.short_description = 'Requester Info'

    def save_model(self, request, obj, form, change):
        if change and request.user.is_staff:
            month = str(timezone.now().month)
            day = str(timezone.now().day)
            admin = request.user.first_name
            obj.last_edit = "{}-{} by {}".format(month,day,admin)
        obj.save()

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'supporter','request_link', 'status','created_date')
    list_display_links = ('id',)
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('id','supporter__first_name', 'supporter__last_name', 'request__requester__first_name', 'request__requester__last_name', 'request__id')
    list_per_page = 25
    readonly_fields = ('supporter','request', 'request_link')

    def request_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('admin:%s_%s_change' % (obj.request._meta.app_label,  obj.request._meta.model_name),  args=[obj.request.id] ),
            obj.request
        ))
    request_link.short_description = 'Request Info'

admin.site.register(Request, RequestAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
