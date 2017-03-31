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


class TextItem(SendItem):
    """
    Defines a text item that simply holds its text.

    Attributes:
        text (str): The text that will be sent to the user.
    """

    def __init__(self, text) -> None:
        """
        Initializes the item with a text.
        """
        super().__init__()
        self.text = text

    def send(self) -> None:
        """
        Sends the data to the API.

        TODO: Complete.
        """
        pass
