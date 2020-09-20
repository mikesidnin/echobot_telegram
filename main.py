import random
import phrase_pack
import config
import sticker_pack
import telebot

from telebot.types import Message


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def sticker (message: Message):

    input_message = str(message.text)

    reply_curse_length = len(phrase_pack.reply_curse) - 1
    random_curse = random.randint(0, reply_curse_length)

    reply_question_length = len(phrase_pack.reply_question) - 1
    random_question = random.randint(0, reply_question_length)

    check_curse = any(i in input_message for i in phrase_pack.ref_curse)
    check_question = any(i in input_message for i in phrase_pack.ref_question)

    if check_curse:
        bot.reply_to(message, phrase_pack.reply_curse[random_curse])

    if check_question:
        bot.reply_to(message, phrase_pack.reply_question[random_question])


    sticker_chance = random.random() * 100

    sticker_length = len(sticker_pack.sticker_pack) - 1
    random_sticker = random.randint(0, sticker_length)

    if sticker_chance >= 95:
        bot.send_sticker(message.chat.id, sticker_pack.sticker_pack[random_sticker])

    reply_chance = random.random() * 100
    reply_other_length = len(phrase_pack.reply_other) - 1
    random_reply = random.randint(0, reply_other_length)

    if reply_chance >= 95:
        bot.send_message(message.chat.id, phrase_pack.reply_other[random_reply])

@bot.message_handler(content_types=['sticker'])
def reply (message: Message):

    sticker_part_1 = ''
    sticker_part_2 = ''

    input_sticker = str(message.sticker)

    for x in range(13, 28):
        sticker_part_1 = sticker_part_1 + input_sticker[x]
        x += 1

    for y in range(70, 83):
        sticker_part_2 = sticker_part_2 + input_sticker[y]
        y += 1

    positive_reply_length = len(phrase_pack.reply_positive) - 1
    random_positive_reply = random.randint(0, positive_reply_length)

    ref_sticker_part_2_length = len(config.ref_sticker_part_2) - 1
    is_positive = 0

    for i in range(0, ref_sticker_part_2_length):
        if sticker_part_1 == config.ref_sticker_part_1 and sticker_part_2 == config.ref_sticker_part_2[i]:
            bot.reply_to(message, phrase_pack.reply_positive[random_positive_reply])
            is_positive = 1

    if is_positive != 1:

        prob_reply = random.random() * 100

        if prob_reply > 80:

            number_replies = len(phrase_pack.reply_negative) - 1

            ran_int = [0] * (number_replies + 1)
            max_index = 0

            for number_rand in range(999):

                nn = random.randint(0, number_replies)

                for i in range(0, number_replies):
                    if nn == i:
                        ran_int[i] = ran_int[i] + 1


            for i in range(0, number_replies):
                if ran_int[i] > ran_int[max_index]:
                    max_index = i

            bot.reply_to(message, phrase_pack.reply_negative[max_index])

        else:
            reply_neg2_len = len(phrase_pack.reply_negative2) - 1

            which_reply_neg2 = random.randint(0, reply_neg2_len)
            bot.send_message(message.chat.id, phrase_pack.reply_negative2[which_reply_neg2])

bot.polling()