import requests
import textwrap


with open('list_link_carmudi.txt') as f:
    list_link = f.readlines()
    for i in range(len(list_link)):
        list_link[i] = list_link[i].replace('\n', '')
    f.close()

# print(list_link)

page1 = requests.get(list_link[0])
page = [textwrap.dedent(line.rstrip()) for line in page1.content.decode('utf-8').split('\n')]
print(page)
# html = html.content.decode('utf-8').splitlines()

HLRT = []  # HLRT is void at the begining

i = 0
while i < len(page) and page[i] != "<hr>":  # skip first occurrece of head
    i += 1
while i < len(page) and page[i] != "</body>":  # l1 is before next tail
    if "<h3>" in page[i]:  # extract atributes from lk to rk
        LR = [page[i].replace("<h3>", "").replace("</h3>", "")]  # LR is void at the begining
        i += 1
        while i < len(page) and page[i] != "</div>":  # while end of rk
            if "<li>" in page[i]:
                li = page[i].split("</b>")
                LR.append(li[1].replace("</li>", ""))
            i += 1
        HLRT.append(LR)  # save tuples
    else:
        i += 1

print(HLRT)
