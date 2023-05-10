FROM debian:bullseye-slim
# ENV LANG C.UTF-8

# Legg til din mappe her
ADD /Users/frei/Documents/watchedFolder/ /Users/frei/Documents/watchedFolder/

RUN apt update && apt install -y curl wget

# RUN echo "-sS https://apertium.projectjj.com/apt/install-nightly.sh | bash"

ADD install-nightly.sh /app/
RUN chmod 777 /app/install-nightly.sh
RUN /app/install-nightly.sh

RUN apt search apertium

RUN apt update && apt install apertium-dev -y
RUN apt install apertium-nno-nob -y

ENTRYPOINT ["apertium"]