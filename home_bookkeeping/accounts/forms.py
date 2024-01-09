from django import forms

from .models import Accounting, ExpenseCalculation, IncomeCalculation


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = ['year', 'month']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'month': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cd = self.cleaned_data
        user = self.initial['user']
        accounting = Accounting.objects.filter(
            users=user, year=cd.get('year'), month=cd.get('month')
        )
        if accounting.exists():
            raise forms.ValidationError('Дата и год уже есть')
        return cd


class IncomeCalculationForm(forms.ModelForm):
    class Meta:
        model = IncomeCalculation
        fields = ['categories', 'sum']
        widgets = {
            'categories': forms.Select(attrs={'class': 'form-select'}),
            'sum': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Сумма'}
            ),
        }

    def clean(self):
        cd = self.cleaned_data
        accounting = self.initial['accounting']
        income = IncomeCalculation.objects.filter(
            incomes=accounting, categories=cd.get('categories')
        )
        if income.exists():
            raise forms.ValidationError('Категория уже есть')
        return cd


class EditIncomeCalculationForm(forms.ModelForm):
    class Meta:
        model = IncomeCalculation
        fields = ['sum']
        widgets = {
            'sum': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Сумма'}
            ),
        }


class ExpenseCalculationForm(forms.ModelForm):
    class Meta:
        model = ExpenseCalculation
        fields = ['categories', 'plan', 'sum']
        widgets = {
            'categories': forms.Select(attrs={'class': 'form-select'}),
            'plan': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'План'}
            ),
            'sum': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Сумма'}
            ),
        }

    def clean(self):
        cd = self.cleaned_data
        accounting = self.initial['accounting']
        expense = ExpenseCalculation.objects.filter(
            expenses=accounting, categories=cd.get('categories')
        )
        if expense.exists():
            raise forms.ValidationError('Категория уже есть')
        return cd


class EditExpenseCalculationForm(forms.ModelForm):
    class Meta:
        model = ExpenseCalculation
        fields = ['plan', 'sum']
        widgets = {
            'plan': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'План'}
            ),
            'sum': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Сумма'}
            ),
        }
