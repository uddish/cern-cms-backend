# cern-cms-backend

## Hadoop Backup Catalog Backend


#### Build Docker Image
```sh
$ docker build -t image-name:verson .
$ docker run -it image-name:version
```

#### Tag the image and push it to Gitlab
```sh
$ docker tag image-name:verson  gitlab-registry.cern.ch/db/hbackup-webapp-backend/centos-python3-oracle
$ docker push  gitlab-registry.cern.ch/db/hbackup-webapp-backend/centos-python3-oracle
```

#### Openshift Deployment
```sh
$ oc login
$ oc new-app --docker-image="gitlab-registry.cern.ch/db/hbackup-webapp-frontend/react-docker" 
```

#### To switch between Openshift projects
```sh
To list the Projects 
$ oc projects
To switch to another project
$ oc project project-name 
```


### [Django Tutorials](https://goo.gl/2VQfsS)

