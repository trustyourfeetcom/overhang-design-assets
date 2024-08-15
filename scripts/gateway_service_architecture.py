from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.digitalocean.database import DbaasPrimary
from diagrams.generic.device import Mobile
from diagrams.onprem.client import User
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import Spring

with Diagram("Gateway Service Architecture", show=True):
    user = User('User')
    mobile = Mobile('Mobile App')

    with Cluster('Kubernetes Cluster') as kubernetes:
        nginx = Nginx('NGINX')
        
        with Cluster("Backend Microservices") as backend:
            gateway_service = Spring("Gateway Service")
            
            spring = Spring("Spring Services")
            
    user >> mobile
    mobile >> nginx
    nginx >> gateway_service
    gateway_service >> spring
