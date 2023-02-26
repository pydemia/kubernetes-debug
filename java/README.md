

```bash
CONTAINER_NAME=pydemia/springboot-demo:latest
docker build . -f app.Dockerfile -t ${CONTAINER_NAME} && \
docker push ${CONTAINER_NAME}
```

* Swagger: `/swagger-ui/index.html`
