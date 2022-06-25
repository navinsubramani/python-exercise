# Please raise a RuntimeError exception.

try:
    raise RuntimeError('custom error 50005')

except(RuntimeError) as err:
    print(err)
