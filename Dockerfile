FROM python
COPY . /
WORKDIR /
RUN pip install requests
CMD ["python3", "main.py"]