FROM jenkins/jenkins
USER root
RUN apt-get update && apt-get install -y apt-transport-https \
       ca-certificates curl gnupg2 \
       software-properties-common \
       lsb-release \
       sudo && \
       curl -fsSL https://download.docker.com/linux/ubuntu/gpg |gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
       echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" |tee /etc/apt/sources.list.d/docker.list > /dev/null 

RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io
RUN echo 'jenkins ALL=NOPASSWD:ALL' > /etc/sudoers
USER jenkins
RUN jenkins-plugin-cli --plugins "git greenballs"
