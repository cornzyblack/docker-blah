# How to setup

Run the following (replace when necessary):

```shell
cd docker_sample_bash_script
docker image build -t <name_you_want_to_give>:tag .
```

### Looking at a DockerFile
- What do the commands in the Dockerfile mean/do? [Reference](https://docs.docker.com/reference/dockerfile/#cmd)

### Building the image

As an example, see below:

```shell
cd docker_sample_bash_script
docker image build -t docker-sample-bash:latest .
```

The above will build an image in your Docker, and then you can run a container off an image using either the HASH code generated (image id) or directly run a container from an image using the name we gave it. This we will see below:

### Running the container

```shell
docker container run docker-sample-bash:latest
```

If you do not pass a tag, as shown here, `docker container run docker-sample-bash` will still use the **latest** tag for a Docker Image (this happens by default).

### Question
- What is the difference between running `docker container run --rm docker-sample-bash:latest` and `docker container run docker-sample-bash:latest` ?

- What happens if we run `docker image build -t docker-sample-bash:latest .` again?
- What happens if we run `docker image build -t docker-sample-bash:alpha .`?
