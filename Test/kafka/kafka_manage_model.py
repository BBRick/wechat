# -.- coding:utf-8 -.-
"""
Created on 2016年7月28日

@author: kerry
"""
import json
#from tools.base.mlog import mlog
from kafka import KafkaConsumer,KafkaProducer
from collections import Iterable

class KafkaProducerManager(object):

    def __init__(self, client, host, coname):
        self.client = client
        self.host = host
        self.coname = coname
	print 'connect write '
        self.producer = KafkaProducer(bootstrap_servers=self.host)

    def __del__(self):
        self.producer.close()

    def push_data(self, parmas_message):
	print 'write message'
        producer = self.producer
        producer.send(self.coname, parmas_message.encode('utf-8'))
        producer.flush()
	print 'write done'



class KafkaConsumerManager(object):
    """
    kafka管理
    """

    def __init__(self, client, host, coname):
        # threading.Thread.__init__(self, name='kafka_manage')
        self.client = client
        self.host = host
        self.coname = coname
        # self.setDaemon(True)
        # self.start()

    def __del__(self):
        pass

    def set_callback(self, callback):
        self.callback = callback

#    def process_data(self, data):
#        name = data['key_name'] + data['pos_name'] + '.txt'
#        ftp_url = '~/text_storage/' + data['key_name'] + '/' + data['pos_name']
        # ftp_manager_t.download(str(name), (ftp_url))

    def run(self):
        """
        连接取数据
        """
        while True:
	    print 'read connect', self.host, self.coname
            consumer =  KafkaConsumer(bootstrap_servers=self.host)
            consumer.subscribe([self.coname])
	    print isinstance(consumer, Iterable)
            for message in consumer:
                try:
                    print message
           #         json_info = json.loads(message[6])
                    self.callback(message[6])
                except Exception, e:
                    print e
 #                   mlog.log().error(e)
