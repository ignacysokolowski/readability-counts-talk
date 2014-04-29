==========================
Methods order: bad example
==========================

.. rst-class:: bad

::

  class XMLParser(object):

      def _find_timestamp(self, xml):
          return xml.xpath('./Timestamp/text()')

      def _find_signature(self, xml):
          return xml.xpath('./Signature/text()')

      @classmethod
      def from_config(cls, config):
          return cls(config['developer'], config['app'], config['certificate'])

      def _calculate_signature(self, timestamp):
          sig = ''.join([timestamp, self.developer, self.app, self.certificate])
          md5sig = hashlib.md5(sig.encode()).digest()
          b64sig = base64.b64encode(md5sig).decode()
          return b64sig

      def __init__(self, developer, app, certificate):
          self.developer = developer
          self.app = app
          self.certificate = certificate

      def validate_signature(self, xml):
          xml_sig = self._find_signature(xml)
          timestamp = self._find_timestamp(xml)
          valid_sig = self._calculate_signature(timestamp)
          if xml_sig != valid_sig:
              raise SignatureError('XML signature is invalid.')

* I don't know what the ``_find_timestamp()`` is used for until I read the
  ``validate_signature`` method.
* Maybe after reading the ``validate_signature()`` I won't care about the
  implementation of finding the timestamp and signature.
* To find out how to instantiate, I have to skip some methods which I don't
  care about for now.
