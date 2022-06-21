import asyncio
import logging
import time


# async def say_hello(name):
#     await asyncio.sleep(5)
#     logging.info(f"hello {name}")


# # async def say_hello_list_test(list_name):
# #     for name in list_name:
# #         await asyncio.sleep(5)
# #         logging.info(f"hello {name}")


# async def say_hello_list(list_name):
#     logging.info(f"start main event loop")
#     await asyncio.gather(say_hello(list_name[0]), say_hello(list_name[1]))
#     # for name in list_name:
#     #     await say_hello(name)
#     logging.info(f"end main event loop")

# coroutine
async def kamtar_amateur_player(name):
    logging.info(f"player {name} start")
    for i in range(4):
        logging.info(f"{name} played!")
        time.sleep(1)
        logging.info(f"Hero played!")
        await asyncio.sleep(2)


async def amateur_player(name):
    logging.info(f"player {name} start")
    for i in range(4):
        logging.info(f"{name} played!")
        time.sleep(1)
        logging.info(f"Hero played!")
        await asyncio.sleep(4)


async def chess_champion(players):
    # players = ["ashkan", "zahra", "arian", "afshin", "tohid", "mehrdad"]

    # t_1 = asyncio.create_task(amateur_player("ashkan"))
    # t_2 = asyncio.create_task(amateur_player("asghar"))
    # await t_1
    # await t_2
    tasks = []
    for name in players:
        if name == "zahra":
            tasks.append(asyncio.create_task(kamtar_amateur_player(name)))
            continue
        tasks.append(asyncio.create_task(amateur_player(name)))
    
    for task in tasks:
        await task


    print(tasks[0].done())
    # print(tasks)
    # await asyncio.gather(amateur_player(players[0]), amateur_player(players[1]), amateur_player(players[2]), amateur_player(players[3]), amateur_player(players[4]), amateur_player(players[5]))

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main: before creating asyn/await")
    asyncio.run(chess_champion(
        ["ashkan", "zahra", "arian", "afshin", "tohid", "mehrdad"]))