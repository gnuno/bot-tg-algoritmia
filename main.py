import logging
import requests
import os
import messages as responses
from github import Github
from telegram.ext import Updater, CommandHandler


### Configurar Login
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

### Variables para el Telegram BOT
PORT = int(os.environ.get('PORT', 8443))
MODE = os.environ.get('MODE')

# Bifurcacion para produccion y desarrollo
if MODE == 'prod':
    API_TOKEN = os.environ.get('TOKEN')
    APP_NAME = os.environ.get('NAME')
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
    def run(updater):
        updater.start_webhook(listen="0.0.0.0",
            port= PORT,
            url_path= API_TOKEN,
            webhook_url= f"https://{APP_NAME}.herokuapp.com/{API_TOKEN}")
        return updater
else:
    API_TOKEN = '' #Copiar aca el token
    dusty_token = '///gh//p_w//zlsG//PbF//5X2nA//mmy//ySzhM//TEmF//137//QY2v//tKNN/'
    GITHUB_TOKEN = dusty_token.replace('/','')
    def run(updater):
        updater.start_polling()
        return updater

### Variables para GitHub API
g = Github(GITHUB_TOKEN)
REPO = g.get_repo('gnuno/algoritmia')

### Comandos del BOT
def start(update, context):
    """Mensaje de bienvenida al iniciar"""
    logger.info(f"USER {update.message.from_user.id} /start")

    user = update.effective_user
    update.message.reply_markdown_v2(f'Hola *{user.mention_markdown_v2()}*\!\nPara ver los comandos disponebles escribí */help*')


def help_command(update, context):
    """Mensaje de ayuda al usar /help"""
    logger.info(f"USER {update.message.from_user.id} /help")
    
    update.message.reply_markdown_v2(responses.help_message())


def actualChallenge(update, context):
    """Busca el reto actual"""
    logger.info(f"USER {update.message.from_user.id} /challenge")

    # Accedemos a la ultima carpeta (menos README y menos LICENSE = ultima carpeta)
    challenge = REPO.get_contents("")[-3]
    # Accedemos al readme
    readme_url = REPO.get_contents(f"{challenge.path}/README.md").download_url
    readme = requests.get(readme_url).text

    # Replace para parsear markdown normal al de telegram
    readme = readme.replace('**','*').replace('#',' ') 
    
    update.message.reply_markdown_v2(responses.normalize_markdown(readme))


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
    dispatcher.add_handler(CommandHandler("challenge", actualChallenge))

    # Handler para errores
    dispatcher.add_error_handler(error)

    # Iniciar bot
    updater = run(updater)
    updater.idle()


if __name__ == '__main__':
    main()
