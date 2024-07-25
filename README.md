## Реализован функционал:

![img_2.png](img_2.png)

### Запуск тестов:

`pytest`

### Запуск докер контейнера:

`docker build -t myimage .`
`docker run -d --name mycontainer -p 80:80 myimage`
Или
`docker-compose build`
`docker-composee up`

### Автодополнение при вводе города (bootstrap из ранее введенных городов)

![img.png](img.png)
![img_1.png](img_1.png)

### Сохраняется история поиска для каждого пользователя. API, показывающее сколько раз вводили какой город

![img_3.png](img_3.png)
![img_4.png](img_4.png)
