# Bot for tracking the status of validators HAQQ #

Порядок установки:  <br>
Installation instructions:

```
cd
git clone https://github.com/ivangrapher/telebot
```

Открыть файл tkn.py и ставить свой телеграм токен вместо TOKEN <br>
Open the tkn.py file and put your telegram token instead of TOKEN <br>

```
nano /$USER/telebot/tkn.py
```

Открыть файл users.txt и поставить свой user_id <br>
Open users.txt file and put your user_id <br>

Запустить бота в tmux или screen <br>
Run bot in tmux or screen <br>

```
python3 main.py
```

## Бот посылающий уведомление валидатора HAQQ <br>
Бот работает в 2 потока <br>
### 1 поток:
  `/add valoper_address` - добавление валопера для мониторинга (валидатор и id пользователя добавляются в файл text.txt).
  Один пользователь может добавить до трех валидаторов <br>
  `/my` - список моих валидаторов <br>
  `/allproposal` - вывод всех proposals <br>
  `/info` - вывод информации по моим валидатороам <br>
  `/del` - удаление всех валидаторов <br>
### 2 поток:
  На втором потоке каждые 10 минут срабатывает функция sending. Функция sending с помощью функции provval() в файле proverka.py проверяет все валидаторы в файле text.txt. Если валидатор в тюрьме, то посылает пользователю этого валидатора сообщение о том, что его валидатор попал в тюрьму.
  И срабатывает функция proverka.newproposal(), которая тоже каждые 10 минут проверяет новые пропозалы. Если обнаружит, что имеется новый пропозал, то всем пользователям отправляет сообщение о новом пропозале.
  
## Notification bot HAQQ
The bot works in 2 threads
### 1 stream:
   `/add valoper_address` - adding a valoper for monitoring (validator and user id are added to text.txt file).
   One user can add up to three validators <br>
   `/my` - list of my validators <br>
   `/allproposal` - output of all proposals <br>
   `/info` - display information about my validators <br>
   `/del` - delete all validators <br>
### 2 stream:
   On the second thread, the sending function is fired every 10 minutes. The sending function uses the provval() function in the proverka.py file to check all the validators in the text.txt file. If the validator is in jail, sends a message to the user of that validator that their validator is in jail.
   And the proverka.newproposal() function is triggered, which also checks new proposals every 10 minutes. If it detects that there is a new proposal, it sends a message to all users about the new proposal.
   
  Ссылка на рабочий бот:  <br>
  Link to working bot:  <br>
   https://t.me/ayta_haqq_bot
Пример работы:
Work example:
![image](https://user-images.githubusercontent.com/103099590/195658414-ac1bfe16-e739-417e-8169-a70a51e434a5.png)

