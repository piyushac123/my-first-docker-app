# Apline Linux DISTRO
FROM alpine:3.5
# Install Python Pip package
RUN apk add --update py2-pip
# move and install required packages
COPY requirements.txt /usr/src/app/ 
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
# move other files
COPY app.py /usr/src/app/ 
COPY templates/index.html /usr/src/app/templates/
 # tell the port number the container should expose
EXPOSE 5000
 # run the application
CMD ["python", "/usr/src/app/app.py"]
