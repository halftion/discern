import re
import scrapy
import util
from ScanningSpider.items import CVEItem
from ScanningSpider.items import CVEDetailItem

class CVEDetails(scrapy.Spider):
    name = "cve_detail"
    allowed_domains = ['cvedetails.com']
    base_url = 'https://www.cvedetails.com/vulnerability-list/year-'
    baer_detail_url = "https://www.cvedetails.com/"
    # start_urls = ['https://www.cvedetails.com/vulnerability-list/year-2019/vulnerabilities.html']

    #初始页面入口：
    def start_requests(self):
        for year in range(2019,1998,-1):
            url = self.base_url + str(year) + '/vulnerabilities.html'
            yield scrapy.Request(url,self.parseList)
    #分页入口：
    def parseList(self, response):
        num = int(response.xpath('//div[@id="pagingb"]/b/text()').get())
        #计算页码总数
        pages = num//50
        if num % 50 > 0:pages += 1
        #获取年份
        year = int(response.xpath('//div[@class="submenu"]/div/b/a/text()').get())
        url = "https://www.cvedetails.com" + response.xpath('//div[@id="pagingb"]/a')[0].xpath('./@href').get()
        for page in range(1,pages+1):
            #替换页码：
            sub_url = re.sub('page=1','page=' + str(page),url)
            yield scrapy.Request(sub_url,self.parseInfo)
    #分页处理：
    def parseInfo(self,response):
        for num in range(len(response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]'))):
            cve = CVEItem()
            cve['cve_id'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[1].xpath('./a/text()').get()
            cve['cve_url'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[1].xpath('./a/@href').get()
            cve['cwe_id'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[2].xpath('./a/text()').get()
            cve['exp'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[3].xpath('./b/text()').get().strip()
            cve['vulnerability_type'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[4].xpath('./text()').get().strip()
            cve['score'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[7].xpath('./div/text()').get()
            # 访问级别
            cve['gainedaccess_level'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[8].xpath('./text()').get()
            # 访问方式（远程、本地）
            cve['access'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[9].xpath('./text()').get()
            # 复杂度
            cve['complexity'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[10].xpath('./text()').get()
            # 认证系统
            cve['authentication'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[11].xpath('./text()').get()
            # 机密性
            cve['confidentiality'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[12].xpath('./text()').get()
            # 完整性
            cve['integrity'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[13].xpath('./text()').get()
            # 可用性
            cve['availability'] = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')[num].xpath('./td')[14].xpath('./text()').get()
            cve['description'] = response.xpath('//table[@id="vulnslisttable"]/tr/td[@class="cvesummarylong"]')[num].xpath('./text()').get().strip()
            yield cve
            # 这里的dont_filter是为了防止重复爬取
            url = self.baer_detail_url + cve['cve_url']
            yield scrapy.Request(url,self.parseDetail,meta={'cve_id':cve['cve_id']},dont_filter=True)

    def parseDetail(self,response):
        cve_id = response.meta['cve_id']
        for num in range(1,len(response.xpath('//table[@id="vulnprodstable"]/tr'))):
            detail = CVEDetailItem()
            detail['cve_id'] = cve_id
            detail['product_type'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[1].xpath('./text()').get().strip()
            detail['vendor'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[2].xpath('./a/text()').get().strip()
            detail['product'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[3].xpath('./a/text()').get().strip()
            detail['version'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[4].xpath('./text()').get().strip()
            detail['update'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[5].xpath('./text()').get().strip()
            detail['edition'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[6].xpath('./text()').get().strip()
            detail['language'] = response.xpath('//table[@id="vulnprodstable"]/tr')[num].xpath('./td')[7].xpath('./text()').get().strip()
            yield detail