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


class _Embed:
    __slots__ = ("_data", "title", "description", "url", "color", "timestamp", "author", "fields", "image", "thumbnail")

    def __init__(self, data: dict):
        self._data = data
        self.title: Optional[str] = data.get("title")
        self.description: Optional[str] = data.get("description")
        self.url: Optional[str] = data.get("url")
        self.color: Optional[int] = data.get("color")
        self.timestamp: Optional[str] = data.get("timestamp")
        self.author: _EmbedAuthor = _EmbedAuthor(data.get("author", {}))
        self.fields: Union[list, list[_EmbedField]] = list(map(_EmbedField, data.get("fields", [])))
        self.image: _EmbedImage = _EmbedImage(data.get("image", {}))
        self.thumbnail: _EmbedImage = _EmbedImage(data.get("thumbnail", {}))


class _Message:
    __slots__ = ("_data", "content", "embeds")

    def __init__(self, data: dict):
        self._data = data
        self.content: Optional[str] = data.get("content")
        self.embeds: Union[list, list[_Embed]] = list(map(_Embed, data.get("embeds", [])))


def json_to_embed(data: Union[str, dict]) -> _Message:
    if isinstance(data, str):
        data = loads(data)
    return _Message(data)
