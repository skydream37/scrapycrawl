# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class OutercrawlPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('outerdata.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists outerdata(store varchar(20), current_time datetime,\
         name varchar(100), price varchar(20), link varchar(100),fee varchar(20), sell varchar(20))')
        # pass

    def close_apider(self, spider):
        self.conn.commit()
        self.conn.close()
        # pass

    def process_item(self, item, spider):
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into outerdata({}) values({})'
        self.cur.execute(sql.format(col, placeholders), item.values())
        return item
