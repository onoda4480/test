from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = 'h5xrNUzyIFGzbm0hFYO3HL8RWWgQcb81i2j28TYgROUlSon6DmiZ9dZ94q1iGJ08RUOc2Yo7UWhCR1hn3bPXxnCAo5p/U4Ol3x9QCDAWFvVit5xzeArFn5OhT+Z6oVDTwVW3JeqvDv6tRmI+o5kuTQdB04t89/1O/w1cDnyilFU=' #ここに自分のトークンを入れて下さい

USER_ID = ' U3d4c04d1ad2dfc143e72deb51d046b57' #ここに自分のユーザーIDを入れて下さい

def send_message(text):
  line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

  try:
      line_bot_api.push_message(USER_ID, TextSendMessage(text=text))
  except LineBotApiError as e:
    print(e.message)

if __name__ == "__main__":
  text = "テストメッセージ" #好きな文章でOKです
  send_message(text)