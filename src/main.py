import xml.etree.ElementTree as ET
import datetime

class SitemapGenerator:
    def __init__(self, sitemap_path, fixed_lastmod='2023-11-02T20:00:00+00:00'):
        self.sitemap_path = sitemap_path
        self.fixed_lastmod = fixed_lastmod
        self.url_list = []

    def create_url(self, loc, lastmod=None, priority=0.8):
        if lastmod is None:
            lastmod = self.fixed_lastmod
        return {
            'loc': loc,
            'lastmod': str(lastmod),
            'priority': str(priority)
        }

    def add_static_urls(self):
        self.url_list.append(self.create_url('https://yoursite.az/', priority=1))
        self.url_list.append(self.create_url('https://yoursite.az/about-us/'))

    def add_dynamic_urls(self, dataset):
        for data in dataset:
            publish_date = data['created_date'].strftime("%Y-%m-%dT%H:%M:%S+00:00")
            loc = data['url']
            url = self.create_url(loc, lastmod=publish_date)
            self.url_list.append(url)

    def generate_sitemap(self):
        root = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
        for url_data in self.url_list:
            url_element = ET.Element('url')

            loc_element = ET.Element('loc')
            loc_element.text = url_data['loc']
            url_element.append(loc_element)

            lastmod_element = ET.Element('lastmod')
            lastmod_element.text = url_data['lastmod']
            url_element.append(lastmod_element)

            priority_element = ET.Element('priority')
            priority_element.text = url_data['priority']
            url_element.append(priority_element)

            root.append(url_element)

        tree = ET.ElementTree(root)
        with open(self.sitemap_path, 'wb') as xml_file:
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)

def main():
    sitemap_xml_path = '/yourpath/sitemap.xml'
    fixed_lastmod = '2023-11-02T20:00:00+00:00'

    sitemap = SitemapGenerator(sitemap_xml_path, fixed_lastmod)

    dataset = YourModel.objects.all()

    sitemap.add_static_urls()
    sitemap.add_dynamic_urls(dataset)
    sitemap.generate_sitemap()

if __name__ == "__main__":
    main()
