Introduction
------------

The mortgage package computes mortgage amortizations.  Generally in real life
the principle and interest portions that this computes is not your entire
mortgage payment.  Other items include escrow payments for taxes and insurance.

.. image:: https://travis-ci.org/jbmohler/mortgage.png?branch=master
  :target: https://travis-ci.org/jbmohler/mortgage

From the command line one can get an summary of the mortgage totals.  For
example, show a bunch of details for loan of $350,000 at 3.75 interest rate.

>>> import mortgage
>>> m=mortgage.Mortgage(interest=0.0375, amount=350000, months=360)
>>> mortgage.print_summary(m)
                     Rate:      0.037500
             Month Growth:      1.003125
                      APY:      0.038151
             Payoff Years:            30
            Payoff Months:           360
                   Amount:     350000.00
          Monthly Payment:       1620.91
           Annual Payment:      19450.92
             Total Payout:     583527.60

Individual Computations
-----------------------

Or one can see bits and pieces of these computations.

>>> m=mortgage.Mortgage(interest=0.04, amount=150000, months=180)
>>> m.monthly_payment()
Decimal('1109.54')
>>> m.total_payout()
Decimal('199717.20')

Show the principle and interest break-down for the first 6 months.

>>> for index, payment in enumerate(m.monthly_payment_schedule()):
...     print(payment)
...     if index == 5: break
(Decimal('609.54'), Decimal('500.00'))
(Decimal('611.57'), Decimal('497.97'))
(Decimal('613.61'), Decimal('495.93'))
(Decimal('615.66'), Decimal('493.88'))
(Decimal('617.71'), Decimal('491.83'))
(Decimal('619.77'), Decimal('489.77'))

We can find the amount of principle paid in the first year.

>>> from itertools import islice
>>> sum(month[0] for month in islice(m.monthly_payment_schedule(), 12))
Decimal('7450.10')
>>> sum(month[0] for month in islice(m.monthly_payment_schedule(), 12, 24))
Decimal('7753.61')

We can verify that we'll be done in 15 years (180 months):

>>> payments = list(m.monthly_payment_schedule())
>>> assert len(payments) == 180
>>> payments[-1]
(Decimal('1103.77'), Decimal('3.68'))

Refinance Analysis
------------------

A pet peeve of the author is that the lower monthly payment is marketed as the
driver of all re-financing decisions.  We'll show here how much you would
payout in interest for a 30 year mortgage in two scenarios:  one with no
refinance and second with a refinance at year 15.

>>> m = mortgage.Mortgage(interest=0.035, amount=200000, months=360)
>>> sum(month[1] for month in islice(m.monthly_payment_schedule(), 360))
Decimal('123311.97')

So paying off the mortgage month by month results in total interest payments
$123,311.97.

>>> p15 = sum(month[0] for month in islice(m.monthly_payment_schedule(), 180))
>>> i15 = sum(month[1] for month in islice(m.monthly_payment_schedule(), 180))
>>> balance = mortgage.dollar(m.amount()) - p15
>>> balance
Decimal('125627.41')
>>> m2 = mortgage.Mortgage(interest=0.035, amount=balance, months=360)
>>> m2.monthly_payment(), m.monthly_payment()
(Decimal('564.13'), Decimal('898.09'))

The refinanced 30 year mortgage will indeed have a much lower monthly payment
of $564.13 instead of $898.09.

>>> i30_2 = sum(month[1] for month in islice(m2.monthly_payment_schedule(), 360))
>>> i15+i30_2
Decimal('164738.60')

That lower payment resulted in the mortgagee paying a mortgage for 45 years
instead of 30 and increased the total interest from $123,311.97 to $164,738.60.
Is the pleasure of a lower payment really worth roughly $40,000 more interest
expense?
