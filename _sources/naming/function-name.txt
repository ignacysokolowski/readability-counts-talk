=================================
Naming conventions: function name
=================================

Function and method name should start with a verb, suggestive on the action.

.. container:: twocol

    .. container:: leftside

        **BAD:**

        .. rst-class:: bad

        .. code-block:: python
            :emphasize-lines: 6

            class JSONFile(object):

                def __init__(self, path):
                    self.path = path

                def content(self):
                    with open(self.path) as f:
                        raw_content = f.read()
                    content = json.loads(raw_content)
                    return content

            json_file = JSONFile('./data.json')
            # User expects 'content` to be an attribute.
            if json_file.content:
                title = json_file.content['title']
                body = json_file.content['body']

    .. container:: rightside

        **GOOD**:

        .. code-block:: python
            :emphasize-lines: 6

            class JSONFile(object):

                def __init__(self, path):
                    self.path = path

                def read(self):
                    with open(self.path) as f:
                        raw_content = f.read()
                    content = json.loads(raw_content)
                    return content

            json_file = JSONFile('./data.json')
            content = json_file.read()
            if content:
                title = content['title']
                body = content['body']
