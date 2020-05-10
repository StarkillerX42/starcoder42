import subprocess as sub

sub.call('f2py -c ftarcoder42.pyf constantf.f90 mathf.f90 physicf.f90 -m'
         ' ftarcoder42', shell=True)
