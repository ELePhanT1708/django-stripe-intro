# django-stripe-intro
Привет , работодатель ! 
Я разобрался как интегрировать stripe payments to your project.

(Если есть докер десктоп) 

После клонирования моего репозитория нужно:
1. Запустить Docker Desktop

2. docker-compose up --build (in 'tutorial' directory)

И ищем сайт по http://localhost:8000/items/


(Если нет докера) После клонирования моего репозитория нужно:
1. Сделать виртуальное окружение у себя


- python -m venv test_env ( в корне клонированного репозитория)


- .\test_env\Scripts\Activate.ps1 (активируем окружение ) 


- pip install -r .\requirements.txt (устанавливаем необходимые зависимости) 


- py .\tutorial\manage.py runserver (запускаем сервер )

http://localhost:8000/items/
и мы увидим список существующих товаров доступных для покупки .  
по кнопке Buy now вы перейдете на формочку stripe для оплаты.

