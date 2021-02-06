# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CVEItem(scrapy.Item):
    cve_id = scrapy.Field()
    cve_url = scrapy.Field()
    cwe_id = scrapy.Field()
    exp = scrapy.Field()
    vulnerability_type = scrapy.Field()
    score = scrapy.Field()
    # 访问级别
    gainedaccess_level = scrapy.Field()
    # 访问方式（远程、本地）
    access = scrapy.Field()
    # 复杂度
    complexity = scrapy.Field()
    # 认证系统
    authentication = scrapy.Field()
    # 机密性
    confidentiality = scrapy.Field()
    # 完整性
    integrity = scrapy.Field()
    # 可用性
    availability = scrapy.Field()
    # 描述
    description = scrapy.Field()

class CVEDetailItem(scrapy.Item):
    cve_id = scrapy.Field()
    product_type = scrapy.Field()
    vendor = scrapy.Field()
    product = scrapy.Field()
    version = scrapy.Field()
    update = scrapy.Field()
    # 版本
    edition = scrapy.Field()
    language = scrapy.Field()


class ScanningspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
