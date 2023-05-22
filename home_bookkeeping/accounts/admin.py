from django.contrib import admin

from .models import (Accounting, ExpenseCalculation, IncomeCalculation,
                     СategoryExpense, СategoryIncome)


@admin.register(СategoryIncome)
class СategoryIncomeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_filter = ("name",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(СategoryExpense)
class СategoryExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_filter = ("name",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(IncomeCalculation)
class IncomeCalculationAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "incomes",
        "categories",
        "sum",
    )
    list_filter = ("categories", "incomes")
    search_fields = ("categories", "incomes")
    empty_value_display = "-пусто-"


@admin.register(ExpenseCalculation)
class ExpenseCalculationAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "expenses",
        "categories",
        "sum",
    )
    list_filter = ("categories", "expenses")
    search_fields = ("categories", "expenses")
    empty_value_display = "-пусто-"


class IncomeCalculationInline(admin.TabularInline):
    model = IncomeCalculation


class ExpenseCalculationInline(admin.TabularInline):
    model = ExpenseCalculation


@admin.register(Accounting)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("pk", "users", "year", "month")
    list_filter = ("users",)
    search_fields = ("users",)
    inlines = [IncomeCalculationInline, ExpenseCalculationInline]
    empty_value_display = "-пусто-"
