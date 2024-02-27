from dex.core.bot import Mody
from dex.core.dir import dirr
from dex.core.git import git
from dex.core.userbot import Userbot
from dex.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Mody()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
