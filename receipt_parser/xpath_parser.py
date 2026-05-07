from lxml import html

def parse_email_receipt(html_content):
    tree = html.fromstring(html_content)

    store = tree.xpath('//h1/text()')

    total = tree.xpath('//span[@class="total"]/text()')

    return {
        "store": store[0] if store else "Unknown",
        "total": total[0] if total else None
    }