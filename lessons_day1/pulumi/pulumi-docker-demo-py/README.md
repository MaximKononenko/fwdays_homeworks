# Pulumi Docker demo (Python)

This directory contains a Pulumi Python program that uses the `pulumi-docker` provider to create a small demo: an `nginx` container serving a static page and a `redis` container on an internal Docker network.

Quick steps (local machine with Python & Pulumi installed)

1. Create a Python virtualenv and install requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Login to a Pulumi backend (local backend recommended for homework):

```bash
pulumi login file://$(pwd)/.pulumi
```

3. Initialize and deploy:

```bash
pulumi stack init dev    # only if stack doesn't exist
pulumi up --yes
```

4. Open `http://localhost:8081` (dev stack uses port 8081 by default)

Dockerized usage

You can run Pulumi inside a container. Below are two examples: a quick ad-hoc run, and a recommended, more robust run that shares a host-backed Pulumi backend and the Docker socket so the host and container see the same stacks.

Quick (ad-hoc) example — runs Pulumi inside a container but does not mount the host Docker socket or a host backend (useful for quick experiments):

```bash
docker run --rm -it \
  -v "$(pwd)":/workspace \
  -v pulumi-home:/root/.pulumi \
  -w /workspace/fwdays_homeworks/lessons_day1/pulumi/pulumi-docker-demo-py \
  --user "$(id -u):$(id -g)" \
  python:3.11-bullseye \
  bash -lc "pip install -r requirements.txt pulumi && curl -fsSL https://get.pulumi.com | sh && export PATH=/root/.pulumi/bin:$PATH && pulumi login file:///workspace/.pulumi && pulumi up --yes"
```

Recommended (robust) example — mounts the host Docker socket and a host directory for the Pulumi local backend so both host and container share the same stack records. Run the first two preparatory commands once:

```bash
# create a host backend directory and make it writable by your user (run once)
mkdir -p ~/pet-projects/pulumi-backend
chown $(id -u):$(id -g) ~/pet-projects/pulumi-backend

docker run --rm -it \
  -v ~/pet-projects/fwdays_homeworks/lessons_day1/pulumi/pulumi-docker-demo-py:/workspace \
  -v ~/pet-projects/pulumi-backend:/workspace/.pulumi \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e HOME=/workspace \
  -e USER="$(id -un)" \
  -w /workspace \
  --user "$(id -u):$(stat -c '%g' /var/run/docker.sock)" \
  python:3.11-bullseye \
  bash -lc "\
    python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    curl -fsSL https://get.pulumi.com | sh && \
    export PATH=\$HOME/.pulumi/bin:\$PATH && \
    pulumi login file://\$PWD/.pulumi && \
    pulumi up --yes"
```

```bash
pulumi login file:///~/pet-projects/pulumi-backend
```
Notes on backend visibility and socket permissions

- If you run Pulumi inside the container with a Docker named volume (`pulumi-home`) the stacks are stored in that volume and the host `pulumi` CLI will not see them unless you copy or mount that backend into the host filesystem. To inspect the named volume from the host you can copy its contents out:

```bash
mkdir -p /tmp/pulumi-from-volume
docker run --rm -v pulumi-home:/from -v /tmp/pulumi-from-volume:/to busybox sh -c "cp -a /from/. /to/ || true"
ls -la /tmp/pulumi-from-volume
```

- Alternatively, use the host-backed directory shown above (`~/pet-projects/pulumi-backend`) so the same backend is available to host and container. After running the recommended example you can run on the host:

```bash
cd ~/pet-projects/fwdays_homeworks/lessons_day1/pulumi/pulumi-docker-demo-py
pulumi login file://$(pwd)/.pulumi
pulumi stack ls
```

- If you prefer the named volume and need to change its owner so your non-root container user can write into it, chown it once from a short-lived container:

```bash
docker run --rm -v pulumi-home:/data alpine sh -c "chown -R $(id -u):$(id -g) /data"
```

Notes
- The program uses the Docker daemon available to the container/host. If you run inside Docker, you must provide access to Docker (e.g., `-v /var/run/docker.sock:/var/run/docker.sock`).
- For CI or repeated runs, consider building an image that already has Pulumi + Python deps installed.
