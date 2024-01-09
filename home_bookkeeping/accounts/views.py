from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (AccountingForm, EditExpenseCalculationForm,
                    EditIncomeCalculationForm, ExpenseCalculationForm,
                    IncomeCalculationForm)
from .models import Accounting, ExpenseCalculation, IncomeCalculation
from .utils import get_plot

FORM_INCOME = IncomeCalculationForm()
FORM_EXPENSE = ExpenseCalculationForm()

LIMIT = 12


def index(request):
    return render(request, 'accounts/index.html')


@login_required
def accounting(request):
    accountings = Accounting.objects.filter(users=request.user).annotate(
        incomes_sum=Sum('calculation_incomes__sum', distinct=True),
        expense_sum=Sum('calculation_expense__sum'),
    )

    page_obj = Paginator(accountings, LIMIT).get_page(request.GET.get('page'))

    form = AccountingForm(request.POST or None, initial={'user': request.user})
    if form.is_valid():
        new_date = form.save(commit=False)
        new_date.users = request.user
        new_date.save()
        return redirect('accounts:accounting')

    context = {'page_obj': page_obj, 'accountings': accountings, 'form': form}
    return render(request, 'accounts/accounting.html', context)


@login_required
def accounting_detail(
    request, accounting_id, form_income=FORM_INCOME, form_expense=FORM_EXPENSE
):
    accounting = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    incomes = accounting.calculation_incomes.all()
    expenses = accounting.calculation_expense.all()

    form_income_data = []
    for instance_income in incomes:
        income_one = EditIncomeCalculationForm(instance=instance_income)
        form_income_data.append(income_one)

    form_expense_data = []
    for instance_expense in expenses:
        expense_one = EditExpenseCalculationForm(instance=instance_expense)
        form_expense_data.append(expense_one)

    accounting_sum = Accounting.objects.filter(users=request.user).annotate(
        incomes_sum=Sum('calculation_incomes__sum', distinct=True),
        expense_sum=Sum('calculation_expense__sum'),
    )
    incomes_number = accounting_sum[0].incomes_sum
    if not incomes_number:
        incomes_number = 0
    expense_number = accounting_sum[0].expense_sum
    if not expense_number:
        expense_number = 0
    difference = incomes_number - expense_number
    field_name = ['Остаток\nсредств', 'Расходы', 'Доходы']
    points = [difference, expense_number, incomes_number]
    chart = get_plot(field_name, points)

    context = {
        'accounting': accounting,
        'incomes': incomes,
        'expenses': expenses,
        'form_income': form_income,
        'form_expense': form_expense,
        'form_income_data': form_income_data,
        'form_expense_data': form_expense_data,
        'chart': chart,
    }
    return render(request, 'accounts/accounting_detail.html', context)


@login_required
def create_income(request, accounting_id):
    accounting = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    form_income = IncomeCalculationForm(
        request.POST or None, initial={'accounting': accounting}
    )
    if form_income.is_valid():
        form_income = form_income.save(commit=False)
        form_income.incomes = accounting
        form_income.save()
        return redirect('accounts:accounting_detail', accounting_id)
    return accounting_detail(request, accounting_id, form_income=form_income)


@login_required
def edit_income(request, accounting_id, income_id):
    incomes = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    instance = get_object_or_404(
        IncomeCalculation, id=income_id, incomes=incomes
    )
    form = EditIncomeCalculationForm(request.POST or None, instance=instance)
    if form.is_valid():
        form_income = form.save(commit=False)
        form_income.incomes = incomes
        form_income.save()
    return redirect('accounts:accounting_detail', accounting_id)


@login_required
def delte_income(request, accounting_id, income_id):
    incomes = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    IncomeCalculation.objects.filter(id=income_id, incomes=incomes).delete()
    return redirect('accounts:accounting_detail', accounting_id)


@login_required
def create_expense(request, accounting_id):
    accounting = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    form_expense = ExpenseCalculationForm(
        request.POST or None, initial={'accounting': accounting}
    )
    if form_expense.is_valid():
        form_expense = form_expense.save(commit=False)
        form_expense.expenses = accounting
        form_expense.save()
        return redirect('accounts:accounting_detail', accounting_id)
    return accounting_detail(request, accounting_id, form_expense=form_expense)


@login_required
def edit_expense(request, accounting_id, expense_id):
    expense = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    instance = get_object_or_404(
        ExpenseCalculation, id=expense_id, expenses=expense
    )
    form = EditExpenseCalculationForm(request.POST or None, instance=instance)
    if form.is_valid():
        form_expense = form.save(commit=False)
        form_expense.expenses = expense
        form_expense.save()
    return redirect('accounts:accounting_detail', accounting_id)


@login_required
def delte_expense(request, accounting_id, expense_id):
    expense = get_object_or_404(
        Accounting, users=request.user, id=accounting_id
    )
    ExpenseCalculation.objects.filter(id=expense_id, expenses=expense).delete()
    return redirect('accounts:accounting_detail', accounting_id)
