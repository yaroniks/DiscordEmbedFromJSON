# DiscordEmbedFromJSON
Библиотека, позволяющая преобразовать JSON в класс Embed.

Установка:
```bash
git clone https://github.com/yaroniks/DiscordEmbedFromJSON.git
cd DiscordEmbedFromJSON
pip install -r requirements.txt
```

Пример использования:
```python
import DiscordEmbedFromJSON as dsjson

message = dsjson.json_to_message("""{
  "content": null,
  "embeds": [
    {
      "title": "2",
      "description": "3",
      "color": null,
      "fields": [
        {
          "name": "4",
          "value": "5"
        }
      ],
      "author": {
        "name": "1"
      },
      "footer": {
        "text": "6"
      }
    }
  ],
  "attachments": []
}""")

embed = message.embeds[0]

print(message.content, embed.title, embed.author.name, 
      embed.image, embed.description, embed.fields[0].value)
```