# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for the application
# - xdotool: For active window tracking on Linux
# - espeak: For pyttsx3 (Text-to-Speech)
# - alsa-utils: For audio playback support
# - gcc, libc6-dev: For building Python C extensions (e.g., psutil)
RUN apt-get update && apt-get install -y --no-install-recommends \
    xdotool \
    espeak \
    alsa-utils \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Install uv for fast dependency management
RUN pip install uv

# Copy dependency files first to leverage Docker cache
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
# --frozen ensures we stick strictly to the lockfile
RUN uv sync --frozen

# Add the virtual environment to the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the application code
COPY src ./src
COPY tracker.py .
COPY README.md .

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH=/app/src

# Expose the port the Flask server runs on
EXPOSE 5000

# Define the entrypoint to run the application
# CMD can be overridden by the user (e.g. to run setup-extension)
ENTRYPOINT ["python", "-m", "guilt_3p.main"]
CMD ["run"]
