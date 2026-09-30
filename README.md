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
│   ├── script.js         # Animações de entrada, menu mobile e ano do rodapé
│   ├── hero-network.svg  # Arte do hero (conexões digitais)
│   ├── bbg-logo.webp     # Logo oficial (512×512)
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

| Âncora               | Conteúdo                                      |
| -------------------- | --------------------------------------------- |
| `#inicio`            | Hero com a proposta principal da BBG          |
| `#sobre`             | Origem da empresa                             |
| `#desafios`          | Problemas que a BBG ajuda a resolver          |
| `#solucoes`          | Sistemas, automação e soluções empresariais   |
| `#diferenciais`      | Por que escolher a BBG                        |
| `#como-trabalhamos`  | Processo de trabalho em três etapas           |
| `#contato`           | Chamada para contato                          |

### Acessibilidade

- Link "Pular para o conteúdo" para navegação por teclado
- Marcação semântica com `aria-label` e `aria-labelledby`
- Menu mobile que fecha com `Esc`
- Animações desativadas para quem usa `prefers-reduced-motion`

## Pendências

- [ ] **Canais de contato:** incluir WhatsApp, e-mail e/ou redes sociais na seção `#contato`.
- [ ] **Imagem de compartilhamento:** adicionar a meta tag `og:image` para a prévia do link em redes sociais e no WhatsApp.

---

© BBG Empreendimentos
