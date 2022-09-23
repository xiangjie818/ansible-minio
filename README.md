# ansible-minio
MinIO deploy
#### 1) 修改本地hosts文件
示例
```bash
172.16.0.11 node1
172.16.0.12 node2
172.16.0.13 node3
172.16.0.14 node4
```
#### 2) 添加inventory配置
示例
```bash
[minio]
172.16.0.11
172.16.0.12
172.16.0.13
172.16.0.14

[all:vars]
ansible_ssh_port=22
```
#### 2) 修改all.yml
示例
```yaml
devices:
  - '/dev/sdb'
  - '/dev/sdc'
  - '/dev/sdd'
  - '/dev/sde'
  - '/dev/sdf'
  - '/dev/sdg'
  - '/dev/sdh'
  - '/dev/sdi'
  - '/dev/sdj'

mountmap:
  /dev/sdb:
    directory: /minio/export1
  /dev/sdc:
    directory: /minio/export2
  /dev/sdd:
    directory: /minio/export3
  /dev/sde:
    directory: /minio/export4
  /dev/sdf:
    directory: /minio/export5
  /dev/sdg:
    directory: /minio/export6
  /dev/sdh:
    directory: /minio/export7
  /dev/sdi:
    directory: /minio/export8
  /dev/sdj:
    directory: /minio/export9

minio_volumes: "http://node{1...4}:9000/minio/export{1...9}"
minio_opts: "--console-address :9001"
minio_root_user: admin
minio_root_password: f3YOzxEo1Vc5wjYNQwfA
```
#### 3) 安装MinIO
```bash
ansible-playbook minio.yml -i <inventory file>
```
