def redirectionUrl(language):
    url = "www.example.org/"

    if language == "English":
        url += "en"
    elif language == "Japanese":
        url += "ja"
    elif language == "Spanish":
        url += "es"
    elif language == "Russian":
        url += "ru"
    return url


