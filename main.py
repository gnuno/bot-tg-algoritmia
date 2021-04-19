import logging
import os
from telegram.ext import Updater, CommandHandler


### Configurar Login
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


### Variables necesarias para el BOT
API_TOKEN = ""


### Comandos del BOT
def start(update, context):
    """Mensaje de bienvenida al iniciar"""
    logger.info(f"USER {update.message.from_user.id} /start")

    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hola {user.mention_markdown_v2()}\!',
    )


def help_command(update, context):
    """Mensaje de ayuda al usar /help"""
    logger.info(f"USER {update.message.from_user.id} /help")
    
    update.message.reply_text('nostas biendo kestoi chikito bieja tonta {}'.format(5))


def error(update, context):
    """Loggea los errores causados por el Updater"""    
    logger.warning(f'Update {update} caused error {context.error}')


### Inicio del bot y handlers
def main():
    """Inicia el bot."""
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    # Handler para cada comando
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Handler para errores
    dispatcher.add_error_handler(error)

    # Iniciar bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()