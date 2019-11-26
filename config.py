import daiquiri, logging

DATA_DIR = "./data/"
daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger()
