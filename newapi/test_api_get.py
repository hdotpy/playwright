def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://gorest.co.in/public/v2/userss")
    print(response.status)
    json_data = response.json()
    print(json_data)
