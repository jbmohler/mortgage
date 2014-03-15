The mortgage package computes mortgage amortizations.  Generally in real life
the principle and interest portions that this computes is not your entire
mortgage payment.  Other items include escrow payments for taxes and insurance.

.. image:: https://travis-ci.org/jbmohler/mortgage.png?branch=master
  :target: https://travis-ci.org/jbmohler/mortgage

From the command line one can get an summary of the mortgage totals:

>>> import mortgage
>>> # Show bunch of details for loan of $350,000 at 3.75 interest rate.
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

Or one can see bits and pieces of these computations.

>>> m=mortgage.Mortgage(interest=0.04, amount=150000, months=180)
>>> m.monthly_payment()
1109.54
>>> m.total_payout()
199717.19999999998

>>> # Show the principle and interest break-down for the first 6 months.
>>> for index, payment in enumerate(m.monthly_payment_schedule()):
...     print(payment)
...     if index == 5: break
(609.54, 500.0)
(611.5699999999999, 497.97)
(613.6099999999999, 495.93)
(615.66, 493.88)
(617.71, 491.83)
(619.77, 489.77)

>>> # Find the amount of principle in the first year.
>>> import itertools
>>> sum(month[0] for month in itertools.islice(m.monthly_payment_schedule(), 12))
7450.0999999999985

>>> # verify that we'll be done in 15 years (180 months)
>>> payments = list(m.monthly_payment_schedule())
>>> assert len(payments) == 180
>>> payments[-1]
(1103.770000000069, 3.68)
