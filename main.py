from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from apscheduler.schedulers.background import BlockingScheduler

import multiprocessing

scheduler = BlockingScheduler()


def release_spiders():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    for spider in runner.spider_loader.list():
        runner.crawl(spider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


@scheduler.scheduled_job('cron', hour=3, minute=53, id="daily_crawl")
def run():
    process = multiprocessing.Process(target=release_spiders)
    process.start()


if __name__ == "__main__":
    scheduler.start()
