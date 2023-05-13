FROM debian:bullseye-slim
# ENV LANG C.UTF-8

RUN apt update && apt install -y curl wget

RUN wget -P /app https://www.nb.no/sbfil/npk-2011-2022/npk_2011_2022.tmx

ADD install-nightly.sh /app/
RUN chmod 777 /app/install-nightly.sh
RUN /app/install-nightly.sh

RUN apt search apertium

RUN apt update && apt install apertium-dev -y
RUN apt install apertium-nno-nob -y

# ENTRYPOINT ["apertium"]