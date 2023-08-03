Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import math
... 
... def compute_payment(PV, r, n):
...     r = r / 12.0
...     payment = PV * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
...     return payment
... 
... def compute_PV(pmt, r, n):
...     r = r / 12.0
...     PV = pmt / (r * (1 - (1 + r) ** -n))
...     return PV
... 
... def compute_months(PV, r, pmt):
...     r = r / 12.0
...     n = np.log(1 - PV * r / pmt) / np.log(1 + r)
...     return n
... 
... 
... PV = 10000
... r = 0.06
... pmt = 500
... 
... n = 12 * 5
... payment = compute_payment(PV, r, n)
... print("Monthly payment:", payment)
... 
... n = 12 * 3
... PV = compute_PV(pmt, r, n)
... print("Maximum borrowing amount:", PV)
... 
... n = compute_months(PV, r, pmt)
... print("Number of months to pay off the loan:", n)
