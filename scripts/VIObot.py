# ===============================================================
# Author: Firdauz Fanani
# Email: firdauzfanani@gmail.com
# Twitter: @firdauzfanani
# ===============================================================

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from lang_dict import *
from lang_dict_viomenu import *
from lang_dict_vioproductmenu import *
from geo_app import *
import logging

# You might need to add your tokens to this file...
from credentials import *


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Global vars:
LANG = "EN"
SET_LANG, MENU, SET_STAT, VIODETAILS,VIOTEMP, HELP,ABOUTVIO, MAP, FAQ, ABOUT, LOCATION,VIOMAP,VIOSKETCH, WATERLVL,VIOPRODUCT,DCIM = range(16)
STATE = SET_LANG


def start(bot, update):
    """
    Start function. Displayed whenever the /start command is called.
    This function sets the language of the bot.
    """
    # Create buttons to slect language:
    keyboard = [['IND', 'EN']]

    # Create initial message:
    message = "Hey, I'm VIO Bot! / Hey, Saya VIO Bot! \n\n\
Please select a language to start. / Silahkan pilih bahasa untuk memulai"

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)

    return SET_LANG


def set_lang(bot, update):
    """
    First handler with received data to set language globally.
    """
    # Set language:
    global LANG
    LANG = update.message.text
    user = update.message.from_user

    logger.info("Language set by {} to {}.".format(user.first_name, LANG))
    update.message.reply_text(lang_selected[LANG],
                              reply_markup=ReplyKeyboardRemove())

    return MENU


def menu(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [[about_vio[LANG], view_about[LANG]],
                [view_vio[LANG], view_product[LANG]],
                [view_faq[LANG], view_help[LANG]]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("Menu command requested by {}.".format(user.first_name))
    update.message.reply_text(main_menu[LANG], reply_markup=reply_markup)

    return SET_STAT

def viomenu(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [[vio_map[LANG], vio_sketch[LANG]],
                [vio_temp[LANG], vio_waterlvl[LANG]]]

    if update.message.text == vio_sketch[LANG]:
        keyboard = [[vio_sketch1[LANG], vio_sketch2[LANG]],
                    [vio_sketch3[LANG], vio_sketch4[LANG]]]
    elif update.message.text == vio_temp[LANG]:
        keyboard = [[vio_temp1[LANG], vio_temp2[LANG]],
                    [vio_temp3[LANG], vio_temp4[LANG]]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("VIO Menu command requested by {}.".format(user.first_name))
    update.message.reply_text(main_menu[LANG], reply_markup=reply_markup)

    return SET_STAT

def vioproductmenu(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [[vio_dcim[LANG], vio_iotplatform[LANG]],
                [vio_goelf[LANG], vio_ework[LANG]],
                [vio_absensi[LANG], vio_chatbot[LANG]]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("VIO Menu command requested by {}.".format(user.first_name))
    update.message.reply_text(main_menu[LANG], reply_markup=reply_markup)

    return SET_STAT

def set_state(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == about_vio[LANG]:
        STATE = ABOUTVIO
        aboutvio_bot(bot, update)
        return MENU
    elif update.message.text == view_vio[LANG]:
        STATE = VIODETAILS
        viomenu(bot, update)
    elif update.message.text == view_product[LANG]:
        STATE = VIOPRODUCT
        vioproductmenu(bot, update)
    elif update.message.text == vio_map[LANG]:
        STATE = VIOMAP
        viomap(bot, update)
        return MENU
    elif update.message.text == vio_waterlvl[LANG]:
        STATE = WATERLVL
        viowaterlvl(bot, update)
        return MENU
    elif update.message.text == vio_dcim[LANG]:
        STATE = DCIM
        dcim(bot, update)
        return MENU
    elif update.message.text == vio_temp[LANG]:
        STATE = VIOTEMP
        viomenu(bot, update)
    elif update.message.text == vio_temp1[LANG]:
        STATE = VIOTEMP
        viotemp(bot, update, 1)
        return MENU
    elif update.message.text == vio_temp2[LANG]:
        STATE = VIOTEMP
        viotemp(bot, update, 2)
        return MENU
    elif update.message.text == vio_temp3[LANG]:
        STATE = VIOTEMP
        viotemp(bot, update, 3)
        return MENU
    elif update.message.text == vio_temp4[LANG]:
        STATE = VIOTEMP
        viotemp(bot, update, 4)
        return MENU
    elif update.message.text == vio_sketch[LANG]:
        STATE = VIOSKETCH
        viomenu(bot, update)
    elif update.message.text == vio_sketch1[LANG]:
        STATE = VIOSKETCH
        viosketch(bot, update, 1)
        return MENU
    elif update.message.text == vio_sketch2[LANG]:
        STATE = VIOSKETCH
        viosketch(bot, update, 2)
        return MENU
    elif update.message.text == vio_sketch3[LANG]:
        STATE = VIOSKETCH
        viosketch(bot, update, 3)
        return MENU
    elif update.message.text == vio_sketch4[LANG]:
        STATE = VIOSKETCH
        viosketch(bot, update, 4)
        return MENU
    elif update.message.text == view_faq[LANG]:
        STATE = FAQ
        faq(bot, update)
        return MENU
    elif update.message.text == view_help[LANG]:
        STATE = HELP
        help(bot, update)
        return MENU
    elif update.message.text == view_about[LANG]:
        STATE = ABOUT
        about_bot(bot, update)
        return MENU
    else:
        STATE = MENU
        return MENU


def report(bot, update):
    """
    FAQ function. Displays FAQ about disaster situations.
    """
    user = update.message.from_user
    logger.info("Report requested by {}.".format(user.first_name))
    update.message.reply_text(loc_request[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return


def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of {}: ({}, {})".format(
                user.first_name, user_location.latitude,
                user_location.longitude))
    report_map = geo_app()
    report_map.append_data(user_location.latitude, user_location.longitude)
    update.message.reply_text(loc_aquired[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return MENU


def viomap(bot, update):
    user = update.message.from_user
    logger.info("Maps requested by {}.".format(user.first_name))
    bot.sendLocation(chat_id=update.message.chat_id, latitude=-6.1977268, longitude=106.7468049)
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return

def viosketch(bot, update, lantai):
    user = update.message.from_user
    logger.info("Sketch requested by {}.".format(user.first_name))
    poto = open('../imgs/Lantai(%d).jpeg' % lantai, 'rb')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=poto)
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return

def viowaterlvl(bot, update):
    user = update.message.from_user
    logger.info("Water Level requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=waterlvl_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return

def viotemp(bot, update, lantai):
    user = update.message.from_user
    logger.info("Temperature requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=temp_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return

def dcim(bot, update):
    user = update.message.from_user
    logger.info("DCIM requested by {}.".format(user.first_name))
    poto = open('../imgs/dcim.png', 'rb')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=poto)
    bot.send_message(chat_id=update.message.chat_id, text=dcim_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return

def vmap(bot, update):
    """
    View map function. In development...
    """
    user = update.message.from_user
    logger.info("Map requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=map_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])

    # View map locally:
    report_map = geo_app()
    report_map.latlong_to_coords()
    report_map.visualize()
    return


def faq(bot, update):
    """
    FAQ function. Displays FAQ about disaster situations.
    """
    user = update.message.from_user
    logger.info("FAQ requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=faq_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return


def about_bot(bot, update):
    """
    About function. Displays info about VIO Bot.
    """
    user = update.message.from_user
    logger.info("About info requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=about_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return

def aboutvio_bot(bot, update):
    """
    About function. Displays info about vio.
    """
    user = update.message.from_user
    logger.info("About info requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text=vio_info[LANG])
    bot.send_message(chat_id=update.message.chat_id, text=back2menu[LANG])
    return


def help(bot, update):
    """
    Help function.
    This displays a set of commands available for the bot.
    """
    user = update.message.from_user
    logger.info("User {} asked for help.".format(user.first_name))
    update.message.reply_text(help_info[LANG],
                              reply_markup=ReplyKeyboardRemove())


def cancel(bot, update):
    """
    User cancelation function.
    Cancel conersation by user.
    """
    user = update.message.from_user
    logger.info("User {} canceled the conversation.".format(user.first_name))
    update.message.reply_text(goodbye[LANG],
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """
    Main function.
    This function handles the conversation flow by setting
    states on each step of the flow. Each state has its own
    handler for the interaction with the user.
    """
    global LANG
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SET_LANG: [RegexHandler('^(IND|EN)$', set_lang)],

            MENU: [CommandHandler('menu', menu),CommandHandler('start', start)],

            SET_STAT: [RegexHandler(
                        '^({}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{})$'.format(
                            about_vio['IND'],view_about['IND'],
                            view_vio['IND'], view_product['IND'],
                            view_faq['IND'],view_help['IND'], vio_map['IND'],
                            vio_waterlvl['IND'],vio_dcim['IND'],
                            vio_sketch['IND'], vio_sketch1['IND'],
                            vio_sketch2['IND'],vio_sketch3['IND'],
                            vio_sketch4['IND'],vio_temp['IND'],
                            vio_temp1['IND'],vio_temp2['IND'],
                            vio_temp3['IND'],vio_temp4['IND']),
                        set_state),
                       RegexHandler(
                        '^({}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{})$'.format(
                            about_vio['EN'], view_about['EN'],
                            view_vio['EN'], view_product['EN'],
                            view_faq['EN'],view_help['EN'], vio_map['EN'],
                            vio_waterlvl['EN'],vio_dcim['EN'],
                            vio_sketch['EN'],vio_sketch1['EN'],
                            vio_sketch2['EN'],vio_sketch3['EN'],
                            vio_sketch4['EN'],vio_temp['EN'],
                            vio_temp1['EN'],vio_temp2['EN'],
                            vio_temp3['EN'],vio_temp4['EN']),
                        set_state)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('menu', menu)]
        },

        fallbacks=[CommandHandler('cancel', cancel),
                   CommandHandler('help', help)]
    )

    dp.add_handler(conv_handler)

    # Log all errors:
    dp.add_error_handler(error)

    # Start DisAtBot:
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process
    # receives SIGINT, SIGTERM or SIGABRT:
    updater.idle()


if __name__ == '__main__':
    main()
