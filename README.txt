The mortgage package computes mortgage amortizations.

>>> import mortgage
>>> m=mortgage.Mortgage(interest=0.04, amount=150000, months=180)
>>> m.monthly_payment()
1109.53
