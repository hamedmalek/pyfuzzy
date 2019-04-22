from __future__ import division #added for float devision in both python 2 & 3
import decimal

def zmf(x,params):
  #checking validation of parameters (params) and the input value (x)
  if not isinstance(params, list):
        raise TypeError ("Params should be a list.")
  if len(params) != 2:
        raise TypeError ("Two values in Params list are expected.")
  if not (isinstance(x, (int, float, decimal.Decimal)) and isinstance(params[0], (int, float, decimal.Decimal)) and isinstance(params[1], (int, float, decimal.Decimal))):
        raise TypeError ("Input and Parameters should be number.")

  a=params[0]
  b=params[1]
  if x<=a:
    return 1
  if a<=x and x<= ((a+b)/2):
    return 1-2*(((x-a)/(b-a))**2)
  if (a+b)/2<=x and x<=b:
    return 2*(((b-x)/(b-a))**2)
  if b<=x:
    return 0  