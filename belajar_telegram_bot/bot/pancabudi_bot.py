from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.callbackcontext import CallbackContext

class PancaBudi:
    """Nama bot : belajar-python, username bot : @pancabudi_bot"""

    def __init__(self):
        self.__token        =   '5239973610:AAGjpcMyIn0k-4LCKP4YR7uR5nTHWWOgvI4';
        self.__botName      =   'belajar-python'
        self.__botUsername  =   '@pancabudi_bot'

        _updater            =   Updater(token=self.__token, use_context=True)
        _dispatcher         =   _updater.dispatcher

        self.__updater        =   _updater
        self.__dispatcher     =   _dispatcher

        _d  =   _dispatcher
        _d.add_handler(CommandHandler('sayHello', self.tM_sayHello))
        _d.add_handler(CommandHandler('sayGoodBye', self.tM_sayGoodBye))

        _d.add_handler(MessageHandler(Filters.text, self.unknown))
        _d.add_handler(MessageHandler(Filters.command, self.unknown))
    
    def start(self):
        _updater    =   self.__updater
        _updater.start_polling()

        print(self.__botName, '(@'+self.__botUsername+') has been started!')

    def stop(self):
        _updater    =   self.__updater
        _updater.stop()

        print(self.__botName, '('+self.__botUsername+') has been stopped!')

    def unknown(self, update : Update, context : CallbackContext):
        update.message.reply_text('I do not understand your command!')


    #tM = Telegran Message
    def tM_sayHello(self, update : Update, context : CallbackContext):
        update.message.reply_text('Hello brother!')

    def tM_sayGoodBye(self, update : Update, context : CallbackContext):
        update.message.reply_text('Good Bye brother!')