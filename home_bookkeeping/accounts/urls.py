from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounting/', views.accounting, name='accounting'),
    path(
        'accounting/<int:accounting_id>/',
        views.accounting_detail,
        name='accounting_detail',
    ),
    path(
        'accounting/<int:accounting_id>/income/create/',
        views.create_income,
        name='create_income',
    ),
    path(
        'accounting/<int:accounting_id>/income/<int:income_id>/edit/',
        views.edit_income,
        name='edit_income',
    ),
    path(
        'accounting/<int:accounting_id>/income/<int:income_id>/delete/',
        views.delte_income,
        name='delte_income',
    ),
    path(
        'accounting/<int:accounting_id>/expense/create/',
        views.create_expense,
        name='create_expense',
    ),
    path(
        'accounting/<int:accounting_id>/expense/<int:expense_id>/edit/',
        views.edit_expense,
        name='edit_expense',
    ),
    path(
        'accounting/<int:accounting_id>/expense/<int:expense_id>/delete/',
        views.delte_expense,
        name='delte_expense',
    ),
]
