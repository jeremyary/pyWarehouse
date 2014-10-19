from django.contrib import admin
from warehouse.models import Worker
from warehouse.models import Classification
from warehouse.models import Order

class ClassificationsWorkerInline(admin.TabularInline):
    model = Worker.classifications.through
    fields = ['classification', 'worker']
    extra = 0

class WorkerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Employee Name', {
                'fields': ['first_name', 'last_name']
        }),
        ('Employee Info', {
                'classes': ['collapse',],
                'fields': ['age', 'start_date']
        }),
    ]
    inlines = [ClassificationsWorkerInline]

class ClassificationAdmin(admin.ModelAdmin):
    fields = ['title',]

class ClassificationsOrderInline(admin.TabularInline):
    model = Order.classifications.through
    fields = ['classification', 'order']
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
                'fields': ['item', 'quantity', 'status', 'placed']
        }),
    ]
    inlines = [ClassificationsOrderInline]

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Order, OrderAdmin)
