# NheengataggerDisambiguator
### Pacote Python para desambiguar sentenças em nheengatu etiquetadas automaticamente pelo Nheengatagger.

Corpus utilizado disponível em: https://github.com/juliana-gurgel/nheengatu/tree/main/corpus

Nheengatagger disponível em: https://github.com/CompLin/nheengatu/tree/main/src

Autores: 
Juliana Lopes Gurgel <julianagurgel@letras.ufc.br>; Victor Pereira do Nascimento Santos <victor_santos@fisica.ufc.br>.


## Instalação

Criar ambiente virtual:
```
python -m venv <path-of-venv>
```

Ativar ambiente virtual:
```
source <path-of-venv>
```

Clonar repositório:
```
git clone <url> <path-of-project>
```

Instalar pacote a partir do diretório:
```
python -m pip install -e <path-of-project>
```

## Utilização

Ative o ambiente virtual:
```
source <path-of-venv>/bin/activate
```

Para iniciar, execute o comando:
```
desambiguador
```

Para gerar a tabela de contexto a partir de um corpus etiquetado pelo Nheengatagger:
```
desambiguador [--log-level=<log-level>] contexto <path-of-corpus> <path-of-tagset> --out <path-of-contexto>
```
Para desambiguar um conjunto de arquivos em um diretório:
```
desambiguador [--log-level=<log-level>] corpus <path-of-corpus> --contexto <path-of-contexto>
```
Para desambiguar uma sentença:
```
desambiguador [--log-level=<log-level>] sentenca <sentenca> --contexto <path-of-contexto>
```
Informações:
```
desambiguador (--h | --help)
desambiguador (--v | --version)
```
Exemplos de uso:
```
# Para gerar a tabela de contexto a partir de um corpus etiquetado pelo Nheengatagger:
desambiguador --log-level=DEBUG contexto /home/user/Documents/desambiguador-nheengatu/data/navarro-2016/ /home/user/Documents/desambiguador-nheengatu/data/tagset.xlsx --out /home/user/Documents/desambiguador-nheengatu/data/contexto.csv

# Para desambiguar um conjunto de arquivos em um diretório:
desambiguador --log-level=DEBUG corpus /home/user/Documents/desambiguador-nheengatu/data/corpus --frequencia /home/user/Documents/desambiguador-nheengatu/data/contexto.csv

# Para desambiguar uma sentença:
desambiguador sentenca 'Ara/N puranga/A+ADV !/PUNCT' --contexto /home/user/Documents/desambiguador-nheengatu/data/contexto.csv
```
Os comandos ficam salvos em um arquivo de histórico, usualmente no diretório raiz do usuário (`$HOME`)

Para exibir histórico pela linha de comando:
```
history
```
Utilize o atalho `CTRL+r` para pesquisar um comando específico no histórico por meio de uma palavra:
```
(reverse-i-search)`': palavra
```
