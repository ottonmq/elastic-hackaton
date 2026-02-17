from elasticsearch import Elasticsearch

class ElasticAgent:
    def __init__(self, cloud_id=None, api_key=None):
        # Aquí va la conexión real al clúster de Elastic
        if cloud_id and api_key:
            self.client = Elasticsearch(cloud_id=cloud_id, api_key=api_key)
        else:
            self.client = Elasticsearch("http://localhost:9200") # Local node

    def check_connection(self):
        try:
            return self.client.info()
        except Exception as e:
            return f"Error de conexión: {str(e)}"
