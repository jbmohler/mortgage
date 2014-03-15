import mortgage
import decimal

def test_dollar():
    assert mortgage.dollar(12.3453) == decimal.Decimal('12.35')
