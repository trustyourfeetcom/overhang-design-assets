from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.vcs import Github
from diagrams.programming.framework import Spring

with Diagram("Properties Architecture", show=True):
        
    github = Github("Properties Repository")
    config = Custom('application.properties', './icons/gear.png')
    with Cluster("Backend Microservices") as backend:
        
        config_service = Spring("Config Service")
        spring = Spring('Spring Apps')
    github >> config >> config_service << spring
