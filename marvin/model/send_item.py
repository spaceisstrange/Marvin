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


class SendItem(object):
    """
    Defines a general item that can be sent to the user. This should be inherited by an specific class
    like a Photo or a Text item.
    """

    def send(self) -> None:
        """
        Sends whatever item this is to the user. SHOULD be implemented by the subclass.
        """
        raise NotImplementedError("Please, implement this method by inheriting this class.")