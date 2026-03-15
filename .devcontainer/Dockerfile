FROM almalinux:9

# 1. Install System Utils, 'which', 'tar', and Docker CLI
# We include dnf-plugins-core to get 'config-manager'
RUN dnf install -y dnf-plugins-core sudo shadow-utils gcc-c++ make which tar git && \
    dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
    dnf install -y docker-ce-cli && \
    dnf clean all

# 2. Install Node.js 20 and Python 3.11
RUN curl -sL https://rpm.nodesource.com/setup_20.x | bash - && \
    dnf install -y nodejs python3.11 python3.11-pip python3.11-devel && \
    dnf clean all

# 3. Set up Python Alternatives (Maps 'python' and 'python3' to 3.11)
RUN alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 && \
    alternatives --install /usr/bin/python python /usr/bin/python3.11 1 && \
    alternatives --install /usr/bin/pip pip /usr/bin/pip3.11 1

# 4. Install Global Runtimes (Angular and Flask)
# Done as root so they are available system-wide
RUN npm install -g @angular/cli && \
    pip install flask flask-cors

# 5. Create the vscode user with sudo privileges
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set the default user
USER $USERNAME