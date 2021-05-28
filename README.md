A demo application of fastapi

# Installation
- pip install fastapi

# How to run on Linux
## univon
  
 - pip install uvicorn
 - uvicorn main:app --host '0.0.0.0' --port 8080 --reload

## gunicon
 - pip install gunicorn
 - gunicorn main:app -b 0.0.0.0:5000  -w 4 -k uvicorn.workers.UvicornH11Worker --daemon 
