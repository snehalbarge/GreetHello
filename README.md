# Hello World Web Application API

I have build REST API server in Python using the Django framework.   


## Setup
- Install Python 3.  
[Download and install python 3.](https://www.python.org/downloads/)
- Install Docker.  
[Download and install Docker](https://docs.docker.com/engine/install/)

- Go to Project Folder
- Build docker Image:  
Open terminal and run: 
```
docker build -t helloworldapp .
```
- To run the docker container.
```
docker run -p 8000:8000 -i -t helloworldapp
```

# Questions and Answers

**1. What other information would you add to health endpoint json object in step 2? Explain what would be the use case for that extra information?**

I shall use a parallel thread to implement the last down time of the application which is used to give efficient scaling and check server resilience.

**2. What branching strategy would you use for development?**

I shall use feature and env based branching strategy. A branch with an id is created here with the new feature which we are adding to the software. As soon as the feature becomes absolutely functional, it is merged together with dev branch while integration testing. Also, the master contains the latest version of software for full stage testing. The latest version releases can be tracked by using git tags.

**3. What CICD tool/service would you use?**

I would say Jenkins, because of its most important part of Jenkins tool is Jenkins Build Pipeline. This potrays various jobs running on builds after commits made by developers. It also informs about current tasks Jenkins is executing. It supports plugins with various platforms like Github, Gitlab , Bitbucket etc. It is time efficient and also helps in to make release to production faster as issues found as soon as code broken. I also worked with TeamCity.

**4. What stages would you have in the CICD pipeline?**

Sandbox, Dev, Stage, Prod

**5. What would be the purpose of each stage in CICD pipeline?**

- **Prod** - The stable product is ready for end users.
- **Stage** - The product is tested by integration testing and pre-end users.
- **Dev** - Active for development users to develop further and highly unstable.
- **Sandbox** - testing playground for developers for further research.
