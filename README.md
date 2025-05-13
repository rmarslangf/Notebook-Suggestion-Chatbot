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

You can use our project in 3 ways.

1- Use cli.py
in oneri-sistemi directory:

```bash
  py(unix or unix-like system you need to use python) cli.py --prompt "enter your Turkish Prompt here"
```
2- Use API UI

Access the API UI (127.0.0.1/docs)
in the ui you see try option on the top right, click on it.
After that, you can enter your prompt on json format.

3- Use Website

Access the Website (localhost:3000). You see ChatGPT like UI. Write your prompts in chat area.

4- Acces Baris's website for ready-to-use application

<a href="https://chatbot.baristok.com.tr" target="_blank">https://chatbot.baristok.com.tr</a>

<!-- Roadmap -->

## :wave: Contributing

| ![Mert](https://avatars.githubusercontent.com/u/114352315?v=4)<br/>Mert ARSLAN | ![Barış](https://avatars.githubusercontent.com/u/165076154?v=4)<br/>Barış TOK | ![Sude](https://avatars.githubusercontent.com/u/180930176?v=4)<br/>Sudenur GÖKTEPE | ![Rabia](https://avatars.githubusercontent.com/u/207037760?v=4)<br/>Rabia Güllü KOCAEL | ![İrem](https://avatars.githubusercontent.com/u/175613127?v=4)<br/>İrem Çınar |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Created and Developed Base NLP Model                                                           | Improved NLP Model                                                          | Gived Advice For NLP Model                                                           | ❌                                                           | Gived Advice For NLP Model                                                            |
| Created and Developed Base Filter Engine (FilterMotor)                                                           | Improved Filter Engine(FilterMotor)                                                           | Gived Advice for Filter Engine(FilterMotor)                                                           | ❌                                                           | Gived Advice for Filter Engine(FilterMotor)                                                           |
| Created and Developed Reccomendation Model(Tavsiye)                                                          | ❌                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
| Created and Developed Autoencoder Model                                                           | ❌                                                           | Taked Decision for DL Model                                                           | Taked Decision for DL Model                                                           | Taked Decision for DL Model                                                           |
| Created and Developed CLI and Output App                                                           | Improved CLI and Output App                                                            | ❌                                                           | ❌                                                           | ❌                                                           |
| Created and Developed Base API                                                          | Perfected the API                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
| Created Demo Web UI                                                        | Created main Web Application                                                           | ❌                                                           | ❌                                                           | ❌                                                           |
| Taked Decision for Main Concept on Project                                                          | Taked Decision for Main Concept on Project                                                          | Taked Decision for Main Concept on Project                                                           | Originiator (also DET.)                                                           | Taked Decision for Main Concept on Project (also DET.)                                                            |
| Created Splunk Report and Python & Splunk Graphs                                                       | Created Web-side Report                                                           | Created and Contributed Main Reports                                                           | Created and Contributed Reports                                                           | Created and Contributed Reports
| Administrated Local Git and Remote Github Repo                                                       | ❌                                                           | ❌                                                           | ❌                                                           | ❌
|❌                                                       |Maked the project Web-Ready and Deployed on: <a href="https://chatbot.baristok.com.tr" target="_blank">https://chatbot.baristok.com.tr</a>                                                            | ❌                                                           | ❌                                                           | ❌
|Maked the data Preprocess with Splunk and stored it on CSV and SQLite                                                       |❌                                                            | ❌                                                           | ❌                                                           | ❌
|❌                                                       |Created dataset with Web Scrape                                                            | ❌                                                           | ❌                                                           | ❌
|Founded source of data's (HTML table)                                                       |Founded Data Source                                                            | ❌                                                           | ❌                                                           | ❌






