def paginate_results(results, page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return results[start_index:end_index]