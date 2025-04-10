# 📝 API - Gerenciador de Tarefas com Flask + MongoDB

Uma API RESTful para gerenciamento de tarefas pessoais (To‑Do List), com autenticação via JWT. Cada usuário pode criar, visualizar, atualizar e excluir suas próprias tarefas.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**
- **Flask**: Framework para criação de APIs.
- **MongoDB + PyMongo**: Banco de dados NoSQL.
- **Pydantic**: Validação de dados.
- **JWT (JSON Web Token)**: Autenticação.
- **Docker + Docker Compose**: Contêineres para a aplicação e banco de dados.
- **Postman**: Testes de API.

---

## 🔧 Instalação Local

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd flask_todo_api
```

### 2. Configure o Ambiente Virtual

# Crie o ambiente virtual

python -m venv venv

# Ative o ambiente virtual

# Linux/Mac

source venv/bin/activate

# Windows

venv\Scripts\activate

### 3. Instale as Dependências

```bash
pip install -r [requirements.txt](http://_vscodecontentref_/1)
```

### 4. Configure as Variáveis de Ambiente

# Exemplo de .env:

```bash
MONGO_URI_DEV=mongodb://localhost:27017/todo_db
SECRET_KEY=123abc456
```

Aqui está o código completo do README.md formatado em Markdown para que você possa copiar e colar diretamente:

````markdown
# 📝 API - Gerenciador de Tarefas com Flask + MongoDB

Uma API RESTful para gerenciamento de tarefas pessoais (To‑Do List), com autenticação via JWT. Cada usuário pode criar, visualizar, atualizar e excluir suas próprias tarefas.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**
- **Flask**: Framework para criação de APIs.
- **MongoDB + PyMongo**: Banco de dados NoSQL.
- **Pydantic**: Validação de dados.
- **JWT (JSON Web Token)**: Autenticação.
- **Docker + Docker Compose**: Contêineres para a aplicação e banco de dados.
- **Postman**: Testes de API.

---

## 🔧 Instalação Local

### 1. Clone o Repositório

```bash
git clone https://github.com/joaovicttorbm/flask_todo_api.git
cd flask_todo_api
```
````

### 2. Configure o Ambiente Virtual

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env` e edite as variáveis conforme necessário:

```bash
cp .env.example .env
```

Exemplo de `.env`:

```env
MONGO_HOST=mongo
MONGO_PORT=27017
MONGO_DB=todo_db
MONGO_URI_DEV=mongodb://localhost:27017/todo_db
SECRET_KEY=123abc456
```

### 5. Inicie o Servidor

```bash
python main.py
```

---

## 🐳 Usando Docker

### 1. Construa e Inicie os Contêineres

Certifique-se de que o Docker e o Docker Compose estão instalados. Em seguida, execute:

```bash
docker-compose up --build
```

### 2. Acesse a API

- A API estará disponível em: [http://localhost:5000](http://localhost:5000)
- O MongoDB estará disponível na porta `27017`.

---

## 📌 Endpoints da API

### 🔐 Autenticação

#### 🧾 Registrar Usuário

**POST** `/api/auth/register`

**Body**:

```json
{
  "username": "xxxxx",
  "email": "xxxxx@email.com",
  "password": "senha123"
}
```

**Resposta**:

```json
{
  "message": "User registered successfully"
}
```

---

#### 🔓 Login

**POST** `/api/auth/login`

**Body**:

```json
{
  "email": "xxxxx@email.com",
  "password": "senha123"
}
```

**Resposta**:

```json
{
  "message": "Login successful",
  "token": {
    "access_token": "xxxxxxxxx......"
  }
}
```

---

### 🧩 Tarefas (Protegidas)

Todas as rotas abaixo requerem autenticação com token JWT. Adicione o cabeçalho:

```
Authorization: Bearer <seu_token_jwt>
```

#### ➕ Criar Tarefa

**POST** `/api/tasks`

**Body**:

```json
{
  "title": "Estudar Flask",
  "description": "Praticar criação de API",
  "status": "in_progress"
}
```

**Resposta**:

```json
{
  "id": "64fb0..."
}
```

---

#### 📋 Listar Tarefas

**GET** `/api/tasks`

**Resposta**:

```json
[
  {
    "_id": "64fb0...",
    "title": "Estudar Flask",
    "description": "Praticar criação de API",
    "status": "pending",
    "owner_id": "xxxxx",
    "created_at": "2024-04-10T14:22:00"
  }
]
```

---

#### 🔍 Buscar Tarefa por ID

**GET** `/api/tasks/<task_id>`

**Resposta**:

```json
{
  "_id": "64fb0...",
  "title": "Estudar Flask",
  "description": "Praticar criação de API",
  "status": "pending",
  "owner_id": "xxxxx",
  "created_at": "2024-04-10T14:22:00"
}
```

---

#### ✏️ Atualizar Tarefa

**PUT** `/api/tasks/<task_id>`

**Body**:

```json
{
  "title": "Atualizado",
  "status": "done"
}
```

**Resposta**:

```json
{
  "message": "Task updated"
}
```

---

#### ❌ Deletar Tarefa

**DELETE** `/api/tasks/<task_id>`

**Resposta**:

```json
{
  "message": "Task deleted"
}
```

---

## ✅ Testando com Postman

### Salvar Token JWT Automaticamente

Na aba **Tests** da requisição de login, cole o seguinte script para salvar o token JWT:

```javascript
// Salva o token globalmente no Postman
const jsonData = pm.response.json();

if (jsonData.token) {
  pm.globals.set("access_token", jsonData.token.access_token);
  console.log("Token salvo com sucesso!");
} else {
  console.warn("Token não encontrado na resposta.");
}
```

Agora, nas rotas protegidas, use o token:

- **Authorization** → **Bearer Token** → **Token**: `{{access_token}}`

---

## 🛠️ Estrutura do Projeto

```
flask_todo_api/
├── app/
│   ├── auth/
│   ├── models/
│   ├── repository/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── database.py
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
```

---

## 🧪 Testes

### Testar com `curl`

Exemplo de requisição para criar uma tarefa:

```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
-H "Authorization: Bearer <seu_token_jwt>" \
-H "Content-Type: application/json" \
-d '{"title": "Estudar Flask", "description": "Praticar criação de API", "status": "pending"}'
```

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

```

Agora você pode copiar e colar este conteúdo diretamente no seu arquivo README.md. Se precisar de mais ajustes, é só avisar!
```
