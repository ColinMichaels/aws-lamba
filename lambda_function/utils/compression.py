import gzip
import json

def compress_data(data):
    json_data = json.dumps(data).encode('utf-8')
    return gzip.compress(json_data)


def decompress_data(compressed_data):
    json_data = gzip.decompress(compressed_data).decode('utf-8')
    return json.loads(json_data)
