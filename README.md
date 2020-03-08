INIT-PYTHON
=========

## Synopsis
This is a project skeleton having full structure of an deployable `python3` project. It includes a startup `bash` script, a `Dockerfile` to build the image with `centos`, a `setup.py` to build into _wheel_ or _egg_ distribution.

## Build
### Using Docker
Build the docker image using the Dockerfile attached.
```
docker build -t init-python:1.0 .
```
Run your arguments to the program directly passing to docker container while running.
```
docker run -t init-python:1.0 sum 1 2
```

### Using virtualenv
Create an virtual environment.
```
virtualenv -p python3
```
Activate the environment.
```
source env/bin/activate
```
Build the project.
```
python setup.py build
```
Install the project.
```
python setup.py install
```

##### Development mode
While developing the project, keep your virtualenv runtime up to date with latest changes you keep making in your code. Instead of `install` use `develop` to keep runtime in development mode.
```
python setup.py develop
```

## F.A.Q.
#### How to include data and other type files into my built project?
In order to include files those are not python scripts, (e.g. `txt`, `csv`, `json`, `xml`) but they are meant to be in some particular directory, use `MANIFEST.in` to capture such paths and tell `setuptools` to include them. 
```
# Add following lines to `MANIFEST.in` to include files at `init/lib/resources` path.

include init/lib/resources/*

```

#### Where to add list of dependencies of my project?
Ideally as we are using `setup.py` here, all your dependencies must be specified in that file under option `install_requires` as an string of list.
> Not mentioning version will let setuptool pick the latest one available.

#### Where I should put my publicly exposing scripts?
All your scripts that ideally be end-point or facing command lines scripts, put them into `init/bin`. Mention them in `setup.py` under option `entry_points`.

#### How I set additional environment variables?
If you are using Dockerfile, you can write them inside `Dockerfile`. Else if you can use them `startup.sh` shell script.