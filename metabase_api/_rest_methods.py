import requests 

class InvalidResponse(Exception):
    """Exception raised for invalid responses."""
    pass

def get(self, endpoint, *args, **kwargs):
    try:
        self.validate_session()
        res = requests.get(self.domain + endpoint, headers=self.header, **kwargs, auth=self.auth)
        if 'raw' in args:
            return res
        else:
            if not res.ok:
                raise InvalidResponse("GET request failed with status code: {}".format(res.status_code))
            return res.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def post(self, endpoint, *args, **kwargs):
    try:
        self.validate_session()
        res = requests.post(self.domain + endpoint, headers=self.header, **kwargs, auth=self.auth)
        if 'raw' in args:
            return res
        else:
            if not res.ok:
                raise InvalidResponse("POST request failed with status code: {}".format(res.status_code))
            return res.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def put(self, endpoint, params, *args, **kwargs):
    try:
        """Used for updating objects (cards, dashboards, ...)"""
        self.validate_session()
        res = requests.put(self.domain + endpoint, headers=self.header, json=params, **kwargs, auth=self.auth)
        if 'raw' in args:
            return res
        else:
            if res.status_code != 200:
                raise InvalidResponse("PUT request failed with status code: {}".format(res.status_code))
            return res.status_code
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def delete(self, endpoint, params, *args, **kwargs):
    try:
        self.validate_session()
        res = requests.delete(self.domain + endpoint, headers=self.header, params=params, **kwargs, auth=self.auth)
        if 'raw' in args:
            return res
        else:
            if res.status_code != 200 and res.status_code != 204:
                raise InvalidResponse("DELETE request failed with status code: {}".format(res.status_code))
            return res.status_code
    except Exception as e:
        print(f"An error occurred: {e}")
        return None