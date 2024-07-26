FROM ubuntu:22.04
WORKDIR /app
COPY . /app/
RUN chmod +x /app/wisecow.sh

RUN apt-get update\
    && apt-get install -y fortune-mod cowsay netcat\
    && rm -rf /var/lib/apt/lists/*


# RUN ln -s /usr/games/cowsay /usr/local/bin/cowsay
# RUN ln -s /usr/games/fortune /usr/local/bin/fortune
EXPOSE 4499
CMD ["/app/wisecow.sh"]