# Bot for tracking the status of validators HAQQ #

Порядок установки:
Installation instructions:

```
cd
https://github.com/ivangrapher/telebot
nano /$USER/telebot/main.py
```

ставить свой телеграм токен
put your telegram token

```
bot = telebot.TeleBot("TOKEN")
```

Запустить бота в tmux или screen
Run bot in tmux or screen

```
python3 main.py
```

## Бот посылающий уведомление валидатора HAQQ <br>
Бот работает в 2 потока <br>
### 1 поток:
  `/add valoper_address` - добавление валопера для мониторинга (валидатор и id пользователя добавляются в файл text.txt).
  Один пользователь может добавить до трех валидаторов <br>
  `/my` - список моих валидаторов <br>
  `/info` - вывод информации по моим валидатороам <br>
  `/del` - удаление всех валидаторов <br>
### 2 поток:
  На втором потоке каждые 10 минут срабатывает функция sending. Функция sending с помощью функции provval() в файле proverka.py проверяет все валидаторы в файле text.txt. Если валидатор в тюрьме, то посылает пользователю этого валидатора сообщение о том, что его валидатор попал в тюрьму.
  
## Notification bot HAQQ
The bot works in 2 threads
### 1 stream:
   `/add valoper_address` - adding a valoper for monitoring (validator and user id are added to text.txt file).
   One user can add up to three validators <br>
   `/my` - list of my validators <br>
   `/info` - display information about my validators <br>
   `/del` - delete all validators <br>
### 2 stream:
   On the second thread, the sending function is fired every 10 minutes. The sending function uses the provval() function in the proverka.py file to check all the validators in the text.txt file. If the validator is in jail, sends a message to the user of that validator that their validator is in jail.
   
  Ссылка на рабочий бот:  <br>
  Link to working bot:  <br>
   https://t.me/ayta_haqq_bot
Пример работы:
Work example:
![image](https://user-images.githubusercontent.com/103099590/195658414-ac1bfe16-e739-417e-8169-a70a51e434a5.png)

