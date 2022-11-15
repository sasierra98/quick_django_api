<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project consists in implementing an API that will use a JWT token to authenticate its use. The following
project uses Django and Django Rest Framework.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][Django.com]][Django-url]
* [![Python][Python.com]][Python-url]
* [![Postgresql][Postgres.com]][Postgres-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
* Python 3.9
* Postgres 14.5

### Installation

1. Clone the repo
   ```sh
   https://github.com/sasierra98/quick_django_api.git
   ```
2. Open folder of repo
   ```sh
   cd ~/quick_django_api
   ```
3. Install environment of python
    ```sh
   python -m venv quick_django_api_venv
   ```
4. Activate environment
    ```sh
   source quick_django_api_venv/bin/activate
   ```
5. Install requirements from `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```
6. Create a tabled named `quick_django_api` in postgres.

7. Edit .env file located in root folder with the credentials of database

8. Migrate data to database
   ```sh
   python manage.py migrate
   ```
9. Run server
   ```sh
   python manage.py runserver
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Postman Collection
https://drive.google.com/file/d/15teihzmoEHzQMqasKtFyr-FsVarqnSt0/view?usp=sharing
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Python.com]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Postgres.com]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/