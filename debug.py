DEBUG = False
MINI_DEBUG = False

if DEBUG and MINI_DEBUG:
    raise Exception("Only enable one of DEBUG, MINI_DEBUG")