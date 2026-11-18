# API de Chamados de Suporte

---

**Nome completo:** Felipe Pereira de Souza Silva

## Objetivo do projeto
Esta API foi desenvolvida em **Flask** com o objetivo de gerenciar o fluxo de chamados de suporte técnico. Ela permite o cadastro, consulta e controle de tickets de atendimento, garantindo respostas estruturadas em formato JSON e validações robustas, com foco em boas práticas de desenvolvimento e testes automatizados.

## Como instalar as dependências
O projeto utiliza o **`uv`** como package manager e ambientes virtuais. Para instalar todas as dependências (incluindo as de desenvolvimento e testes) de forma determinística utilizando o .lock file, execute o comando abaixo na raiz do projeto:

```bash
uv sync --locked
```

*Nota: Esse comando criará automaticamente o ambiente virtual (`.venv`) e instalará exatamente as versões especificadas no arquivo `uv.lock`.*

## Como executar a aplicação
Com as dependências instaladas e o ambiente virtual configurado pelo `uv`, execute o servidor de desenvolvimento da API:

```bash
uv run python app.py
```

O servidor será iniciado localmente (geralmente em http://127.0.0.1:5000 ou http://localhost:5000).

## Como acessar a rota inicial e resposta esperada
Para verificar se a API está funcionando corretamente, você pode acessar a rota raiz (`/`) utilizando o navegador, o `curl` ou um cliente HTTP (como Apidog, Insomnia ou Postman).

* **URL de acesso:** `http://127.0.0.1:5000/ ou http://localhost:5000/
* **Método HTTP:** `GET`
* **Resposta esperada (Status Code `200 OK` e `Content-Type: application/json`):**

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```
