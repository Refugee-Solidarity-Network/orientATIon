FROM gitpod/workspace-full

USER gitpod

# Install and set global Python version to 3.11
RUN pyenv install 3.11 \
    && pyenv global 3.11

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt