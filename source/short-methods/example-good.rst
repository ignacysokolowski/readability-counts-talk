===========================
Short methods: good example
===========================

::

  class XMLParser(object):

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

* Comment replaced by a method name.
* Each unit can be tested separately.
