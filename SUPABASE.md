# Creating the `users` Table in Supabase

## English Version

This guide shows how to create a table named **`users`** in Supabase with the following columns:

- `id` → type `uuid`, primary key
- `usuario` → type `text`
- `senha` → type `text`

> ⚠️ The table **must be named exactly `users`**, and the columns **must be named exactly `id`, `usuario`, and `senha`** for your Python code to work correctly.

---

## Step-by-Step

### 1. Access Supabase
- Go to [https://supabase.com](https://supabase.com)
- Log in and enter your project

### 2. Go to "Table Editor"
- In the left menu, click **Table Editor**
- Click **+ New Table**

### 3. Configure the table
- **Table Name**: `users`
- **Schema**: `public`

---

### 4. Add the following columns

| Column Name | Type   | Primary Key? | Not Null | Default               |
|-------------|--------|--------------|----------|------------------------|
| `id`        | `uuid` | Yes          | Yes      | `gen_random_uuid()`    |
| `usuario`   | `text` | No           | Yes      |                        |
| `senha`     | `text` | No           | Yes      |                        |

Make sure to:
- Set `id` as the **primary key**
- Use `gen_random_uuid()` as the **default** for the `id` column

---

### 5. Disable RLS (Row Level Security)
- After creating the table, go to **Authentication > Policies**
- Select the `users` table
- Disable **Enable RLS** if it's active

---

### 6. Get Your API Key and URL
- In the left menu, click on **Connect**
- Then go to **App Frameworks**
- Copy your **Project URL** and **anon public API key**
- You will need these to connect Supabase with Python

---

### Done!
Your `users` table is now ready to use with your Python app.

---

## Versão em Português

Este guia ensina como criar uma tabela chamada **`users`** no Supabase com as seguintes colunas:

- `id` → tipo `uuid`, chave primária
- `usuario` → tipo `text`
- `senha` → tipo `text`

> ⚠️ O nome da tabela deve ser exatamente **`users`** e os nomes das colunas devem ser exatamente **`id`, `usuario` e `senha`**, para garantir o funcionamento com o código em Python.

---

## Passo a Passo

### 1. Acesse o Supabase
- Acesse [https://supabase.com](https://supabase.com)
- Faça login e entre no seu projeto

### 2. Vá para "Table Editor"
- No menu lateral, clique em **Table Editor**
- Clique em **+ New Table**

### 3. Configure a tabela
- **Nome da Tabela**: `users`
- **Schema**: `public`

---

### 4. Adicione as colunas conforme abaixo

| Nome da Coluna | Tipo   | Chave Primária? | Not Null | Valor Padrão           |
|----------------|--------|------------------|----------|-------------------------|
| `id`           | `uuid` | Sim              | Sim      | `gen_random_uuid()`     |
| `usuario`      | `text` | Não              | Sim      |                         |
| `senha`        | `text` | Não              | Sim      |                         |

Certifique-se de:
- Marcar `id` como **chave primária**
- Usar `gen_random_uuid()` como **valor padrão** da coluna `id`

---

### 5. Desative o RLS (Row Level Security)
- Após criar a tabela, vá até **Authentication > Policies**
- Selecione a tabela `users`
- Desative a opção **Enable RLS**, se estiver ativada

---

### 6. Obtenha a URL e a API Key do seu projeto
- No menu lateral, clique em **Connect**
- Depois vá até **App Frameworks**
- Copie sua **Project URL** e a **anon public API key**
- Você vai precisar dessas informações para conectar com o Python

---

### Pronto!
Sua tabela `users` está pronta para ser usada com seu código Python.
