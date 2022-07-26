# SDGUI
Simple Docker GUI

Для использования необходимо включить API Вашего Docker, для этого:

1. Отредактируйте файл /lib/systemd/system/docker.service
2. Заменив параметр ExecStart следуюшей строкой: ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 $DOCKER_OPTS
3. Перезагрузить сервис Вашего Docker, выполнив команды:
- systemctl daemon-reload
- service docker restart

ВАЖНО: все работающие контейнеры будут перезапущены!

Пример работы SDGUI, отображение контейнеров (аналог консольной команды: docker ps -a), с функциональными возможностями
![image](https://user-images.githubusercontent.com/95647455/181085261-c883b282-6e07-416e-baa0-38019b91def7.png)

Пример работы, отображение образов (аналог консольной команды: docker images), с возможностью удаления образа
![image](https://user-images.githubusercontent.com/95647455/181086025-54cb7161-1a61-4b61-a396-e54487841820.png)
