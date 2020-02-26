# PYRPG

The python command line rpg

----------------------

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
