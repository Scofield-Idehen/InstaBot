from instabot import Bot 

my_bot = Bot()
#login your bot  account 

my_bot.login(username=" ", password=" ")

#follow a user

my_bot.follow("name of person")

#follow many users
my_bot.follow_users(["user", "user","user"])

#unfollow the non followers
my_bot.unfollow_non_followers()

#upload an image 
my_bot.upload_photo("image.jpg", caption= "my first instagram bot and i am testing it")

#send message
my_bot.send_message("hello friend, i am a bot and i am trying to breath", "username")

#like a post
my_bot.like_user("username", amount=5, filtration=False)

#comment
#first we must get the user_ID of the user and from the username 
# then we get media of the user through their ID
# Then we get the media and comment under it 
user_id = my_bot.get_user_id_from_username("username")
#count 
media_id = my_bot.get_last_user_medias(user_id, 1)
my_bot.comment(media_id[0], "this is cool keep it up")


#get followers 

followers_list = my_bot.get_user_followers("name")

#get following of user 

following_list = my_bot.get_user_following("user")

for each_f in followers_list:
    print(my_bot.get_username_from_user_id(each_f))

for each_person in following_list:
    print(my_bot.get_username_from_user_id(each_person))

my_bot.logout()
