from var import Var
from firebot.Configs import Config
from firebot.utils import fire_on_cmd

issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "2.0"
if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"✘ SHOWING Iwang-Bot STATS ✘\n"
    f"VERSION = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {amiusingsudo} \n"
    f"LOG-CHAT = {logchat} \n"
    f"HEROKU = {riplife} \n"
    f"G-DRIVE = {wearenoob}"
)
