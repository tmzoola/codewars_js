def domain_name(url):
    if "//" in url:
        new_url = url.split('//')[1]
        if 'www.' in new_url:
            return new_url.split('.')[1]
        else:
            return new_url.split('.')[0]
    else:
        if 'www.' in url:
            return url.split('.')[1]
        else:
            return url.split('.')[0]



print(domain_name("www.xakep.ru"))