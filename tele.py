from telethon import TelegramClient

from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.functions.channels import GetParticipantsRequest

from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
api_id = 1135557
api_hash = 'b00c96e8406d2d404d353394cd90f05a'
phone = '+918299446752'

client = TelegramClient(phone, api_id, api_hash)
client.session.report_errors = False
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

channel = client(ResolveUsernameRequest('MY_CHANNEL')) # Your channel username

user = client(ResolveUsernameRequest('Username')) # Your channel admin username
admins = [InputUserSelf(), InputUser(user.users[0].id, user.users[0].access_hash)] # admins
admins = [] # No need admins for join and leave and invite filters

filter = None # All events
filter = ChannelAdminLogEventsFilter(True, False, False, False, True, True, True, True, True, True, True, True, True, True)
cont = 0
list = [0,100,200,300]
for num in list:
    result = client(GetParticipantsRequest(InputChannel(channel.chats[0].id, channel.chats[0].access_hash), filter, num, 100))
    for _user in result.users:
        print( str(_user.id) + ';' + str(_user.username) + ';' + str(_user.first_name) + ';' + str(_user.last_name) )
        with open(''.join(['users/', str(_user.id)]), 'w') as f: f.write(str(_user.id))
