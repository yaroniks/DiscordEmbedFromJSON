# DiscordEmbedFromJSON
Библиотека, которая парсит JSON дискорд вебхука.

Установка:
```bash
git clone https://github.com/yaroniks/DiscordEmbedFromJSON.git
```

Пример использования:
```python
import DiscordEmbedFromJSON as dsjson

message = dsjson.json_to_message("""{
  "content": "1",
  "embeds": [
    {
      "title": "3",
      "description": "4",
      "color": null,
      "fields": [
        {
          "name": "5",
          "value": "6"
        }
      ],
      "author": {
        "name": "2"
      },
      "footer": {
        "text": "7"
      }
    }
  ],
  "attachments": []
}""")

embed = message.embeds[0]

print(message.content, embed.title, embed.author.name, embed.image, embed.description, embed.fields[0].value)
```

Получить JSON сообщения можно с помощью [Discohook](https://discohook.org/)
