# django-stripe-intro
Привет , работодатель ! 
Я разобрался как интегрировать stripe payments to your project.

(Если есть докер десктоп) 

После клонирования моего репозитория нужно:
запустить docker-compose.yml и проект соберется сам !! 
docker-compose up --build (in 'tutorial' directory)

И ищем сайт по http://localhost:8000/items/


(Если нет докера) После клонирования моего репозитория нужно:
1. venv with all dependencies in requirements.txt

будет запустить сервер и по  ти по ссылке 
http://localhost:8000/items/
и мы увидим список существующих товаров доступных для покупки .  
по кнопке Buy now вы перейдете на формочку stripe для оплаты.

