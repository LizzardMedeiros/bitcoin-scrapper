#Bitcoin Scrapper Python

### O projeto

Uma simples aplicação que compara o marketcap das principais moedas _fiat_ do mundo com o marketcap do Bitcoin, além de prover algumas estatísticas úteis

## Requerimentos (libs)

> - parsel
> - requests

## Como rodar

> - Rode o arquivo `analysis.py` - `python3 -i analysis.py`
> - Use os métodos implementados

## Métodos implementados

> - **btc_can_rises()** - Estima quanto a capitalização do Bitcoin precisa aumentar (ou diminuir) para atingir o nível de capitalização das moedas _fiat_ no mundo

## Docker

### Instalação com Docker

- Crie uma conta no [Docker HUB](https://hub.docker.com/)
- Instale o [Docker](https://www.docker.com/products/docker-desktop)
- Rode o comando `docker build . -t bitcoin-scrapper`

### Desistalando container

- Rode o comando `docker rm bitcoin-scrapper`

### Para rodar o container:
``` bash
 $ docker run -it --name=btc-scrapper -v $PWD/src:/btc_scrapper/src bitcoin-scrapper bash
```