FROM python:3.9
WORKDIR /app
COPY . /app
CMD ["python", "treasure_game.py"]