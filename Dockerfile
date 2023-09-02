FROM python:3.8-slim

LABEL authors="rvanhopp"

# Set up and install the app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "app.py"]
