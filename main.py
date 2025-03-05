from json import loads
from typing import Optional, Union


class _EmbedField:
    __slots__ = ("name", "value", "inline")

    def __init__(self, data: dict):
        self.name = data.get("name")
        self.value = data.get("value")
        self.inline = data.get("inline", False)


class _EmbedAuthor:
    __slots__ = ("name", "url", "icon_url")

    def __init__(self, data: dict):
        self.name: Optional[str] = data.get("name")
        self.url: Optional[str] = data.get("url")
        self.icon_url: Optional[str] = data.get("icon_url")


class _EmbedFooter:
    __slots__ = ("text", "icon_url")

    def __init__(self, data: dict):
        self.text: Optional[str] = data.get("text")
        self.icon_url: Optional[str] = data.get("icon_url")


class _EmbedImage:
    __slots__ = ("url")

    def __init__(self, data: dict):
        self.url: Optional[str] = data.get("url")

    def __str__(self):
        return self.url


class _Embed:
    __slots__ = ("_data", "title", "description", "url", "color", "timestamp")

    def __init__(self, data: dict):
        self._data = data
        self.title: Optional[str] = data.get("title")
        self.description: Optional[str] = data.get("description")
        self.url: Optional[str] = data.get("url")
        self.color: Optional[int] = data.get("color")
        self.timestamp: Optional[str] = data.get("timestamp")

    @property
    def author(self) -> Optional[_EmbedAuthor]:
        if self._data.get("author"):
            return _EmbedAuthor(self._data["author"])
        return None

    @property
    def fields(self) -> Optional[list[_EmbedField]]:
        if self._data.get("fields"):
            return list(map(_EmbedField, self._data["fields"]))
        return None

    @property
    def image(self) -> Optional[_EmbedImage]:
        if self._data.get("image"):
            return _EmbedImage(self._data["fields"])
        return None

    @property
    def thumbnail(self) -> Optional[_EmbedImage]:
        if self._data.get("thumbnail"):
            return _EmbedImage(self._data["fields"])
        return None


class _Message:
    __slots__ = ("_data", "content")

    def __init__(self, data: dict):
        self._data = data
        self.content: Optional[str] = data.get("content")

    @property
    def embeds(self) -> Optional[list[_Embed]]:
        if self._data.get("embeds"):
            return list(map(_Embed, self._data.get("embeds", [])))
        return None


def json_to_message(data: Union[str, dict]) -> _Message:
    if isinstance(data, str):
        data = loads(data)
    return _Message(data)
