"""
elasticsearch

"""

from elasticsearch import Elasticsearch

es = Elasticsearch()


def search(query: str):
    dsl = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "genre", "describe"]
            }
        },
        "highlight": {
            "fields": {
                "name": {},
                "genre": {},
                "describe": {}
            }
        }
    }

    result = es.search(index='douban', docvalue_fields=['movies'], body=dsl, size=10)
    return result
