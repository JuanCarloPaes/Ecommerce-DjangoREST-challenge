# Ecommerce-DjangoREST-challenge

Use os comandos seguintes para instalar a API // Use the following commands to install the API
 
python -m venv venv
cd ecommerce
venv/Scripts/Activate.ps1
pip install -r requirements.txt

* Faça um arquivo chamado ".env" dentro da pasta "eshop", em seguida coloque o seguinte script
* Make a file called ".env" inside the "eshop" folder, then put the following script

      # SECURITY WARNING: keep the secret key used in production secret!
      SECRET_KEY = (your django secret key)
      
      # SECURITY WARNING: don't run with debug turned on in production!
      DEBUG = True
      
      #Database name variable (foi usado o postgrsql como database // it was used the postgresql for database)
      DATABASE_NAME = (o nome do seu banco de dados // your database name)
      DATABASE_USER = (o usuario do seu banco de dados // your database user)
      DATABASE_PASSWORD = (a senha do seu banco de dados // your database password)
      DATABASE_HOST = (o host do seu banco de dados // your database host)
      DATABASE_PORT = (o port do seu banco de dados // your database port)
      
      AWS_ACCESS_KEY_ID = (a chave de acesso do seu AWS S3// your S3 AWS access key)
      AWS_SECRET_ACCESS_KEY = (sua chave secreta do AWS S3 // your AWS S3 secret key)
      AWS_STORAGE_BUCKET_NAME = (o nome do seu bucket AWS S3 // your AWS S3 bucket's name)
      AWS_S3_REGION_NAME =  (a regiao do seu bucket AWS S3 // the region your AWS S3 bucket is)
      
      EMAIL_HOST = 'smtp.mailtrap.io'
      EMAIL_HOST_USER = (seu host user pro mailtrap.io // your host user code for mailtrap.io)
      EMAIL_HOST_PASSWORD = (sua senha do email host pro mailtrap.io // your host password for mailtrap.io)
      EMAIL_PORT = (seu email port pro mailtrap.io // your email port for mailtrap.io)
      
      STRIPE_PUBLIC_KEY = (sua chave publica do stripe // your stripe public key)
      STRIPE_SECRET_KEY = (sua chave secreta do stripe // your stripe secret key)
      
      
      STRIPE_WEBHOOK_SECRET =  (sua chave secreta do stripe webhook//your stripe webhook secret key)

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
  
