The mortgage package computes mortgage amortizations.

First one can see how much total payout a mortgage would take at arbitrary
terms.

>>> import mortgage
>>> m=mortgage.Mortgage(interest=0.04, amount=150000, months=180)
>>> m.monthly_payment()
1109.53
>>> m.total_payout()
199715.4
