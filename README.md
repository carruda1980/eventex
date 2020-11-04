# Eventex - Sua agenda de eventos online

##Como desenvolver?
1. Clone o repositório.
2. Crie um virtualenv com Python 3.6.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instância com o .env
6. Execute os testes.

<code>
git clone https://github.com/caugustoarruda/eventex.git wttd
cd wttd
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements
cp contribu/env-sample .env
python manage.py test
</code>

##Como fazer o deploy?
1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a inst1ãncia.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código par o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
```

