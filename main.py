import logging
import requests
import os
import messages as responses
from github import Github
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


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


def getChallenge(id_challenge):
    """Recibe un ID y busca en el repo tal challenge o el ultimo si no existe"""
    contents = REPO.get_contents("")
    for content_file in contents:
        splitted_path = content_file.path.split("-")
        id = splitted_path[0] if len(splitted_path) > 1 else None
        if id != None and int(id) == int(id_challenge):
            return content_file
    if challenge == None:
        return REPO.get_contents("")[-3]


def actualChallenge(update, context):
    """Busca el reto actual o por id de challenge"""
    splitted = update.message.text.split()
    id_challenge = splitted[1] if len(splitted) > 1 else None
    challenge = None
    if id_challenge:
        logger.info(f"USER {update.message.from_user.id} /challenge {id_challenge}")
        challenge = getChallenge(id_challenge)
    else:
        logger.info(f"USER {update.message.from_user.id} /challenge")
        # Accedemos a la ultima carpeta (menos README y menos LICENSE = ultima carpeta)
        challenge = REPO.get_contents("")[-3]

    # Accedemos al readme
    readme_url = REPO.get_contents(f"{challenge.path}/README.md").download_url
    readme = requests.get(readme_url).text

    # Replace para parsear markdown normal al de telegram
    readme = readme.replace('**','*').replace('#',' ') 

    update.message.reply_markdown_v2(responses.normalize_markdown(readme))


def allChallenges(update, context):
    """Lista todos los challenges disponibles para luego acceder por id"""
    logger.info(f"USER {update.message.from_user.id} /all")
    challenges = REPO.get_contents("")
    
    keyboard = []
    for challenge in challenges:
        splitted = challenge.path.split("-")
        id = splitted[0] if len(splitted) > 1 else None
        if id != None:
            keyboard.append([InlineKeyboardButton(f"{id} - {splitted[1]}", callback_data = id.__str__())])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id= update.message.chat.id, reply_markup= reply_markup, text= 'Todos los desafios disponibles:')


def selectedChallenge(update, context):
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()
    
    challenge = getChallenge(query.data)
    readme_url = REPO.get_contents(f"{challenge.path}/README.md").download_url
    readme = requests.get(readme_url).text

    # Replace para parsear markdown normal al de telegram
    readme = readme.replace('**','*').replace('#',' ') 
    update.callback_query.message.reply_markdown_v2(responses.normalize_markdown(readme))
    #query.edit_message_text(text= responses.normalize_markdown(readme))


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
    dispatcher.add_handler(CommandHandler("list", allChallenges))
    dispatcher.add_handler(CallbackQueryHandler(selectedChallenge))

    # Handler para errores
    dispatcher.add_error_handler(error)

    # Iniciar bot
    updater = run(updater)
    updater.idle()


if __name__ == '__main__':
    main()
