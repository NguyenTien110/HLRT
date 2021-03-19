import requests
import textwrap

link = 'https://www.carmudi.vn/mua-ban-o-to/'
HLRT = []  # HLRT is void at the begining


def get_html(link_get):
    html = requests.get(link_get)
    lines = [textwrap.dedent(line.rstrip()) for line in html.content.decode('utf-8').split('\n')]
    return lines


def main():
    i = 0
    html = get_html(link)
    while i < len(html) and not html[i].endswith('<section id="listings" class="list ">'):  # HEAD LEFT
        i += 1

    while i < len(html) and html[i] != '<button class="btn-advisory hide">Liên hệ tư vấn</button>':  # RIGHT TAIL
        if html[i].startswith('<article class="media ">'):  # extract atributes from lk to rk
            data = {}
            i += 1
            count = 0
            small_element = ['type', 'location', 'transmission', 'build']
            while i < len(html) and html[i] != '<hr class="dotted-line">':
                if '<h3 class="list-info-title">' == html[i]:
                    data['title'] = html[i + 1]
                elif '<small' in html[i]:
                    data[small_element[count]] = html[i].replace('<small>', '').replace('</small>', '')
                    count += 1
                elif 'class="list-price-number"' in html[i]:
                    data['price'] = html[i + 1]
                i += 1
            HLRT.append(data)  # save data
        else:
            i += 1
    print(HLRT)


if __name__ == '__main__':
    main()
