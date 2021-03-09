# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['GetUserDict']

from typing import Dict, Union
from pyrogram.types import User
from userge.utils.functions import mention_html, AttributeDict
from ...ext import RawClient


class GetUserDict(RawClient):  # pylint: disable=missing-class-docstring
    async def get_user_dict(self, user_id: Union[int, str, User], attr_dict: bool = False) -> Union[Dict[str, str], AttributeDict]:
        """This will return user `Dict` which contains
        `id`(chat id), `fname`(first name), `lname`(last name),
        `flname`(full name), `uname`(username) and `mention`.
        """
        if isinstance(user_id, User):
            user_obj = user_id
        else:
            user_obj = await self.get_users(user_id)
        fname = (user_obj.first_name or '').strip()
        lname = (user_obj.last_name or '').strip()
        username = (user_obj.username or '').strip()
        if fname and lname:
            full_name = fname + ' ' + lname
        elif fname or lname:
            full_name = fname or lname
        else:
            full_name = "user"
        mention = mention_html(user_obj.id, username or full_name)
        out = {'id': user_obj.id, 'fname': fname, 'lname': lname,
                'flname': full_name, 'uname': username, 'mention': mention}
        return AttributeDict(out) if attr_dict else out
