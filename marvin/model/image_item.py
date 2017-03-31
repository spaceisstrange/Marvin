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

from marvin.model.send_item import SendItem


class ImageItem(SendItem):
    """
    Defines an image item that holds the URL of the image and its caption.
    
    Attributes:
        url (str): The URL in which the image is hosted and from which it'll be loaded by the Telegram API.
        caption (str): Text that will be sent as a caption of the image. Can be None.
    """

    def __init__(self, url, caption=None) -> None:
        """
        Initializes the item with the URL of the image and its caption (if any).
        """
        super().__init__()
        self.url = url
        self.caption = caption

    def send(self) -> None:
        """
        Sends the data to the API.
        
        TODO: Complete.
        """
        pass
