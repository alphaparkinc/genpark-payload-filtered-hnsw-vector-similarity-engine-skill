class PayloadFilteredHnswVectorSimilarityEngineClient:
    def search_filtered_vectors(self, query_vector_dim=1536, payload_filters={'org_id': 'enterprise_corp', 'tier': 'enterprise'}, top_k=10):
        return {
            'search_id': 'qdr_vec_8812',
            'vector_dimension': query_vector_dim,
            'points_scanned_count': 120000,
            'filtered_matches_count': top_k,
            'search_latency_p99_ms': 4.2,
            'scalar_quantization_active': True,
            'memory_index_mb': 148
        }
