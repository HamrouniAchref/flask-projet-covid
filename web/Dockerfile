FROM python:3.6
RUN apt-get update -y
RUN pip install --upgrade pip
COPY . /app 
WORKDIR /app
RUN pip install scikit-learn numpy scipy pandas 
RUN pip install -r requirements.txt


#RUN python -c "import nltk; nltk.download('all-corpora')"
ENTRYPOINT ["python"]
CMD ["app/app.py"]
