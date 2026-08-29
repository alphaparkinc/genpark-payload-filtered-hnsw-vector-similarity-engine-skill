from client import PayloadFilteredHnswVectorSimilarityEngineClient

def main():
    client = PayloadFilteredHnswVectorSimilarityEngineClient()
    res = client.search_filtered_vectors(1536, {'workspace': 'engineering_ml', 'region': 'us-east-1'}, 8)
    print('Vector Search: ' + res['search_id'] + ' (Dim: ' + str(res['vector_dimension']) + ')')
    print('Points Scanned: ' + str(res['points_scanned_count']) + ' -> Filtered Matches: ' + str(res['filtered_matches_count']))
    print('P99 Latency: ' + str(res['search_latency_p99_ms']) + 'ms | Scalar Quantization: ' + str(res['scalar_quantization_active']))
    print('Index Memory: ' + str(res['memory_index_mb']) + ' MB')

if __name__ == '__main__':
    main()
