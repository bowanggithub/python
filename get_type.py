print("type(123)=", type(123))
print("type(\'123\')=", type('123'))
print('type(None) =', type(None))
print("type(abs)= ", type(abs))

import types

print("type(\'abc\')==str?", type('abc')==str)

def fn():
    pass

type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x:x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType
