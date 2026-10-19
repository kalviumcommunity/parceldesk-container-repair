# ParcelDesk Container Repair — CA-4

Intentionally broken starter for DevOps Foundation Module 4. Exactly three faults: build, runtime environment configuration, and reachability. Repair in that order using your assessment instructions. No solution included.

## Expected behaviour

- Python standard-library HTTP service; no external packages or database.
- Container listens on port **8000**, reachable from outside the container.
- Host port **8080** maps to container port **8000**.
- Required runtime configuration: **APP_MODE=production**. Invalid/missing mode exits with `ERROR: APP_MODE must be production`.
- Successful startup logs actual listening address, port, and mode.
- `GET http://localhost:8080/health` returns HTTP **200** and `ParcelDesk healthy`.
- Unknown paths return 404. Do not add application features.

## Setup — before assessment timer

Docker installed/running, Git and POSIX shell available, host port 8080 free. Windows: use preconfigured WSL/Docker integration. Pre-pull image:

```sh
docker pull python:3.12-alpine
```

Fork this repository, clone your fork, then create `fix/ca4-parceldesk`. No PR against this instructor repository.

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

## Submit and clean up

Follow instructor's `assessment.md`: one PDF with three labelled task sections, real before/after terminal evidence, changed lines and root-cause notes, plus your fork URL, branch and commit. Push only to your own fork. No cloud, paid services, PR, or video required.

When finished:

```sh
docker rm -f parceldesk-ca4
```
