import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate=False

handler = logging.FileHandler('E:/ArtKaduna/syslog.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
