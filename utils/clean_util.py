def cleaned_data(data):
    """clean data by removing empty keys"""
    if not isinstance(data, (dict, list)):
        return data

    if isinstance(data, list):
        return [v for v in (cleaned_data(v) for v in data) if v]

    return {k: v for k, v in ((k, cleaned_data(v)) for k, v in data.items()) if v}
