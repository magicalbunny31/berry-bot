# install dependencies using a builder (for security) and by using python:3 (as it includes compilers)
FROM python:3 AS builder

# set the directory for this builder
WORKDIR /build

# copy configuration files and install dependencies
COPY ./requirements.txt ./
RUN python -m venv /opt/venv && \
   /opt/venv/bin/pip install --no-cache-dir --upgrade pip && \
   /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


# app's final image
FROM python:3-slim

# install:
#    curl (for installing https://dotenvx.com/)
#    dotenvx (https://dotenvx.com/)
RUN apt-get update \
   && apt-get install -y curl \
   && curl -sfS https://dotenvx.sh/install.sh | sh \
   && apt-get purge -y --auto-remove curl \
   && rm -rf /var/lib/apt/lists/*

# change user
RUN useradd -m -u 1000 python
USER python

# set the directory for this app and change its permissions
WORKDIR /home/python/berry-bot/
RUN chown -R python:python /home/python/berry-bot/
WORKDIR /home/python/berry-bot/berry-bot-discord/
RUN chown -R python:python /home/python/berry-bot/berry-bot-discord/

# copy virtual environment from the builder
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder --chown=python:python /opt/venv /opt/venv

# copy the rest of the files and change its permissions
COPY --chown=python:python ./ ./

# start the app
CMD ["dotenvx", "run", "-f", "./src/.env", "-fk", "./src/.env.keys", "--", "python", "-u", "-m", "src.main"]