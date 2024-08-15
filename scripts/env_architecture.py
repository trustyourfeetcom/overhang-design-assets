from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.ci import GithubActions
from diagrams.programming.framework import Spring

with Diagram("Environment Variables Workflow", show=True):

    with Cluster('Kubernetes Cluster') as kubernetes:
        helm = Custom('Helm', './logos/helm.png')
        with Cluster("Backend Microservices") as backend:
            spring = Spring("Spring App")
            variable = Custom('Env Variable', './icons/variable.png')

    action = GithubActions("GitHub Actions")
    action >> helm >> spring >> variable