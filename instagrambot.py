from instapy import InstaPy #You need to ''' pip install instapy''' in your terminal before running this code in a virtual environment to ensure the library is downloaded to your system.

insta = InstaPy(username='123abc', password='123abc', headless_browser=True) #You can remove the headless browser declaration if you attach a GUI to this program as I did before for a similar project however for this version, there is no GUI attached so this declaration saves GPU space and is faster.
insta.like_by_tags(["supercar", "lamborghini","apple","rap","money", "cool"], amount=5) # arguments adjustable based on specific needs
insta.set_dont_like(["naked", "nsfw"])# arguments adjustable based on specific needs
insta.set_do_follow(True, percentage=50)# arguments adjustable based on specific needs
insta.set_do_comment(True, percentage=50)# arguments adjustable based on specific needs
insta.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:","That's Great!", "Wow!", "That is awesome!"])# arguments adjustable based on specific needs
insta.set_quota_supervisor(enabled=True, peak_comments_daily=350, peak_comments_hourly=20)#Allows us to limit our automated activity on Instagram to not get our bot blocked.
insta.set_use_clarifai(enabled=True, api_key='<insert key here>') #section where the ClarifAI is integrated into the program
insta.clarifai_check_img_for(['nsfw'])# arguments adjustable based on specific needs
insta.set_relationship_bounds(enabled=True, max_followers=5000) #allows us to only target smaller account who are more likely to follow and engage with users back
insta.end()
