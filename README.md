# PYRPG

The python command line rpg

----------------------
![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/crashzeus/pyrpg?style=flat-square)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/crashzeus/pyrpg?style=flat-square)
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/crashzeus/pyrpg/latest?style=flat-square)
![GitHub](https://img.shields.io/github/license/Crash-Zeus/pyrpg?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/Crash-Zeus/pyrpg?style=social)

# How to play

## Play image from docker hub

- ```bash 
    docker run -it crashzeus/pyrpg:tag
    ```
Available tag :
- latest (develop only)
- stable
- dev

Docker image from https://hub.docker.com/r/crashzeus/pyrpg

## Play localy
-  First of all, clone repository with 
    ```bash 
        git clone https://github.com/Crash-Zeus/pyrpg.git
    ```
-  Make you sure ton have docker-compose & docker install on your machine
-  Run docker-compose in the repo with
    ```bash 
        docker-compose up -d
    ```
-  Run the game with
    ```bash
        docker exec -it pyrpg python3 ./main.py
    ```
More soon
