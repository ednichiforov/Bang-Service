import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def custom_info_logging(action, update):
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username}:{action}")


def custom_warning_logging(update, _):
    logger.warning(f'Update {update} caused error {_}')
