docker build -t beejuggame .
docker run -d --name beejugcontainer -p 80:80 beejuggame
