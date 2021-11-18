import base64


class Base64Conversion:

    @staticmethod
    def base64_decode(item, extension=None):
        base64_bytes = item.encode('utf-8')
        if extension == 'pdf':
            return base64.decodebytes(base64_bytes)
        decoded_data = base64.b64decode(base64_bytes)
        return decoded_data.decode('utf-8')
