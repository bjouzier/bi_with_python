from google.cloud import bigquery

client=bigquery.Client()
query = """
SELECT * FROM `prj-perso01.Comptes_Perso.Comptes` LIMIT 500
"""
query_job = client.query(query) 

results = query_job.result()
for row in results:
    print(row)
    