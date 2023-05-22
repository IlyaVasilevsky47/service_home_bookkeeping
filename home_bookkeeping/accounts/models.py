import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

YEAR_CHOICES = [(y, y) for y in range(2020, datetime.date.today().year + 3)]
MONTH_CHOICE = [(m, m) for m in range(1, 13)]


class СategoryIncome(models.Model):
    name = models.CharField(
        verbose_name="Название", unique=True, max_length=200
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("id",)
        verbose_name = "Категория дохода"
        verbose_name_plural = "Категории доходов"


class СategoryExpense(models.Model):
    name = models.CharField(
        verbose_name="Название", unique=True, max_length=200
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("id",)
        verbose_name = "Категория расхода"
        verbose_name_plural = "Категории расходов"


class Accounting(models.Model):
    users = models.ForeignKey(
        User,
        related_name="accounting_users",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    incomes = models.ManyToManyField(
        СategoryIncome,
        through="IncomeCalculation",
        related_name="accounting_incomes",
        verbose_name="Доход",
    )
    expense = models.ManyToManyField(
        СategoryExpense,
        through="ExpenseCalculation",
        related_name="accounting_expense",
        verbose_name="Расход",
    )
    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
        verbose_name="Год"
    )
    month = models.IntegerField(
        choices=MONTH_CHOICE,
        default=datetime.datetime.now().month,
        verbose_name="Месяц",
    )

    def __str__(self):
        return f"{self.users}-{self.year}.{self.month}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_accounting",
                fields=["users", "year", "month"],
            )
        ]
        ordering = ("-year", "-month")
        verbose_name = "Бухгалтерия"
        verbose_name_plural = "Бухгалтерии"


class IncomeCalculation(models.Model):
    incomes = models.ForeignKey(
        Accounting,
        related_name="calculation_incomes",
        on_delete=models.CASCADE,
        verbose_name="Доход",
    )
    categories = models.ForeignKey(
        СategoryIncome,
        related_name="calculation_categories",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    sum = models.IntegerField(verbose_name="Сумма")

    def __str__(self):
        return f"{self.categories}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_income",
                fields=["incomes", "categories"],
            )
        ]
        ordering = ("categories__id",)
        verbose_name = "Расчет доходов"
        verbose_name_plural = "Расчеты доходов"


class ExpenseCalculation(models.Model):
    expenses = models.ForeignKey(
        Accounting,
        related_name="calculation_expense",
        on_delete=models.CASCADE,
        verbose_name="Доход",
    )
    categories = models.ForeignKey(
        СategoryExpense,
        related_name="calculation_categories",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    plan = models.IntegerField(verbose_name="План")
    sum = models.IntegerField(verbose_name="Сумма")

    def __str__(self):
        return f"{self.categories}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_expense",
                fields=["expenses", "categories"],
            )
        ]
        ordering = ("categories__id",)
        verbose_name = "Расчет расходов"
        verbose_name_plural = "Расчеты расходов"
