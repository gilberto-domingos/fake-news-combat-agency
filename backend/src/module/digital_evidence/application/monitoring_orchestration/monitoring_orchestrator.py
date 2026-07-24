"""
5) Receber os resultados encontrados da pesquisa
   → monitoring_orchestrator.py
   Receber:
   → resultado retornado pelo SearchContentService
   Fazer:
   → analisar os resultados encontrados
   → decidir que um resultado válido encontrado deve gerar um Incident
   Disparar:
   → IncidentCreateCommand
"""

"""
 
  Enviar essas keywords para o serviço de pesquisa
   → search_content_service.py   
   Fazer:
   → encaminhar as [keywords] para os mecanismos de pesquisa configurados
   → solicitar busca de conteúdos relacionados
           ↓
4) Pesquisar nas fontes externas
   → search_gateway_content_interface.py
   → search_youtube_gateway_implement.py
   → search_google_gateway_implement.py
   → search_tiktok_gateway.py
   → search_facebook_gateway_implement.py
   Receber:
   → [keywords] para pesquisa
   Fazer:
   → executar pesquisas nas plataformas externas
   → coletar os conteúdos encontrados
   Retornar:
   → resultados encontrados para o SearchContentService
           ↓
5) Receber os resultados encontrados da pesquisa
   → monitoring_orchestrator.py
   Receber:
   → resultado retornado pelo SearchContentService
   Fazer:
   → analisar os resultados encontrados
   → decidir que um resultado válido encontrado deve gerar um Incident
   Disparar:
   → IncidentCreateCommand
           ↓
6) Criar Incident
   → incident_create_cmd.py
   → incident_create_handler.py
   → incident_create_service.py
   → incident.py
   Receber:
   → dados do resultado válido encontrado
   Fazer:
   → criar a entidade Incident
   → persistir o incidente
        ↓
7) Criar Evidence
   → evidence_create_cmd.py
   → evidence_create_handler.py
   → evidence_create_service.py
   → evidence.py
   Receber:
   → Incident criado
   Fazer:
   → criar a evidência relacionada ao incidente
   → persistir Evidence
        ↓
8) Criar EvidenceSnapshot
   → evidence_snapshot_create_cmd.py
   → evidence_snapshot_create_handler.py
   → evidence_snapshot_create_service.py
   → evidence_snapshot.py
   Receber:
   → Evidence criada
   Fazer:
   → capturar e preservar o estado da evidência
   → criar o snapshot da prova digital
"""
