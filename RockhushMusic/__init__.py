from RockhushMusic.core.bot import Rocky
from RockhushMusic.core.dir import dirr
from RockhushMusic.core.git import git
from RockhushMusic.core.userbot import Userbot
from RockhushMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Rocky()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
