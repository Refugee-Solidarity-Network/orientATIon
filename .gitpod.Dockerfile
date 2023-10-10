FROM gitpod/workspace-full

USER gitpod

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt