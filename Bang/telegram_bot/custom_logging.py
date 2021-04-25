import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def custom_info_logging(func):
    def inner(update, _):
        user = update.message.from_user
        logger.info(f"{user.first_name}/{user.username} pressed {func.__name__}")
        return func(update, _)
    return inner


def custom_warning_logging(func):
    def inner(update, _):
        logger.warning(f'Update {update} caused error {_}')
        return func(update, _)
    return inner
