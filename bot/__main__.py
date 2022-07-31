import time
import asyncio
import config

from aiogram import Bot, Dispatcher, executor
from loguru import logger

from start_script import start_script
from config import SINGLE_START, TIME_TO_SLEEP
from tools import prepare_temp_folder
from last_id import check_data, write_data, read_data

logger.add(
    "./logs/debug.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="1 week",
    compression="zip",
)

logger.info("Script is started.")


bot = Bot(config.TG_BOT_TOKEN)
links_data = 'links_data.pickle'
links = dict()
# {
#     'pmpu_news': 0,
#     'sspmpu': 0
# }


@logger.catch
async def background_on_start():
    global bot
    global links
    global links_data

    d = dict()
    links = check_data(d, links_data)

    while True:
        print('new iter')
        links = read_data(links_data)

        await start_script(bot, links)

        write_data(links, links_data)
        prepare_temp_folder()

        await asyncio.sleep(15)


async def on_bot_start_up(dispatcher: Dispatcher):
    asyncio.create_task(background_on_start())


async def add_link(msg):
    print(msg)
    link = msg.get_args().split('/')[-1]

    if link in links:
        await msg.answer('Такая группа уже существует')
    else:
        links[link] = 0
        await msg.answer('Группа добавлена')

    write_data(links, links_data)


async def del_link(msg):
    print(msg)
    link = msg.get_args().split('/')[-1]

    if link in links:
        del links[link]
        await msg.answer('Группа удалена')
    else:
        await msg.answer('Нет такой группы')

    write_data(links, links_data)


async def show_links(msg):
    print(msg)
    await msg.answer('Список групп:\n' + '\n'.join(links))


def create_bot_factory():
    dp = Dispatcher(bot)

    dp.register_message_handler(
        add_link,
        commands='add'
    )

    dp.register_message_handler(
        del_link,
        commands='del'
    )

    dp.register_message_handler(
        show_links,
        commands='show'
    )

    #await dp.start_polling()
    executor.start_polling(dp, skip_updates=True, on_startup=on_bot_start_up)



if __name__ == '__main__':
    # asyncio.run(create_bot_factory())
    create_bot_factory()