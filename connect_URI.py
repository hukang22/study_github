def connect_URI(server, port):
    str = 'http://' + server + ':' + port
    return str

result = connect_URI('test.com', '8080')
result1 = connect_URI(port='8080', server='test2.com') #키워드 파라미터
print(result)
print(result1)