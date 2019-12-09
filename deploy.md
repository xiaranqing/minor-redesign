### 环境部署

### mongo安装(docker)
```
# 下载mongo4.0镜像

```
docker pull mongo:4.0
```

# 运行
```
docker run --name=mongo4.0 -p 27017:27017 -e /usr/local/var/mongodb:/data/db -d mongo:4.0 --auth
```

```

创建用户

```
docker exec -it mongo4.0 mongo admin
use admin;
db.createUser({     user:'mongo-admin',     pwd: 'mongo-password',     roles: [ { role: "root", db: "admin"} ] });
```
