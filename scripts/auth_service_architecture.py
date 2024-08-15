from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.digitalocean.database import DbaasPrimary
from diagrams.generic.device import Mobile
from diagrams.onprem.client import User
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import Spring

with Diagram("Auth Service Architecture", show=True):
    user = User('User')
    mobile = Mobile('Mobile App')

    with Cluster('Kubernetes Cluster') as kubernetes:
        nginx = Nginx('NGINX')
        
        with Cluster("Backend Microservices") as backend:
            gateway_service = Spring("Gateway Service")
            
            auth_service = Custom("Auth Service", "./icons/lock.png")
            user_service = Custom("User Service", "./icons/profile-user.png")
            microservices = [auth_service, user_service]
            
            config_service = Spring("Config Service")
            registry_service = Spring("Registry Service")
            
        auth_db = DbaasPrimary("Auth Database")
        user_db = DbaasPrimary('User Database')

    postgres_cluster = PostgreSQL("PostgreSQL Cluster")

    user >> mobile
    mobile >> nginx
    nginx >> gateway_service

    gateway_service >> microservices

    config_service - registry_service

    auth_service >> auth_db
    user_service >> user_db

    auth_db >> postgres_cluster
    user_db >> postgres_cluster
