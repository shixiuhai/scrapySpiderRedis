env="dev"
if env == "dev":
   from scrapySpiderRedis.dev_settings import *
elif env == "prod":
   from scrapySpiderRedis.prod_settings import *
   