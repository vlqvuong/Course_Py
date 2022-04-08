from os import getenv

MONGOHOST = getenv("MONGOHOST", "localhost")
MONGOPORT = getenv("MONGOPORT", 27017)
MONGOUSER = getenv("MONGOUSER", "root")
MONGOPASS = getenv()