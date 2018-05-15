# testr 

[![pipeline status](https://gitlab.com/evan-duncan/testr/badges/develop/pipeline.svg)](https://gitlab.com/evan-duncan/testr/commits/develop) [![coverage report](https://gitlab.com/evan-duncan/testr/badges/develop/coverage.svg)](https://gitlab.com/evan-duncan/testr/commits/develop) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ef70155e57746aaa906a748971a1c2e)](https://www.codacy.com/app/pregression/testr?utm_source=gitlab.com&amp;utm_medium=referral&amp;utm_content=pregression/testr&amp;utm_campaign=Badge_Grade)

Working towards making testing an activity that is more effective and efficient in a world where things move quickly


## Development
You're free to stand up your own environment or use docker-compose.
We are not running containers in production so the intent of using Docker
is for rapid development.

### Docker Compose (recommended)
* [https://docs.docker.com/compose/install/](Install Docker Compose)
* Run `docker-compose up`
* Run `docker-compose exec web python3 manage.py migrate`
* Run `docker-compose exec web python3 manage.py createsuperuser`

This will have run all necessary setup and created your own super user for development.

## Built With
* [Python 3](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [jQuery](https://jquery.com/)

## Code of Conduct
We follow the Contributor Covenant Code of Conduct. Please read the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for more information about our code of conduct.

## Contributing
Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for our process on submitting merge requests to us.

## Change Log
We follow [Semantic Versioning](https://semver.org/). To see versions please read our [CHANGELOG](CHANGELOG).

## License
This project is licensed under the GNU Affero General Public License. See the [LICENSE](LICENSE) file for more information.

## Special Thanks
* [Heroku](https://www.heroku.com/)
* [Docker](https://www.docker.com/)
* [Wagtail](https://wagtail.io/)
* [django-allauth](https://github.com/pennersr/django-allauth)
* [django-anymail](https://github.com/anymail/django-anymail)
* [django-tellme](https://github.com/ludrao/django-tellme)
* [django-compressor](https://github.com/django-compressor/django-compressor)
* [behave](https://github.com/behave/behave)
