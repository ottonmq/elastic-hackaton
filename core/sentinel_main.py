from agents.elastic_agent import ElasticAgent

def run_audit():
    print("🏮 INICIANDO AUDITORÍA ELASTIC - ARQUITECTO OTTO")
    agent = ElasticAgent()
    info = agent.check_connection()
    print(f"ESTADO DEL NODO: {info}")

if __name__ == "__main__":
    run_audit()
