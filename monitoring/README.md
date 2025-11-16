<!-- vagrant destroy -f && vagrant up -->
<!-- vagrant ssh -->

<!-- Une fois dans la VM 
cd /vagrant/provision
docker compose build demo-app
docker compose up -d
-->

![alt prometheus grafana alertmanager](prom-graf-alert.png)

<h1 align="center"><span style="color:#D24E42">MONITORING & OBSERVABILITY</span></h1>
<h2 align="center"><span style='color:#D24E42'>Stack :  Vagrant - Docker - Prometheus - Grafana - Alertmanager</span></h2>

<h2 align="center"><span style="color:#D24E42">I - INTRODUCTION</span></h1>

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

<h2 align="center"><span style="color:#D24E42">II - VISION GÉNÉRALE : comment l’environnement fonctionne ?</span></h1>

Lorsque l’on lance l’environnement avec `vagrant up`, la VM installe automatiquement Docker, puis démarre un stack complet comprenant :

### 🔹 **1. Une application Python instrumentée**

→ simule un service réel
→ expose des métriques internes (latence, requêtes, gauge aléatoire…) sur `/metrics`

### 🔹 **2. Prometheus**

→ collecte toutes les métriques :

* de l’application
* du système (node_exporter)
* des conteneurs (cAdvisor)
* de lui-même
  → stocke les données dans une base TSDB

### 🔹 **3. Grafana**

→ fournit des dashboards interactifs
→ les dashboards sont **auto-provisionnés**, ce qui prouve un niveau DevOps avancé
→ un exemple de dashboard est fourni (app + système + conteneurs)

### 🔹 **4. Alertmanager**

→ gère les alertes configurées dans Prometheus
→ peut notifier (email, Slack, webhook…)

### 🔹 **5. Node Exporter**

→ expose les métriques de la VM (CPU, RAM, I/O, filesystems…)

### 🔹 **6. cAdvisor**

→ expose les métriques de performance des conteneurs Docker

---