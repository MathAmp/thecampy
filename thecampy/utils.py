SPACE = "&nbsp;"


def request_url(resource):
    baseUrl = 'https://www.thecamp.or.kr'
    r = "{}/{}".format(baseUrl, resource)
    return r


def content_str_to_html_str(content: str) -> str:
    content = content.replace(" ", SPACE).replace("\r", "")
    return ''.join(["<p>{0}</p>".format(x if x else SPACE)
                    for x in content.split('\n')])

