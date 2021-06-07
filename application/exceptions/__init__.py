class BadRequestBody(Exception):
    """
    Bad request exception to be raise that allows you to create a custom message.

    If you add the argument 'message' you may pass a string with
    placeholder brackets that can be filled with given args
    """
    def __init__(self, message=None, **kwargs):
        self._message = message
        self._kwargs = kwargs

    @property
    def message(self):
        return self.create_message()
    
    def create_message(self):
        if not self._message:
            ret = self.__class__.__name__
        else:
            ret = self._message
        
        notes = []
        for k in self._kwargs:
            v = repr(self._kwargs[k])
            note = ' {}={}'.format(k, v)
            notes.append(note)
        
        if notes:
            ret += ','.join(notes)

        return ret
    
    def __str__(self):
        return self.create_message()
