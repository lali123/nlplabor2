from concurrent.futures import ThreadPoolExecutor

def fetch_data(id):
    # Simulate network call
    return f"Data for {id}"

ids = [1, 2, 3, 4, 5]
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_data, ids))
