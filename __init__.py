from os.path import dirname, basename, isfile, join
from importlib import import_module
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

#https://stackoverflow.com/questions/2933470/how-do-i-call-setattr-on-the-current-module
#https://stackoverflow.com/questions/17929222/how-to-import-package-modules-from-packages-init-py
for name in __all__:
    mod = import_module('.'+name,__name__)
    globals()[name] = getattr(mod,name)
    