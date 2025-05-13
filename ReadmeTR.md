<div align="center">

  <img src="assets/logo.png" alt="logo" width="200" height="auto" />
  <h1>Notebook Tavsiye Chatbot'u</h1>
  
  <p>
    Türk Lirası bazında istediğiniz notebook'u sizler için bulan chatbot.
  </p>
<br />
</div>

<!-- Table of Contents -->
# :notebook_with_decorative_cover: İçerikler
- [Proje Hakkında](#star2-about-the-project)
  * [Ekran Görüntüleri](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Sunduklarımız](#dart-features)
- [Başlarken](#toolbox-getting-started)
  * [Ön Gereksinimler](#bangbang-prerequisites)
  * [Local Çalıştırmak](#running-run-locally)
- [Kullanım](#eyes-usage)
- [Destekçiler](#wave-contributing)
<!-- About the Project -->
## :star2: Proje Hakkında


<!-- Screenshots -->
### :camera: Ekran Görüntüleri

<div align="center"> 
  <img src="assets/WhatsApp Görsel 2025-05-12 saat 21.21.36_1f942d20.jpg" alt="screenshot" />
</div>


<!-- TechStack -->
### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://nextjs.org/">Next.js</a></li>
    <li><a href="https://reactjs.org/">React.js</a></li>
    <li><a href="https://tailwindcss.com/">TailwindCSS</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://python.org/">Python</a></li>
  </ul>
</details>

<!-- Features -->
### :dart: Sunduklarımız

- Web-Ready
- Autoencoder tabanlı ve NLP destekli Yapay Zeka Modeli kullanır.
- UX öncelliki kullanıcı arayüzü tasarımı.

<!-- Getting Started -->
## 	:toolbox: Başlarken

<!-- Prerequisites -->
### :bangbang: Ön Gereksiniler

Python 3.10 bulunmalı.
Node.js bulunmalı.

Gerekli Python Kütüphanelerini indiriniz:

```bash
 pip install tensorflow matplotlib seaborn numpy pandas scikit-learn uvicorn fastapi bs4
```

NPM ie gerekli JS kütüphaneleri kurulmalı.

```bash
  cd laptop-chatbot
 npm instal
```
<!-- Run Locally -->
### :running: Local Çalıştırmak

Projeyi önce klonlayın

oneri-sistemi dizinine geçin ve aşağıdaki kodu çalıştırın.

```bash
  uvicorn botapi:app --reload
```

laptop-chatbot dizinine geçin ve aşağıdaki kodu çalıştırın.

```bash
  npm run dev
```

Şimdi websitemize (localhost:3000 in my case) ve API UI (127.0.0.1/docs)'ına erişebilirsiniz.




<!-- Usage -->
## :eyes: Kullanım

Projemizi 3 farklı yol ile kullanabilirsiniz.

1- cli.py'i kullanarak:
oneri-sistemi dizininde:

```bash
  py(unix veya unix-like sistemlerde python) cli.py --prompt "Prompt girin"
```

2- Websitesine Erişerek:

Websitesini eriş (localhost:3000). ChatGPT tarzı bir UI göreceksiniz, bu alanda promptlarınızı yazabilirsiniz.

3- Barış'ın Websitesin'de kullanıma hazır olarak kullanmak:

<a href="https://chatbot.baristok.com.tr" target="_blank">https://chatbot.baristok.com.tr</a>

<!-- Roadmap -->

## :wave: Ortaklar

 Yapılan İşler | <img src="https://avatars.githubusercontent.com/u/114352315?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Mert ARSLAN | <img src="https://avatars.githubusercontent.com/u/165076154?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Barış TOK | <img src="https://avatars.githubusercontent.com/u/180930176?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Sudenur GÖKTEPE | <img src="https://avatars.githubusercontent.com/u/207037760?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Rabia Güllü KOCAEL | <img src="https://avatars.githubusercontent.com/u/175613127?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>İrem Çınar |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
NLP Tarafı| Temel NLP modelini oluşturdu geliştirdi                                                           | NLP modelini geliştirdi                                                          | NLP Model için tavsiye verdi                                                          | ❌                                                           | NLP Model için tavsiye verdi                                                            |
FilterMotor Tarafı|Temel FilterMotor kısmını oluşturdu ve geliştirdi                                                           | FilterMotor kısmını geliştirdi                                                           | FilterMotor için tavsiye verdi                                                          | ❌                                                           |FilterMotor için tavsiye verdi                                                           |
Tavsiye Kısmı| Tavsiye modelini oluşturdu ve geliştirdi                                                          | ❌                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
Deep Learning Model| Autoencoder kullanarak derin öğrenme modelini geliştirdi                                                           | ❌                                                           |Derin öğrenme modelinin kararını aldı                                                          |Derin öğrenme modelinin kararını aldı                                                           | Derin öğrenme modelinin kararını aldı                                                           |
Çıktı Tarafı| CLI ve çıktı uygulamasını oluşturdu ve geliştirdi                                                           | CLI ve çıktı uygulamasını geliştirdi.                                                            | ❌                                                           | ❌                                                           | ❌                                                           |
API tarafı| Temel API'yi oluşturdu ve geliştirdi                                                          | API'nin son halini verdi                                                          | ❌                                                           | ❌                                                           | ❌                                                           |
Web UI Side| ❌                                                        | Ana Web Uygulamasını Oluşturdu ve Geliştirdi                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
Proje Fikri| ❌                                                          | Projenin konseptinde söz sahibi                                                          | Projenin konseptinde söz sahibi                                                           | Fikri veren (DET.)                                                           |Projenin konseptinde söz sahibi (DET.)                                                            |
Raporlar| Splunk Raporun'u ve Splunk & Python Grafiklerini oluşturdu                                                       | Web Raporunda Söz sahibi                                                          | Ana Raporların oluşturucusu ve katılımcısı                                                           |Ana Raporların oluşturucusu ve katılımcısı                                                           |Ana Raporların oluşturucusu ve katılımcısı 
Git/Github Repo| Local Git ve Github Repo'sunu Yönetti.                                                       | ❌                                                           | ❌                                                           | ❌                                                           | ❌
Web-Ready Proje Geliştirme|❌                                                       |Projeyi Deploy etti: <a href="https://chatbot.baristok.com.tr" target="_blank">https://chatbot.baristok.com.tr</a>                                                            | ❌                                                           | ❌                                                           | ❌
Veri Ön-İşleme|Splunk ile veri ön işlemisini yaptı ve bunları CSV ve SQLite formatlarında sakladı.                                                      |❌                                                            | ❌                                                           | ❌                                                           | ❌
Verisetini Oluşturma|❌                                                       |Ham Verisetini oluşturdu CSV                                                           | ❌                                                           | ❌                                                           | ❌
Veri Kaynağını bulmak|❌                                                       |Veri Kaynağını buldu                                                            | ❌                                                           | ❌                                                           | ❌







