FROM debian:bullseye-slim

WORKDIR /app

RUN apt-get update -y && apt-get install -y \
    python3 python3-pip python3-setuptools git zsh curl

COPY ./assets/fonts/ /usr/share/fonts

COPY ./requirements.txt /app

COPY ./requirements_dev.txt /app

COPY ./docker-entrypoint.sh /app

RUN chmod +x ./docker-entrypoint.sh

RUN pip install -r ./requirements.txt

RUN pip install -r ./requirements_dev.txt

RUN chsh -s $(which zsh) && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
    zsh

CMD [ "./docker-entrypoint.sh" ]