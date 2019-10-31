import logging

class JsonComparator:

    def __init__(self):
        pass

    def equals(self,live_json,std_json):

        logging.info("live_json  "+str(live_json))
        logging.info("std_json  " + str(std_json))

        return live_json == std_json

    def less_than(self,live_json,std_json):
        pass

    def more_than(self,live_json,std_json):
        pass

if __name__ == "__main__":
    jsonComparator = JsonComparator()
    a = {'errcode': 0, 'errmsg': 'created'}
    b = {'errcode': '0', 'errmsg': 'Created10'}
    c = jsonComparator.equals(a,b)
    print(c)