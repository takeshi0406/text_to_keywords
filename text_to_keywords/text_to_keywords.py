import xmlrpc.client


class client:

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy("http://d.hatena.ne.jp/xmlrpc")

    def parse_text(self, text, score=0, cname=[]):
        config = self._make_config(text, score, cname)
        keywords = self.server.hatena.setKeywordLink(config)
        return keywords.get('wordlist')

    def _make_config(self, text, score, cname):
        return {'body': text, 'mode': 'lite', 'score': score, 'cname': cname}
