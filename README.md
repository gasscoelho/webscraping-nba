# Web Scraping - NBA

A python web scraping program to gather information about [NBA players](https://www.nba.com/players).

## Demo

![webscraping-nba](https://user-images.githubusercontent.com/33602013/138600646-759aa188-8b61-4cf8-bcce-d265497f50e7.gif)

## Get Started

Follow the steps below to properly run this application.

#### Clone the repository:

```bash
git clone https://github.com/gasscoelho/webscraping-nba.git
```
```bash
cd webscraping-nba
```

#### Start the application:

```bash
docker-compose up
```
Alternatively, you can run the app manually by accessing the container' terminal:

```bash
docker-compose run app bash
```

```bash
python webscraping.py
```

## Built With

✨Python <br />
✨Pandas <br />
✨Selenium <br />

## Dessert 🍨

One of the challenges faced during the development of this project was how to make sure to execute the app container only after the Selenium container was ready. The `depends_on` property in the docker-compose file will only set the order of the execution and not in fact wait for the process to be ready. So, to achieve that behavior, I used the `docker-compose-wait` tool.

This tool is a command-line utility that facilitates the orchestration of services by making a docker image to start only after other docker images are ready while using docker-compose.

Check their [repository](https://github.com/ufoscout/docker-compose-wait) to know more about the tool and how to use it.

## Author

**[Gabriel Coelho](https://gasscoelho.me/en)** - Software Engineer