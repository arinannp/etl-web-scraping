# ETL Scraping Data From Web and Stored to Postgres Database

## Web Scraping 
- url:  ```https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia```

## Requirements
- Docker

## How to Run
- build docker image dengan command  `docker-compose -f docker-compose.yml build`
- jalankan aplikasi dengan command  `docker-compose -f docker-compose.yml up`
- matikan aplikasi dengan command  `docker-compose -f docker-compose.yml down`

## Sample Output
#### Year - 2011
![Sample Output](./images/output-2011.png)
#### Year - 2013
![Sample Output](./images/output-2013.png)
#### Year - 2017
![Sample Output](./images/output-2017.png)
#### Year - 2019
![Sample Output](./images/output-2019.png)
#### Year - 2020
![Sample Output](./images/output-2020.png)
