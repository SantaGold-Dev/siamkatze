# Siamkatze

O Siamkatze é um script em Python projetado para encontrar e gerenciar links simbólicos quebrados num diretório especificado.

## Recursos

- **Encontrar Links Simbólicos Quebrados**: O principal recurso do Siamkatze é identificar e relatar links simbólicos quebrados dentro do diretório fornecido.

- **Busca Recursiva**: O Siamkatze oferece uma opção para realizar uma busca recursiva, permitindo analisar subdiretórios em busca de links simbólicos quebrados.

- **Excluir Links Quebrados**: Para maior conveniência, o Siamkatze inclui uma opção para excluir os links simbólicos quebrados identificados.

## Uso

```bash
python siamkatze.py [-r] [-d] [-v] directory_path
```

### Argumentos

- `directory_path`: O caminho para o diretório onde o Siamkatze começará a procurar por links simbólicos quebrados.

### Opções

- `-r, --recursive`: Ative a busca recursiva para encontrar links simbólicos quebrados em subdiretórios.

- `-d, --delete`: Ative esta opção para excluir os links simbólicos quebrados encontrados.

- `-v, --verbose`: Ative o modo detalhado para exibir informações adicionais.

## Exemplo

Para encontrar e listar links simbólicos quebrados no diretório atual, execute:

```bash
python siamkatze.py .
```

Para realizar uma busca recursiva e excluir os links simbólicos quebrados:

```bash
python siamkatze.py -r -d /caminho/para/diretorio
```

## Licença

Este projeto está licenciado sob a [Licença MIT](../LICENSE).

## Contribuições

Contribuições são bem-vindas! Por favor, verifique as [diretrizes de contribuição](CONTRIBUTING_pt-BR.md) antes de fazer contribuições.

## Problemas

Se você encontrar algum problema ou tiver sugestões, por favor [abra uma issue](https://github.com/yourusername/siamkatze/issues).