#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import argparse

MONTHS_IN_YEAR = 12

class Mortgage:
    def __init__(self, interest, months, amount):
        self._interest = float(interest)
        self._months = int(months)
        self._amount = float(amount)

    def rate(self):
        return self._interest

    def month_growth(self):
        return 1. + self._interest / MONTHS_IN_YEAR

    def apy(self):
        return self.month_growth() ** MONTHS_IN_YEAR - 1

    def loan_years(self):
        return float(self._months) / MONTHS_IN_YEAR

    def loan_months(self):
        return self._months

    def amount(self):
        return self._amount

    def monthly_payment(self):
        pre_amt = self.amount() * self.rate() / (float(MONTHS_IN_YEAR) * (1.-(1./self.month_growth()) ** self.loan_months()))
        return float(int(pre_amt * 100))/100

    def total_value(self, m_payment):
        return m_payment / self.rate() * (float(MONTHS_IN_YEAR) * (1.-(1./self.month_growth()) ** self.loan_months()))

    def annual_payment(self):
        return self.monthly_payment() * MONTHS_IN_YEAR

    def total_payout(self):
        return self.monthly_payment() * self.loan_months()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mortgage Amortization Tools')
    parser.add_argument('-i', '--interest', default=6, dest='interest')
    parser.add_argument('-y', '--loan-years', default=30, dest='years')
    parser.add_argument('-m', '--loan-months', default=None, dest='months')
    parser.add_argument('-a', '--amount', default=100000, dest='amount')
    args = parser.parse_args()

    if args.months:
        m = Mortgage(float(args.interest) / 100, float(args.months), args.amount)
    else:
        m = Mortgage(float(args.interest) / 100, float(args.years) * MONTHS_IN_YEAR, args.amount)

    print '%*s:  %*.*f' % (25, 'Rate', 12, 6, m.rate())
    print '%*s:  %*.*f' % (25, 'Month Growth', 12, 6, m.month_growth())
    print '%*s:  %*.*f' % (25, 'APY', 12, 6, m.apy())
    print '%*s:  %*.*f' % (25, 'Payoff Years', 12, 0, m.loan_years())
    print '%*s:  %*.*f' % (25, 'Payoff Months', 12, 0, m.loan_months())
    print '%*s:  %*.*f' % (25, 'Amount', 12, 2, m.amount())
    print '%*s:  %*.*f' % (25, 'Monthly Payment', 12, 2, m.monthly_payment())
    print '%*s:  %*.*f' % (25, 'Annual Payment', 12, 2, m.annual_payment())
    print '%*s:  %*.*f' % (25, 'Total Payout', 12, 2, m.total_payout())
