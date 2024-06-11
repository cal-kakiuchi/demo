FROM node:18-buster-slim

ENV TZ Asia/Tokyo

WORKDIR /app

RUN apt update \
    && apt install -y \
    git \
    vim
RUN apt install -y nodejs npm
# RUN npx nuxi init .--force
# RUN npm install n -g
