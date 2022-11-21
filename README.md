# gousto-recipes

[TODO] About

## Development

### Prerequisites

- [Docker Desktop](https://docs.docker.com/desktop/release-notes/)
- [Docker Dev Environments enabled](https://docs.docker.com/desktop/dev-environments/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code Remote Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


For convinience, you can use the link below to open the project in the Dev Environments of Docker Desktop:

[Start Development](https://open.docker.com/dashboard/dev-envs?url=https://github.com/nichelia/gousto-recipes/tree/main)

Alternatively, you can execute the below command on your terminal:

```bash
docker dev create https://github.com/nichelia/gousto-recipes/tree/main
```

Under the `Docker Dashboard / Dev Environments`, you can click the `Open in VSCode` button.
You can do the same with CLI:

```bash
docker dev open [dev_env_name] [container_ref]
```
where `dev_env_name` can be obtained by running `docker dev list` and `container_ref` by running `docker ps -a`.

Once in VSCode, open `Terminal` and execute the below. The terminal should open within the docker container running the development code.
Make sure that your `pwd` is `/com.docker.devenvironments.code`.
```bash
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
```

A new VSCode pop up will appear with the message `Your application running on port 80 is available.`. Click `Open in browser`. VSCode automatically maps the container port to host port. If you missed the dialogue, you can check the mapped port under `Ports` window of VSCode.