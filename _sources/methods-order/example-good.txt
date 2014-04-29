===========================
Methods order: good example
===========================

::

  class XMLParser(object):

      def __init__(self, developer, app, certificate):
          self.developer = developer
          self.app = app
          self.certificate = certificate

      @classmethod
      def from_config(cls, config):
          return cls(config['developer'], config['app'], config['certificate'])

      def validate_signature(self, xml):
          xml_sig = self._find_signature(xml)
          timestamp = self._find_timestamp(xml)
          valid_sig = self._calculate_signature(timestamp)
          if xml_sig != valid_sig:
              raise SignatureError('XML signature is invalid.')

      def _find_signature(self, xml):
          return xml.xpath('./Signature/text()')

      def _find_timestamp(self, xml):
          return xml.xpath('./Timestamp/text()')

      def _calculate_signature(self, timestamp):
          sig = ''.join([timestamp, self.developer, self.app, self.certificate])
          md5sig = hashlib.md5(sig.encode()).digest()
          b64sig = base64.b64encode(md5sig).decode()
          return b64sig

* I can immediately see how to instantiate.  Oh, and there's an alternative
  constructor.
* Public method is what I'll probably use.  For now I don't care about the
  helpers.
* When reading the public method, I see the flow but I don't have to know
  the implementation of each step.
* If I'm interested in how the signature is calculated, I can go to the helper
  method below.  And I can test it without parsing the XML.
