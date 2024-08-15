from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.programming.framework import Spring

with Diagram("Config Service Architecture", show=True, direction="TB"):
        
    with Cluster("Backend Microservices") as backend:
        gateway_service = Spring("Gateway Service")
        
        auth_service = Custom("Auth Service", "./icons/lock.png")
        user_service = Custom("User Service", "./icons/profile-user.png")
        
        config_service = Spring("Config Service")
        registry_service = Spring("Registry Service")
        microservices = [auth_service, user_service, registry_service, gateway_service]

    config_service >> microservices
