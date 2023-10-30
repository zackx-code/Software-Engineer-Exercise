#import weightedGraph from .weightedGraph;

districts = {
    'Kasungu': {'Ntchisi': 66, 'Mchinji': 66},
    'Ntchisi': {'Kasungu': 66, 'Dowa': 38},
    'Nkhotakota': {'Ntchisi': 66},
    'Mchinji': {'Kasungu': 66, 'Lilongwe': 109},
    'Dowa': {'Ntchisi': 38, 'Salima': 67, 'Kasungu': 117},
    'Salima': {'Dowa': 67, 'Nkhotakota': 112},
    'Lilongwe': {'Mchinji': 109, 'Dedza': 92},
    'Dedza': {'Lilongwe': 92, 'Ntcheu': 74, 'Salima': 96},
    'Ntcheu': {'Dedza': 74}
}
