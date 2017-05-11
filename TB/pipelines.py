# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class TbPipeline(object):
    def __init__(self):
        import csv
        import time
        timestamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        path = "./results"
        if not os.path.exists(path):
            os.makedirs(path)
        self.file = open(f'{path}/result.{timestamp}.csv', 'w', encoding='utf_8_sig', newline="")
        self.writer = csv.writer(self.file, delimiter=',', dialect=csv.excel, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        self.writer.writerow(['item_id', 'item_name', 'trade', 'comments'])

    def process_item(self, item, spider):
        tmp = [item["item_id"], item["item_name"], item["trade"], item["comments"]]
        self.writer.writerow(tmp)
        return item

    def __del__(self):
        self.file.close()

        # 613474254104
