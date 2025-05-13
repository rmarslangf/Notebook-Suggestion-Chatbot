Türkçe Readme.md Dosyasına erişmek için: <a href="/ReadmeTR.md">Readme TR</a>
<div align="center">

  <img src="assets/logo.png" alt="logo" width="200" height="auto" />
  <h1>Notebook Suggestion Chatbot</h1>
  
  <p>
    New chatbot using Turkish Lira pricing for notebooks.
  </p>
<br />
</div>

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Run Locally](#running-run-locally)
- [Usage](#eyes-usage)
- [Contributing](#wave-contributing)
<!-- About the Project -->
## :star2: About the Project

This project aims to develop an AI-powered laptop recommendation system that understands user needs in Turkish.
Built on an AutoEncoder-based deep learning architecture, the system analyzes user requests expressed in free-form language and provides personalized recommendations using embedded latent vectors.

<!-- Screenshots -->
### :camera: Screenshots

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
### :dart: Features

- Web-Ready
- Using an Autoencoder-based Deep Learning Model that supports Turkish Language NLP tasks.
- UX-first style UI.

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

Python 3.10 must be Downloaded
Node.js must be Downloaded

Python libs must be downloaded.

```bash
 pip install tensorflow matplotlib seaborn numpy pandas scikit-learn uvicorn fastapi bs4
```

NPM must download JS libs.

```bash
  cd laptop-chatbot
 npm instal
```
<!-- Run Locally -->
### :running: Run Locally

Clone the project

in oneri-sistemi directory

```bash
  uvicorn botapi:app --reload
```

in the other hand, in the laptop-chatbot

```bash
  npm run dev
```

Now you can access to website (localhost:3000 in my case) and API UI (127.0.0.1/docs)




<!-- Usage -->
## :eyes: Usage

You can use our project in 3 different ways.

1- Use cli.py
in oneri-sistemi directory:

```bash
  py(unix or unix-like system you need to use python) cli.py --prompt "enter your Turkish Prompt here"
```


2- Use Website

Access the Website (localhost:3000). You see ChatGPT like UI. Write your prompts in chat area.

3- Acces Baris's website for ready-to-use application

<a href="https://chatbot.baristok.com.tr" target="_blank">https://chatbot.baristok.com.tr</a>

<!-- Roadmap -->

## :wave: Collaborators

 Tasks | <img src="https://avatars.githubusercontent.com/u/114352315?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Mert ARSLAN | <img src="https://avatars.githubusercontent.com/u/165076154?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Barış TOK | <img src="https://avatars.githubusercontent.com/u/180930176?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Sudenur GÖKTEPE | <img src="https://avatars.githubusercontent.com/u/207037760?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>Rabia Güllü KOCAEL | <img src="https://avatars.githubusercontent.com/u/175613127?v=4" width="128" height="128" style="border-radius: 50%; object-fit: cover;"/><br/>İrem Çınar |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
NLP Side| Created and Developed Base NLP Model                                                           | Improved NLP Model                                                          | Gived Advice For NLP Model                                                           | ❌                                                           | Gived Advice For NLP Model                                                            |
Filter Motor Side| Created and Developed Base Filter Engine (FilterMotor)                                                           | Improved Filter Engine(FilterMotor)                                                           | Gived Advice for Filter Engine(FilterMotor)                                                           | ❌                                                           | Gived Advice for Filter Engine(FilterMotor)                                                           |
Recommendation Side| Created and Developed Reccomendation Model(Tavsiye)                                                          | ❌                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
Deep Learning Model| Created and Developed Autoencoder Model                                                           | ❌                                                           | Taked Decision for DL Model                                                           | Taked Decision for DL Model                                                           | Taked Decision for DL Model                                                           |
Output Side| Created and Developed CLI and Output App                                                           | Improved CLI and Output App                                                            | ❌                                                           | ❌                                                           | ❌                                                           |
API Side| Created and Developed Base API                                                          | Perfected the API                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
Web Ui Side| Created Demo Web UI                                                        | Created main Web Application                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
Project Idea| Taked Decision for Main Concept on Project                                                          | Taked Decision for Main Concept on Project                                                          | Taked Decision for Main Concept on Project                                                           | Originiator (also DET.)                                                           | Taked Decision for Main Concept on Project (also DET.)                                                            |
Reports| Created Splunk Report and Python & Splunk Graphs                                                       | Created Web-side Report                                                           | Created and Contributed Main Reports                                                           | Created and Contributed Reports                                                           | Created and Contributed Reports
Git/Github Repo| Administrated Local Git and Remote Github Repo                                                       | ❌                                                           | ❌                                                           | ❌                                                           | ❌
Web-Ready Project Creation|❌                                                       |Maked the project Web-Ready and Deployed on: <a href="https://chatbot.baristok.com.tr" target="_blank">https://chatbot.baristok.com.tr</a>                                                            | ❌                                                           | ❌                                                           | ❌
Data Processing|Maked the data Preprocess with Splunk and stored it on CSV and SQLite                                                       |❌                                                            | ❌                                                           | ❌                                                           | ❌
Dataset Creation|❌                                                       |Created dataset with Web Scrape                                                            | ❌                                                           | ❌                                                           | ❌
Data Source Founding|Founded Data Source's Target HTML Header                                                       |Founded Data Source                                                            | ❌                                                           | ❌                                                           | ❌






