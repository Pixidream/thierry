<div align="center">
  <img src="./resources/images/man.svg" height="128" />
  <br />
  <h1>THIERRY</h1>
  <blockquote>
  <p>Django backend for Jean Baptiste Show website</p>
  </blockquote>
  <br />
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" />
  <img src="./resources/images/made-with-django.svg" />
  <br />
  <img src="https://github.com/Pixidream/thierry/actions/workflows/codeql-analysis.yml/badge.svg?branch=main" />
  <img src="https://github.com/Pixidream/thierry/actions/workflows/code-quality.yml/badge.svg?branch=main" />
  <img src="https://github.com/Pixidream/thierry/actions/workflows/tests.yml/badge.svg?branch=main" />
  <br />
  <br />
  <br />
  <a href="https://www.youtube.com/user/JeanBaptisteShow" target="_blank">
    <img src="./resources/images/banner.png" />
  </a>
  <br />
  <br />
  <br />
  <div>
    <div align="center">
      <a href="https://shop.spreadshirt.fr/jeanbaptisteshow/hommes?q=D1" target="_blank">
        <img src="./resources/images/tshirt.png" />
      </a>
      <a href="https://www.tipeee.com/jean-baptiste-show" target="_blank">
        <img src="./resources/images/tipee.png" />
      </a>
    </div>
    <div align="center">
      <a href="https://streamlabs.com/jeanbaptisteshow" target="_blank">
        <img src="./resources/images/donate.png" />
      </a>
      <a href="http://bit.ly/OALMUB" target="_blank">
        <img src="./resources/images/twitter.png" />
      </a>
    </div>
    <div align="center">
      <a href="https://discord.com/invite/aQtFyQk" target="_blank">
        <img src="https://discordapp.com/api/guilds/595603581349134346/widget.png?style=banner2" alt="Discord Banner 2"/>
      </a>
      <a href="https://twitch.tv/jeanbaptisteshow" target="_blank" style="margin-left: 2rem;">
        <img src="./resources/images/twitch.svg" width="260"/>
      </a>
    </div>
  </div>
</div>

---

## Requirements
- poetry
- docker (with docker-compose)
- python ^3.10
- make

## Stack
- backend server: Django + Django Rest Framework
- database: Postgres
- cache: Redis

## Development
Copy `.env.example` to `.env.dev` and [get a Youtube API Key](https://console.developers.google.com). Add the key to `.env.dev`.

> `app/` folder in mounter in web container so you can have hot reload while running code in docker

Default user:password for http://localhost:8000/admin is `admin:admin`

Then, the make file provide shortcuts for regular actions:
- `make dev`: up docker-compose
- `make updatedebriefs`: sync debriefs with database
- `make test`: run tests
- `make pre-commit` run pre-commit on all files (good to run before committing)
- `make stop`: down docker-compose
- `make stop-clean`: down docker-compose and remove volumes and possible orphans containers
