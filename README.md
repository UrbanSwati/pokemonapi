# Pokemon API

Pokemon API that consumes the [https://pokeapi.co/api/v2](https://pokeapi.co/api/v2) API.

API/Swagger docs link: [https://api-pokemon.urbanswati.co.za/docs](http://api-pokemon.urbanswati.co.za/docs)

Frontend using the API link: [https://pokemon.urbanswati.co.za/](https://pokemon.urbanswati.co.za/)

Frontend source code, [link](https://github.com/UrbanSwati/pokemon-frontend)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- [Docker](https://docs.docker.com/)
- [Python](https://www.python.org/downloads/)
- [Coffee]()

### Installing

Install the project dependencies either using pip or [pipenv](https://pipenv.pypa.io/en/latest/)

```
pip install -r requirements
```

or with Pipenv

```
pipenv install -r
```

Then activate your environment on Pipenv
```
pipenv shell
```

## Running locally
### Docker
Build the image
```
docker build . -t pokemonapi
```
Then run the container
```
docker run -p 80:80 -t pokemonapi 
```
Then go to [http://localhost](http://localhost) 
or access the Swagger docs at [http://localhost/docs](http://localhost/docs) 

*If you get an error concerning port 80 already being allocated change to a different port*
example using port `8000`
```
docker run -p 8000:80 -t pokemonapi 
```
Then go to [http://localhost:8000](http://localhost:8000) 
or access the Swagger docs at [http://localhost:8000/docs](http://localhost:8000/docs) 
## Running the tests

To run tests use `pytest`

```
pytest
```
To run with coverage
```
pytest --cov
```

### And coding style tests

For code linting use [black](https://pypi.org/project/black/)

```
black .
```

## Deployment

You can use heroku linked with your github account or 
AWS services (ECR, ECS, EKS, Elastic Beanstalk etc)

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
* [Pipenv](https://pipenv.pypa.io/en/latest/) - Dependency Management
* [Docker](https://docs.docker.com/) - Used to containerize application
* [Coffee]() - Used to give energy to spit out code

## Authors

* **William Maphanga** - *Initial work* - [UrbanSwati](https://github.com/UrbanSwati/)

See also the list of [contributors](https://github.com/UrbanSwati/pokemonapi) who participated in this project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://pokeapi.co/api/v2
* Coffee, again
* Python Team (whoop whoop!)
* FastAPI
* and last but not least, Stack Overflow
