# Run hello world locally on host machine:
```bash
python3 -m venv venv
pip3 install -r requirements.txt
python3 ./hello-world.py
```

# Build docker image:
```bash
docker build -t hello-world-app:latest .
```

# Run docker container:
```bash
docker run -it -p 8080:80 hello-world-app:latest
```