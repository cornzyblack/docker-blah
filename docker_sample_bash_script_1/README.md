# How to setup

Run the following (replace when necessary):

```shell
cd docker_sample_bash_script_1
docker image build -t <name_you_want_to_give>:tag .
```

### Building the image

As an example, see below:

```shell
cd docker_sample_bash_script_1
docker image build -t docker-sample-bash-1:latest .
```

The above will build an image in your Docker, and then you can run a container off an image using either the HASH code generated (image id), or you can directly run a container from an image using the name we gave it. This we will see below:

### Running the container

```shell
docker container run docker-sample-bash-1:latest
```

### Question

- Why is the container not working properly?  <!-- Let's do some investigations. -->
- What is the difference between the **Dockerfile** in this folder, and the one in `docker_sample_bash_script/`?
- What does this do `docker container run --name SDA_DE_test docker-sample-bash-1`
- What is the difference between `docker container run docker-sample-bash-1:latest` and `docker container run --name SDA_DE_test docker-sample-bash-1`?

Let's further inspect the Docker image using the GUI or terminal.

- What does the following do:
`docker container run --env MYNAME=Eni --env FAVOURITE_COLOR=slimshady --name SDA_DE_test docker-sample-bash-1:latest`
[Hint here](https://docs.docker.com/reference/cli/docker/container/run/#env)

If the above code breaks for you, what's going on?

- What does this do `docker container inspect SDA_DE_test`?
- What does `docker image inspect docker-sample-bash-1:latest` do? What's the difference?
- What does this do? `docker container --rm run --env MYNAME=slimshady --env FAVOURITE_COLOR=Blue --name SDA_DE_test_shady docker-sample-bash-1:latest`
