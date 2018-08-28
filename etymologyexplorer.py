import os, time, logging
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
from instapy import InstaPy

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=os.environ['INSTA_USERNAME'],
                  password=os.environ['INSTA_PASSWORD'],
                  headless_browser=True,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
                 #potency_ratio=-1.21,
                  delimit_by_numbers=True,
                   max_followers=8500,
                    max_following=5555,
                     min_followers=45,
                      min_following=56)
    

    session.set_user_interact(amount=2, randomize=True, percentage=50, media='Photo')
    session.set_dont_like(['watch', 'god', 'God'])    
    session.like_by_tags(['etymology', 'wordgram', 'wordoftheday', 'wordfortheday' ,'funfact' ,'funfacts' ,'vocabulary' ,'learnvocabulary' ,'learnsomethingneweveryday' ,'becomesmartereveryday' ,'dictionarycom' ,'englishvocabulary' ,'etymologyrules' ,'language' ,'definition' ,'words' ,'dictionary' ,'unknownwords' ,'obscurewords' ,'languagelovers' ,'esoteric'], 
                         amount=10, interact=True)

    session.set_user_interact(amount=2, randomize=True, percentage=50, media='Photo')
    session.set_do_like(enabled=True, percentage=50)
    session.set_do_follow(enabled=False)
    session.interact_user_followers(['etymologynerd', 'dictionarycom', 'cambridgewords', 'oxforddictionaries', 'etymologyrules'], 
                                    amount=50, randomize=True)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp: 
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    logging.info("Ending session");
    session.end()


