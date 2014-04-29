==========================
Short methods: bad example
==========================

.. rst-class:: bad

::

  class XMLParser(object):

      def validate_signature(self, xml):
          xml_sig = xml.xpath('./Signature/text()')
          timestamp = xml.xpath('./Timestamp/text()')

          # Calculate valid signature.
          sig = ''.join([timestamp, self.developer, self.app, self.certificate])
          md5sig = hashlib.md5(sig.encode()).digest()
          b64sig = base64.b64encode(md5sig).decode()

          if xml_sig != b64sig:
              raise SignatureError('XML signature is invalid.')

* How to test finding the ``xml_sig`` and ``timestamp``?
* How to test calculating the valid signature?
