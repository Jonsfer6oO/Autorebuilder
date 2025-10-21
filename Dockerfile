FROM python:3.12
WORKDIR /app
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN  git config --global user.email "Autorebuilder@email.com"
RUN git config --global user.name "Autorebuilder"

COPY . . 

CMD ["python3", "main.py"]  