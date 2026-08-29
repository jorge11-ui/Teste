                      Listas de coisas para aprender

1-Blender
2-Gimp(2d)
3-Git e github
4-Figma 
5-Notion, obsidian
6-Escrita 
7-Sketching
8-Fotografia 
9-Da vinci resolve
10-origami

# Comandos importantes do Neovim

## Edição
- `diw` - apaga a palavra inteira
- `ci"` / `ci(` - apaga e entra em insert dentro de "..." ou (...)
- `dtx` / `dfx` - apaga até (sem/sem incluir) x
- `yy`/`dd` + `p`/`P` - copiar/apagar linha e colar
- `>>` / `<<` - indentar/desindentar linha

## Navegação
- `gg` / `G` - início/fim do ficheiro
- `{` / `}` - por parágrafo
- `%` - saltar entre parênteses correspondentes
- `w` / `b` / `e` - por palavra
- `Ctrl+d` / `Ctrl+u` - meia página para baixo/cima

## Visual mode
- `V` (linha), `v` (caracteres), `Ctrl+v` (colunas)
- `Ctrl+v` -> selecionar -> `I` -> texto -> `Esc` (escrever em várias linhas)

## Buffers / janelas
- `:ls` - listar buffers | `:bd` - fechar buffer
- `Ctrl+w` + `s`/`v` - dividir janela
- `Ctrl+w` + `hjkl` - mover entre janelas
- `:tabnew` / `gt` / `gT` - separadores

## Procura / substituição
- `/palavra` -> `n` / `N` para navegar
- `:%s/velho/novo/g` - substituir tudo
- `:%s/velho/novo/gc` - com confirmação

## Poderosos
- `u` desfaz / `Ctrl+r` refaz
- `.` repete o último comando de edição
- `q` regista macros (`qa`, executa com `@a`)

