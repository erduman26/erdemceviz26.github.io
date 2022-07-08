from flask import Flask,render_template,request
from blog import BlogYazi
from config import Config
from database import Database

app=Flask(__name__)
app.config.from_object(Config) # CRSF

def icerikDoldur():
    yaziListe=[]
    yazi1=BlogYazi()
    yazi1.baslik="Merhaba Blog Sayfama Hoşgeldin"
    yazi1.baslikresim="sample.jpg"
    yazi1.yayinicerik="Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur.Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek."
    yazi1.yayintarihi="01.01.2022"
    yazi1.yazarIsim="Erdem Ceviz".upper()
    yazi1.yazikisaicerik=yazi1.yayinicerik[0:9000]+""

    yazi2=BlogYazi()
    yazi2.baslik="Flask Nedir?"
    yazi2.baslikresim="y3.jpg"
    yazi2.yayinicerik="Flask bir python frameworküdür. Bilindiği üzere python hızlıca birşeyler yapmak belli sonuçları zamandan kazanarak ortaya çıkarmak için hayat kurtaran bir dildir. Web servislerinde de hızlı sonuç elde etmek için pythonun flask frameworkünden yararlanlabirilir. Flask hem çabuk öğrenilebilen hemde bencmarklarına bakıldığında performansı gayet yüksek bir frameworktür.Günümüzde birçok programlama dili ile web programlama yapılabiliyor. Ben size bu yazımda web programlama için kullanabileceğiniz python dilinin Flask web framework’ünü anlatmaya çalışacağım.Flask, yukarıda bahsettiğim gibi python dilinin bir web framework’üdür. Framework diye bahsediyoruz ama belki bilmeyenler olabilir, kısaca framework nedir onu anlatalım."
    yazi2.yayintarihi="01.01.2022"
    yazi2.yazarIsim="Erdem Ceviz".upper()
    yazi2.yazikisaicerik=yazi2.yayinicerik[0:9000]+""

    yazi3=BlogYazi()
    yazi3.baslik="Python Nedir?"
    yazi3.baslikresim="y2.jpg"
    yazi3.yayinicerik="Günümüzde birçok programlama dili ile web programlama yapılabiliyor. Ben size bu yazımda web programlama için kullanabileceğiniz python dilinin Flask web framework’ünü anlatmaya çalışacağım.Flask, yukarıda bahsettiğim gibi python dilinin bir web framework’üdür. Framework diye bahsediyoruz ama belki bilmeyenler olabilir, kısaca framework nedir onu anlatalım."
    yazi3.yayintarihi="01.01.2022"
    yazi3.yazarIsim="Erdem Ceviz".upper()
    yazi3.yazikisaicerik=yazi3.yayinicerik[0:9990]+""

    yaziListe.append(yazi1)
    yaziListe.append(yazi2)
    yaziListe.append(yazi3)
    yaziListe.append(yazi3)
    yaziListe.append(yazi3)
    yaziListe.append(yazi3)

    return yaziListe

@app.route("/")
def anasayfa():
    yazilar = icerikDoldur()
    return render_template("index.html",sayfabasligi="Anasayfa",yaziListe = yazilar)

@app.route("/iletisim")
def iletisim():
    ben={}
    ben["ad"]="Erdem"
    ben["soyad"]="Ceviz"
    ben["tel"]="05556556666"
    return render_template("iletisim.html",sayfabasligi="İletişim",kisi=ben)

@app.route("/hakkinda")
def hakkinda():
    return render_template("hakkinda.html",sayfabasligi="Hakkinda")

@app.route("/girisyap",methods=['POST', 'GET'])
def girisyap():
    if request.method == 'POST':
        isim = request.form.get('kadi') 
        sifre = request.form.get('sifre')

        if isim =="Erduman26" and sifre=="7mrs3v3b":
            return render_template("adminanasayfa.html")
        else:
            return render_template("girisyap.html",sayfabasligi="Giriş Yap",error="Giriş Başarısız")
    else:
        return render_template("girisyap.html",sayfabasligi="Giriş Yap")

@app.route("/yeniyaziekle")
def yeniyaziekle():
    return render_template("yaziekle.html",sayfabasligi="Yeni Yazı Ekle")

@app.route("/bilgilerim")
def bilgilerim():
    if request.method != "POST":
        BilgilerSinifi = Database.startCon().classes.bilgiler
        u1 = Database.loadSession().query(BilgilerSinifi).first()
        return render_template("bilgilerim.html",sayfabasligi="Bilgilerim",bilgiler=u1)

@app.route("/hakkindaduzenle")
def hakkindaduzenle():
    if request.method != "POST":
        BilgilerSinifi = Database.startCon().classes.bilgiler
        u1 = Database.loadSession().query(BilgilerSinifi).first()
        return render_template("hakkindaduzenle.html",sayfabasligi="Hakkında",hakkinda=u1.hakkinda)


if __name__ == "__main__":
    app.run(debug=True)

#py -m pip install flask