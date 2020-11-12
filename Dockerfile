# cynnexis/tyme
#
# To build this image:
# docker build -t cynnexis/tyme .

FROM python:3.7.6-buster

USER root
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /root/tyme

RUN apt-get update -y && \
	apt-get install -y \
		dos2unix \
		make && \
	rm -rf /var/lib/apt/lists/*

COPY . .

# Some files on Windows use CRLF newlines. It is incompatible with UNIX.
RUN dos2unix *.sh && chmod +x *.sh

# Install requirements
RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "./docker-entrypoint.sh"]
