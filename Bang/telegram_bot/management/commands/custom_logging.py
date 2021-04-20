import logging
from .db_usage import write_user_logs


def custom_logging(action, update):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username}:{action} ")
    write_user_logs(update=update, action=action)
