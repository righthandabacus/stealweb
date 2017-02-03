### How to stop "Docker maven builds" downloading the whole maven repository everytime

When you google for this problem you can find different answers with
different types of mounting of m2 folder. But if you are planing to
mount your local m2 folder into Docker that is not really a very clean
solution. The problem with that is the Docker build you are planing can
be biased based on your local builds you have.  
  
So I asked the question in
[stackoverflow](http://stackoverflow.com/questions/39977955/how-to-mount-docker-volume-into-my-docker-project-using-compose)
and here is docker-compose.yml of my final working solution  
  
version: '2'  
services:  
  client:  
    build: .  
    container\_name: client  
    volumes:  
      - m2repo:/root/.m2/repository  
volumes:  
  m2repo:  
  
Now when you run the system for the 2nd time, it will not load the maven
content form the internet spending hours downloading them.  
  



