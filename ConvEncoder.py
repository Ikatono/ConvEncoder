import numpy as np

class ConvEncoder:
    #code is an array representing the code
    #punctures where puncture is true
    #code and puncture must have the same height
    #if stream == False the encoder will flush after every call to feed()
    #
    def __init__(self, code, feedback=False, puncture=None, stream=True, block=2000):
        validcode = False
        self.code = np.array(code, dtype=np.bool_)
        self.feedback = feedback
        if puncture is not None:
            self.puncture = np.array(puncture, dtype=np.bool_)
            if self.node.shape[0] != self.puncture.shape[0]:
                raise ValueError('code and feedback must have the same number of rows.')
        if not isinstance(stream, bool):
            raise TypeError('stream must be a boolean (received %s)' % str(type(stream)))
        self.stream = stream
    
    def feed(data):
        data = np.array(data, dtype=np.bool_)
        