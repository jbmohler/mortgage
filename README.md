The mortgage package computes mortgage amortizations.  Generally in real life
the principle and interest portions that this computes is not your entire
mortgage payment.  Other items include escrow payments for taxes and insurance.

[![Build Status](https://travis-ci.org/jbmohler/mortgage.png?branch=master)](https://travis-ci.org/jbmohler/mortgage)

First one can see how much total payout a mortgage would take at arbitrary
terms.

>>> import mortgage
>>> m=mortgage.Mortgage(interest=0.04, amount=150000, months=180)
>>> m.monthly_payment()
1109.54
>>> m.total_payout()
199717.19999999998

>>> # Show the principle and interest break-down for the first 6 months.
>>> for index, payment in enumerate(m.monthly_payment_schedule()):
...     print payment
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
>>> print payments[-1]
(1103.770000000069, 3.68)
