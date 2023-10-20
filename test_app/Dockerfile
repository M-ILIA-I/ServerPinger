FROM python:3.11

ENV HOME=/home/app/web

RUN addgroup --system app && adduser --system app --ingroup app

WORKDIR $HOME

COPY ./requirements.txt $HOME

RUN pip install -r requirements.txt

COPY . $HOME
RUN sed -i 's/\r$//g' $HOME/entrypoint.sh
RUN chmod ug+x $HOME/*
RUN chown -R app:app $HOME

USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
