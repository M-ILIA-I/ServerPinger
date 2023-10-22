FROM node:16

ENV FRONT_HOME=/home/app/front

RUN addgroup --system app && adduser --system app --ingroup app

RUN mkdir -p $FRONT_HOME

WORKDIR $FRONT_HOME

COPY . $FRONT_HOME

RUN chmod ug+x $FRONT_HOME/*

RUN chown -R app:app $FRONT_HOME
USER app

RUN npm install