# Configuração do Trusted Publishing para PyPI

Para que o GitHub Actions possa publicar automaticamente no PyPI, você precisa configurar o **Trusted Publishing** primeiro.

## 📋 **Passo a passo para configurar:**

### 1. Acesse o PyPI
Vá para: https://pypi.org/manage/account/publishing/

### 2. Adicione um Trusted Publisher
Clique em **"Add a new pending publisher"**

### 3. Preencha os dados exatamente assim:
```
PyPI Project Name: publish-lib-ghp
Owner: ghpascon
Repository name: publish_lib_ghp
Workflow filename: publish.yml
Environment name: release
```

### 4. Dados do seu repositório (baseado no erro):
```
Repository: ghpascon/publish_lib_ghp
Repository Owner: ghpascon
Repository Owner ID: 152620285
Workflow Reference: ghpascon/publish_lib_ghp/.github/workflows/publish.yml
Environment: release
```

## 🔧 **Configuração alternativa (sem Trusted Publishing):**

Se você preferir usar API Token ao invés de Trusted Publishing:

### 1. Criar API Token no PyPI:
- Vá para: https://pypi.org/manage/account/token/
- Crie um novo token com escopo: **"Entire account"**
- Copie o token (começa com `pypi-`)

### 2. Adicionar token ao GitHub Secrets:
- No seu repositório: Settings → Secrets and variables → Actions
- Clique em **"New repository secret"**
- Nome: `PYPI_API_TOKEN`
- Valor: Cole o token do PyPI

### 3. Atualizar o workflow:
```yaml
- name: Publish package distributions to PyPI
  uses: pypa/gh-action-pypi-publish@release/v1
  with:
    password: ${{ secrets.PYPI_API_TOKEN }}
    verbose: true
```

## 🚀 **Recomendação:**

Use o **Trusted Publishing** pois é mais seguro (não precisa armazenar tokens).

## 🔍 **Para verificar se funcionou:**

Depois de configurar, execute:
```bash
python commit.py
```

E escolha uma versão patch para testar o processo completo.

## 📝 **Notas importantes:**

1. **Nome do projeto deve ser único** no PyPI
2. **Environment "release"** deve existir no GitHub (já configurado)
3. **Workflow filename** deve ser exatamente `publish.yml`
4. Após configurar, pode levar alguns minutos para ativar

## 🔗 **Links úteis:**

- [Documentação Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [Troubleshooting](https://docs.pypi.org/trusted-publishers/troubleshooting/)
- [GitHub Actions PyPI Publish](https://github.com/pypa/gh-action-pypi-publish)