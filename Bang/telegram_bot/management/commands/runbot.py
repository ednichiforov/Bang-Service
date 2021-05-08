from django.core.management.base import BaseCommand

from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CommandHandler,
    ConversationHandler,
)

from telegram_bot.bot_info_commands import start, commands, unknown_command, error
from telegram_bot.bot_registration_commands import (
    first_name_reg,
    last_name_reg,
    number_reg,
    registration_end,
    user_cancel,
)
from telegram_bot.bot_admin_commands import (
    admin_starts_conv,
    admin_loading_info,
    admin_cancel,
)


FIRST_NAME_REG, LAST_NAME_REG, NUMBER_REG, USER_REGISTER_END = range(4)

ADMIN_CONV, LOADING_INFO = range(2)


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(
            token="1731613284:AAFb38FNilx8DyedftJFnsgiiOywHLeTMBY",
            use_context=True,
        )

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler(command="start", callback=start))

        dispatcher.add_handler(
            MessageHandler(
                filters=Filters.regex("^(DJ SCHOOL|Вечеринки|Барное меню)$"),
                callback=commands,
            )
        )

        user_conv_handler = ConversationHandler(
            entry_points=[
                MessageHandler(
                    filters=Filters.regex("^(Попасть в списки)$"),
                    callback=first_name_reg,
                ),
                CommandHandler(command="user_cancel", callback=user_cancel),
            ],
            states={
                FIRST_NAME_REG: [
                    MessageHandler(filters=Filters.text, callback=first_name_reg),
                    CommandHandler(command="user_cancel", callback=user_cancel),
                ],
                LAST_NAME_REG: [
                    MessageHandler(filters=Filters.text, callback=last_name_reg),
                    CommandHandler(command="user_cancel", callback=user_cancel),
                ],
                NUMBER_REG: [
                    MessageHandler(filters=Filters.text, callback=number_reg),
                    CommandHandler(command="user_cancel", callback=user_cancel),
                ],
                USER_REGISTER_END: [
                    MessageHandler(filters=Filters.text, callback=registration_end),
                ],
            },
            fallbacks=[CommandHandler(command="user_cancel", callback=user_cancel)],
            allow_reentry=True,
        )

        dispatcher.add_handler(user_conv_handler)

        admin_conv_handler = ConversationHandler(
            entry_points=[
                CommandHandler(command="Gappa", callback=admin_starts_conv),
                CommandHandler(command="admin_cancel", callback=admin_cancel),
            ],
            states={
                ADMIN_CONV: [
                    MessageHandler(filters=Filters.all, callback=admin_starts_conv),
                    CommandHandler(command="admin_cancel", callback=admin_cancel),
                ],
                LOADING_INFO: [
                    MessageHandler(filters=Filters.all, callback=admin_loading_info),
                ],
            },
            fallbacks=[CommandHandler(command="admin_cancel", callback=admin_cancel)],
            allow_reentry=True,
        )

        dispatcher.add_handler(admin_conv_handler)
        dispatcher.add_handler(MessageHandler(Filters.all, callback=unknown_command))
        dispatcher.add_error_handler(error)
        updater.start_polling(poll_interval=0.5)

        updater.idle()
