Para executar a aplicação é necessário instalar o django e algumas bibliotecas utilizadas no projeto
pip install django-crispy-forms
pip install django-import-export

Após instalar as dependências, comando para executar dentro da pasta principal:

python manage.py runserver

Abrir no navegador o endereço:
localhost:8000 - acessa a página principal que é a lista de pagamentos cadastrados podendo adicionar um novo, 
alterar ou deletar um existente.

localhost:8000/upload - acessa a página para fazer o upload de um arquivo xlsx