
def test_api_get(playwright):
    request=playwright.request.new_context()
    response=request.get("https://api.restful-api.dev/collections",
                         headers={"x-api-key": "a220afa3-848b-4aeb-9c7b-3908d519543a"})

    print(response)
    print(response.body)
    data=response.json()
    print(data)
    request.dispose()
def test_api_post(playwright):
    request=playwright.request.new_context()
    response=request.post("https://api.restful-api.dev/collections/products/objects",
                          headers={"x-api-key": "a220afa3-848b-4aeb-9c7b-3908d519543a"},
                          data={
                                "name": "Apple MacBook Pro 16",
                                "data": {
                                    "year": 2019,
                                    "price": 1849.99,
                                    "CPU model": "Intel Core i9",
                                    "Hard disk size": "1 TB"
                                }
                                })
    print(response)
    response_data=response.json()
    print(response_data)
    created_id=response_data["id"]    
    print(created_id)