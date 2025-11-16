<!-- vagrant destroy -f && vagrant up -->
<!-- vagrant ssh -->

<!-- Une fois dans la VM 
cd /vagrant/provision
docker compose build demo-app
docker compose up -d
-->

![alt prometheus grafana alertmanager](prom-graf-alert.png)

<h1 align="center"><span style="color:#D24E42">MONITORING & OBSERVABILITY</span></h1>
<h2 align="center">🎨 Stack :  Vagrant - Docker - Prometheus - Grafana - Alertmanager</h2>

Ce projet a pour objectif de construire **un environnement complet et reproductible de monitoring, d’alerting et d’observabilité**, similaire à ce que l’on retrouve dans une architecture de production moderne.

Il a été conçu pour :

* **démontrer une compréhension avancée des outils de monitoring**
  (Prometheus, Grafana, Alertmanager, Node Exporter, cAdvisor),
* **montrer la capacité à instrumenter une application**
  (exposition de métriques personnalisées avec Prometheus client Python),
* **illustrer une approche DevOps professionnelle**
  via l’automatisation (Vagrant), la conteneurisation (Docker) et la structuration du code (tree propre + provisioning reproductible),
* **permettre un déploiement instantané** sur n’importe quelle machine, sans configuration préalable,
* **servir de support pédagogique** pour expliquer à un recruteur comment je mets en place un stack d’observabilité cohérent et propre.

---