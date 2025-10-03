import allure


def attach_reqres(response):
        request = response.request
        allure.attach(request.method, name="Метод запроса", 
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(request.url, name="Url request", 
                      attachment_type=allure.attachment_type.TEXT)