import pandas as pd
import os
import sys

from scraping.web_scraping import scraper, transformer, writer, reader

# logging.basicConfig(level=logging.DEBUG)


URL = "https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia"
DB_NAME = "web_scraping_db"
DB_USER = "username"
DB_PASSWORD = "secret"
DB_HOST = "db"
DB_PORT = "5432"
CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
TABLE_NAME = "orang_terkaya_indonesia"


def main() -> None:
    dfs = scraper.scrape(URL)
    
    # logging.debug(f"List orang terkaya 2011-2020 ...")
    # for i, df in enumerate(dfs):
    #     if i>=3 and i<=7:
    #         logging.debug(f'\n{df.head()}')

    store_df = transformer.transform([dfs[3], dfs[4], dfs[5], dfs[6], dfs[7]], [2011, 2013, 2017, 2019, 2020])
    writer.write_to_postgres(df=store_df, db_name=DB_NAME, table_name=TABLE_NAME, connection_string=CONNECTION_STRING)
    result_df = reader.read_from_postgres(db_name=DB_NAME, table_name=TABLE_NAME, connection_string=CONNECTION_STRING)
    
    print("Daftar Orang Terkaya di Indonesia:")
    print(result_df.to_string())


if __name__ == "__main__":
    main()