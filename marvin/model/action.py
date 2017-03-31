# Made with <3 by Fran González (@spaceisstrange)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>


class Action(object):
    """
    Defines an action that can be done by the bot, like sending a photo with text and expecting
    something as a reply from the user.
    
    Attributes:
        name (str): The name of the action itself so the user can refer to it later.
        send_items (:obj:`list` of :obj:`send_item`): List of things to send to the user, like text or a photo.
        replies (:obj:`list` of :obj:`send_item`): List of replies available for the user that will be presented as buttons.
    """

    def __init__(self, name, send_items, replies) -> None:
        """
        Initializes an action with its name, list of send items and list of replies (if any).
        """
        super().__init__()
        self.name = name
        self.send_items = send_items
        self.replies = replies

