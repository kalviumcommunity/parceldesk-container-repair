# ParcelDesk Container Repair — CA-4

Intentionally broken starter for DevOps Foundation Module 4. Exactly three faults: build, runtime environment configuration, and reachability. Repair in that order. Preserve the existing service and ports.

## Expected behaviour

- Python standard-library HTTP service; no external packages or database.
- Container listens on port **8000**, reachable from outside the container.
- Host port **8080** maps to container port **8000**.
- Required runtime configuration: **APP_MODE=production**. Invalid/missing mode exits with `ERROR: APP_MODE must be production`.
- Successful startup logs actual listening address, port, and mode.
- `GET http://localhost:8080/health` returns HTTP **200** and `ParcelDesk healthy`.
- Unknown paths return 404. Do not add application features.

## Prerequisites and setup

Docker installed/running, Git and POSIX shell available, host port 8080 free. Windows: use preconfigured WSL/Docker integration. Pre-pull image:

```sh
docker pull python:3.12-alpine
```

Fork this repository, clone your fork, then create `fix/ca4-parceldesk`. Push repairs only to your own fork.

## Build, run, inspect

```sh
docker build -t parceldesk:ca4 .
sh run.sh
docker ps -a --filter name=parceldesk-ca4
docker logs parceldesk-ca4
docker port parceldesk-ca4
curl --max-time 5 -i http://localhost:8080/health
```

These commands do not all succeed in the starter. Diagnose rather than replacing the service. A detached container ID alone does not prove startup. Wait a few seconds and inspect logs/status. After a source change rebuild the image, then rerun `sh run.sh`; after a script change rerun the script. The script removes/recreates only `parceldesk-ca4`.

For a running container inspect mode using `docker exec parceldesk-ca4 printenv APP_MODE`. Configuration belongs at runtime, not hardcoded into source/image. No secrets needed. `EXPOSE` is metadata, not port publishing.

## Scope and cleanup

Repair only the Dockerfile source path, runtime variable in run.sh, and application's bind address. Preserve base image, required runtime mode check, route and ports. Rebuild after application changes; recreate without rebuilding for script-only changes. Keep genuine failure and recovery output plus short cause/fix/result notes.

No host Python installation, external packages, cloud account, billing or secrets needed. Use curl for host requests and internet access for image downloads. Run commands from repository root. The script recreates parceldesk-ca4; ensure that name belongs to your exercise before using it.

```sh
docker rm -f parceldesk-ca4
```
