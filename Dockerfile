FROM centos:8

LABEL MAINTAINER "https://github.com/arghajit"

RUN yum install -y epel-release sudo jq gcc python3 python3-devel
RUN mkdir -p /home/app /home/app/.ssh
RUN useradd -m -s /bin/bash -d /home/app -c 'App Administrator' -p 'docker' -U app
RUN usermod -aG wheel app
RUN echo 'app     ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY .  /home/app/
RUN chmod +x /home/app/startup.sh
# RUN chmod +x /home/fsge/startup.sh /home/fsge/secrets-parameters.sh
RUN chown -R app:app /home/app

WORKDIR /home/app
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python3 get-pip.py
RUN pip install virtualenv && virtualenv -p python3 env && source env/bin/activate
RUN python3 setup.py install

USER app
ENTRYPOINT ["/bin/bash","./startup.sh"]