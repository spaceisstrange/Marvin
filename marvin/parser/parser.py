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

import json
from marvin.model.action import Action
from marvin.model.send_item import SendItem
from marvin.model.reply import Reply
from marvin.model.image_item import ImageItem
from marvin.model.text_item import TextItem


class Parser:
    """
    Given JSON data, parses it to turn it into actions that the bot should execute.
    """

    @staticmethod
    def get_actions(json_file) -> []:
        """
        Makes a list of actions out of the parsed JSON data.
        
        Args:
            json_file (file): The JSON data that we want to parse.
        
        Returns:
            The parsed list of actions.
        """
        json_data = json.load(json_file)
        actions = []

        for action in json_data:
            name = action["name"]
            send_items = []
            replies = []

            for send_item in action["send"]:
                send_items.append(Parser.get_item_from_json(send_item))

            try:
                reply_list = action["replies"]
            except:
                reply_list = []

            for reply in reply_list:
                text = reply["text"]
                do = reply["do"]
                replies.append(Reply(text, do))

            actions.append(Action(name, send_items, replies))

        return actions

    @staticmethod
    def get_item_from_json(item) -> SendItem:
        """
        Returns an specific SendItem from the type specified in the JSON data.
        
        Args:
            item (json): JSON from which we'll take our data.
            
        Returns:
            The specific SendItem.
            
        Raises:
            SyntaxError: If the type of the item is unknown.
        """
        item_type = item["type"]
        data = item["data"]

        if item_type == 'image':
            try:
                caption = item['caption']
            except:
                caption = None

            return ImageItem(data, caption)
        elif item_type == 'text':
            return TextItem(data)

        raise SyntaxError('Unknown item \'' + item_type + '\'')
