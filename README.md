# BBG Empreendimentos — Landing Page

Landing page institucional da **BBG Empreendimentos**, empresa que desenvolve sistemas e soluções empresariais de tecnologia.

Site estático, feito com HTML, CSS e JavaScript puros: sem framework, sem dependências e sem etapa de build.

## Sumário

- [Tecnologias](#tecnologias)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Rodando localmente](#rodando-localmente)
- [Deploy no Netlify](#deploy-no-netlify)
- [Identidade visual](#identidade-visual)
- [Seções da página](#seções-da-página)
- [Adicionando um case](#adicionando-um-case)
- [Adicionando um cliente](#adicionando-um-cliente)
- [Pendências](#pendências)

## Tecnologias

| Camada     | Tecnologia                                                |
| ---------- | --------------------------------------------------------- |
| Estrutura  | HTML5 semântico                                           |
| Estilo     | CSS3 puro (`public/styles.css`)                           |
| Interação  | JavaScript vanilla (`public/script.js`)                   |
| Fontes     | [Google Fonts](https://fonts.google.com): Space Grotesk e Inter |
| Hospedagem | [Netlify](https://www.netlify.com)                        |

## Estrutura do projeto

```
bbg-landing-page/
├── public/               # Tudo o que é publicado no site
│   ├── index.html        # Página única da landing page
│   ├── styles.css        # Estilos, layout responsivo e animações
│   ├── script.js         # Animações de entrada, abas dos cases, menu mobile e ano do rodapé
│   ├── og-image.jpg      # Prévia do link nas redes (1200×630)
│   ├── bbg-perfil-verde.webp # Símbolo em fundo verde (seção de contato)
│   ├── clientes/         # Logos dos clientes (.webp com fundo transparente)
│   ├── projetos/         # Telas dos projetos desenvolvidos (.webp)
│   ├── bbg-logo.webp     # Logo oficial (512×512)
│   ├── bbg-logo-mark.webp # Símbolo com fundo transparente (menu e rodapé)
│   ├── hero-earth.webp   # Textura da Terra do hero (NASA Blue Marble, domínio público)
│   ├── hero-earth-sm.webp # Versão menor da textura, usada no celular
│   └── favicon.png       # Ícone da aba (192×192)
├── ideas.md              # Direção visual e decisões de design
├── netlify.toml          # Configuração de deploy do Netlify
└── README.md
```

## Rodando localmente

Como não há build, basta servir a pasta `public` com qualquer servidor estático:

```bash
# Com Python
python3 -m http.server 8080 -d public

# Ou com Node.js
npx serve public
```

Depois, abra <http://localhost:8080> (ou a porta indicada pelo `serve`).

> **Atenção:** não abra o `index.html` direto pelo navegador (`file://`). Os caminhos dos arquivos começam com `/` e só funcionam quando servidos por HTTP.

## Deploy no Netlify

O deploy é contínuo: todo `git push` na branch `main` publica o site automaticamente.

### Primeira configuração

1. No [Netlify](https://app.netlify.com), clique em **Add new site → Import an existing project**.
2. Conecte o GitHub e selecione o repositório `bbgempreendimentos/bbg-landing-page`.
3. Não é preciso configurar nada: o `netlify.toml` já define a pasta publicada.
4. Clique em **Deploy**.

```toml
# netlify.toml
[build]
  publish = "public"
```

### Domínio próprio

Em **Site configuration → Domain management**, adicione o domínio e siga as instruções de DNS. O certificado HTTPS é emitido automaticamente.

## Identidade visual

| Elemento          | Valor                                  |
| ----------------- | -------------------------------------- |
| Cor principal     | Azul-marinho `#0A1628`                 |
| Cor de destaque   | Verde-esmeralda `#22C58B`              |
| Títulos           | Space Grotesk                          |
| Textos e interface| Inter                                  |

Mais detalhes sobre a direção criativa estão em [`ideas.md`](ideas.md).

## Seções da página

A página segue a direção "relatório impresso": um eixo vertical em 42% da largura organiza títulos e textos, e as seções alternam entre páginas de texto e campos inteiros de cor.

| Âncora               | Conteúdo                                                        |
| -------------------- | --------------------------------------------------------------- |
| `#inicio`            | Hero com a Terra e o título "Talento não depende de CEP."       |
| `#projetos`          | Projetos e cases de sucesso (desafio, entrega, situação) e clientes |
| `#sobre`             | Origem da BBG, com o símbolo como capitular                     |
| `#solucoes`          | O que fazemos, em campo verde com o título fixo                 |
| `#como-trabalhamos`  | Processo como uma barra de progresso ampliada                   |
| `#contato`           | Chamada para contato                                            |

### Acessibilidade

- Link "Pular para o conteúdo" para navegação por teclado
- Marcação semântica com `aria-label` e `aria-labelledby`
- Menu mobile que fecha com `Esc`
- Animações desativadas para quem usa `prefers-reduced-motion`; sem JavaScript, todo o conteúdo aparece

## Adicionando um case

1. Salve as telas em `public/projetos/` (`.webp`, de preferência com 1400–1600 px de largura).
2. Em `public/index.html`, copie um bloco `<article class="case">` dentro de `#projetos` e cole antes de `<div class="shell clients">`.
3. Troque título, descrição e os três itens de `case-facts` (**O desafio**, **O que entregamos**, **Situação**). Use só fatos confirmados com o cliente.
4. Para ter abas com várias telas, use a estrutura do case da Gestão Documental (`project-gallery` + botões `data-view`). As imagens extras usam `data-src` e só carregam no clique.

## Adicionando um cliente

Em `<ul class="client-row">`, copie um `<li class="client-tile">` e cole antes do item "O próximo case pode ser o seu". O logo aparece sobre fundo branco, então `.png`/`.webp` com fundo transparente ou branco funcionam.

## Checagem de design

A página foi conferida com a skill `design-taste-frontend` (pasta `.taste-skill/`, ignorada no git):

```bash
python3 -m http.server 8080 -d public &
node ~/.claude/skills/design-taste-frontend/scripts/lint.mjs public
node ~/.claude/skills/design-taste-frontend/scripts/inspect.mjs http://localhost:8080/ --allow gradient
```

O `--allow gradient` existe por causa da Terra e das estrelas do hero, que são desenhadas com gradientes.

## Pendências

- [ ] **Canais de contato:** incluir WhatsApp, e-mail e/ou redes sociais na seção `#contato`.
- [x] **Imagem de compartilhamento:** `og:image` aponta para `public/og-image.jpg` (gerada de `branding/meta-bm/og-compartilhamento.png`).

---

© BBG Empreendimentos
