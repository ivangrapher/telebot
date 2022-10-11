Порядок установки:


Бот посылающий уведомление
Бот работает в 2 потока
1 поток:
  - /add <valoper> - добавление валопера для мониторинга
  - /my - список моих валидаторов
  - /info - вывод информации по моим валидатороам
  - /del - удаление всех валидаторов
2 поток:
  Каждые 10 минут проверяет списки валидаторов и, если валидатор попал в тюрьму отправляет уведомление владельцу валидатора
  
Notification bot
The bot works in 2 threads
1 stream:
   - /add <valoper> - adding a valoper for monitoring
   - /my - list of my validators
   - /info - display information about my validators
   - /del - delete all validators
2 stream:
   Every 10 minutes checks the lists of validators and if the validator is jailed sends a notification to the owner of the validator
