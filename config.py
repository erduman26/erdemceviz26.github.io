import os # işletim sistem kaynaklarına erişim modülü
class Config(object):
    # gizli anahtar oluşturma
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Adashbah-asd342-4324s'