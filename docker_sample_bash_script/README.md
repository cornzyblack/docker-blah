# How to setup

Simply run the following:

```shell
cd docker_sample_bash_script
docker image build -t <name_you_want_to_give>:tag .
```

### Building the image

As an example, see below:

```shell
cd docker_sample_bash_script
docker image build -t docker-sample-1:latest .
```

The above will build an image in your Docker, and then you can run a container off an image using either the HASH code generated (image id), or you can directly run a container from an image using the name we gave it. This we will see below:

### Running the container

```shell
docker container run docker-sample-1:latest
```

Note that not passing a tag as shown here `docker container run docker-sample-1` will still result in using the **latest** tag for a Docker Image (this happens by default).

### Question
- What is the difference between running `docker container run --rm docker-sample-1:latest` and `docker container run docker-sample-1:latest` ?
- What happens if we run `docker image build -t docker-sample-1:latest .` again?
- What happens if we run `docker image build -t docker-sample-1:alpha .`?
