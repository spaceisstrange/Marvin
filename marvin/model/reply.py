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


class Reply(object):
    """
    Defines a reply that the user can select.

    Attributes:
        text (str): The text that will be shown in the button.
        do (str): The name of the action that will be called when this button is pressed.
    """

    def __init__(self, text, do) -> None:
        """
        Initializes an item with its type and data.
        """
        super().__init__()
        self.text = text
        self.do = do

    def get_button(self):
        """
        Transforms the current reply into a button known by the bot API.

        :return: A button that can be sent through the bot API.
        """
