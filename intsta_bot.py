from instabot import Bot
bot=Bot()
bot.login(username="preferential_brown", password="Saurabh1100")
# bot.follow("narendramodi")
# bot.upload_photo("path")
# bot.get_user_id_from_username("narendramodi")
# bot.send_message("hello ji", ["user1", "user2"])
# followers=bot.get_user_followers("preferential_brown")
# for follower in followers:
#     print(bot.get_user_info(follower))
following=bot.get_user_following("preferential_brown")
for Following in following:
    print(bot.get_user_info(Following))
