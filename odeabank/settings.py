BOT_NAME = 'odeabank'
SPIDER_MODULES = ['odeabank.spiders']
NEWSPIDER_MODULE = 'odeabank.spiders'
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'odeabank.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'
