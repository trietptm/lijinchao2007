TestCode='''def test():
    print 1111'''

#a = compile(TestCode, "a.py", "exec")
exec TestCode
test()
print locals()
print globals()

func = locals()["test"]
func()