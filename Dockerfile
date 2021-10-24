FROM python:3.8

LABEL maintainer="Gabriel Coelho <gabriel@gasscoelho.me>"

# Set environment variables
ENV WORKSPACE=/usr/app

# Set working directory
WORKDIR $WORKSPACE

COPY requirements.txt ./

# Install python libs
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Add docker-compose-wait tool
ENV WAIT_VERSION 2.9.0
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

CMD ["python", "webscraping.py"]