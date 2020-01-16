"""I have been wanting to use s.describe in py2, but it will throw an error
    in paring the file, so I have to completely remove it from the import
    """
# Only for 3 because scope must be an int
def iprint(x, scope: int=1, **kwargs):
    """This prints items indented by 4 spaces, to help clarify scope of
    operations. x is the value intended to be printed, scope is an integer
    of the number of indents desired.
    """
    print("", x, sep="    "*scope, **kwargs)
