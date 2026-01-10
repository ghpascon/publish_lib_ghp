# Setup Guide - Como Usar Este Projeto

Este guia mostra como configurar e usar este projeto como template para publicar suas próprias bibliotecas Python no PyPI.

## 🚀 **Configuração Inicial**

### 1. Fork/Clone do Projeto

```bash
# Clone o repositório
git clone https://github.com/ghpascon/publish_lib_ghp.git
cd publish_lib_ghp
```

### 2. Personalize o Projeto

**Atualize o `pyproject.toml`:**
```toml
[tool.poetry]
name = "seu-pacote-nome"  # Mude aqui
version = "0.1.0"
description = "Sua descrição aqui"  # Mude aqui
authors = ["Seu Nome <seu.email@exemplo.com>"]  # Mude aqui
homepage = "https://github.com/seu-usuario/seu-projeto"  # Mude aqui
repository = "https://github.com/seu-usuario/seu-projeto"  # Mude aqui
```

**Atualize os arquivos:**
- `README.md` - Mude título, descrição e exemplos
- `LICENSE` - Atualize o copyright
- Pasta `src/` - Renomeie para o nome do seu pacote

## 🔐 **Configuração do GitHub Actions**

### Opção 1: Usando API Token (Mais Simples)

#### 1. Criar Token no PyPI
1. Acesse: https://pypi.org/manage/account/token/
2. Clique em **"Add API token"**
3. **Token name:** Coloque um nome descritivo (ex: "GitHub Actions")
4. **Scope:** Selecione "Entire account" (ou específico para seu projeto)
5. Clique em **"Add token"**
6. **COPIE O TOKEN** (começa com `pypi-...`) - só aparece uma vez!

#### 2. Adicionar Token aos GitHub Secrets
1. No seu repositório GitHub, vá em: **Settings** → **Secrets and variables** → **Actions**
2. Clique em **"New repository secret"**
3. **Name:** `PYPI_API_TOKEN`
4. **Secret:** Cole o token que você copiou do PyPI
5. Clique em **"Add secret"**

## 📝 **Como Fazer Releases**

### Usando o Script Automatizado

Este projeto inclui um script `commit.py` que automatiza todo o processo:

```bash
python commit.py
```

**O script fará:**
1. Perguntará o tipo de versão (patch, minor, major)
2. Perguntará a mensagem do commit
3. Atualizará a versão automaticamente
4. Fará commit das mudanças
5. Criará e enviará a tag
6. O GitHub Actions fará o resto!

## 📋 **Checklist de Configuração**

- [ ] Forked/clonado o repositório
- [ ] Atualizado `pyproject.toml` com seus dados
- [ ] Renomeado pasta `src/publish_lib_ghp` para `src/seu_pacote`
- [ ] Atualizado `README.md`
- [ ] Configurado token PyPI OU trusted publishing
- [ ] Adicionado `PYPI_API_TOKEN` aos GitHub Secrets (se usando token)
- [ ] Testado com `python commit.py`

## 🎯 **Exemplo de Uso do Script commit.py**

```
$ python commit.py

🚀 Script de Release Automatizado
========================================

📈 Tipos de versão disponíveis:
  1. patch - Correções de bugs (1.0.0 -> 1.0.1)
  2. minor - Novas funcionalidades (1.0.0 -> 1.1.0)
  3. major - Mudanças que quebram compatibilidade (1.0.0 -> 2.0.0)

❓ Escolha o tipo de versão (1-3 ou patch/minor/major): 2

💬 Digite a mensagem do commit: Adicionar nova classe Calculator

📋 Resumo da operação:
   Versão atual: 0.1.0
   Tipo de atualização: minor
   Mensagem do commit: Adicionar nova classe Calculator

❓ Confirma a operação? (S/n): s

🔄 Executando: poetry version minor
✅ Nova versão: 0.2.0
📝 Adicionando mudanças ao git...
📝 Fazendo commit...
📤 Enviando commit para o repositório...
🏷️  Criando tag v0.2.0...
📤 Enviando tag para o repositório...

🎉 Release criado com sucesso!
```

## 🔍 **Verificar se Funcionou**

1. **GitHub Actions:** https://github.com/seu-usuario/seu-projeto/actions
2. **PyPI:** https://pypi.org/project/seu-pacote-nome/
3. **Instalar:** `pip install seu-pacote-nome`

## 🆘 **Solução de Problemas**

### Token PyPI não funciona
- Verifique se copiou o token completo
- Confirme que o secret se chama exatamente `PYPI_API_TOKEN`
- Teste criando um novo token

### Trusted Publishing falha
- Verifique se os dados no PyPI batem exatamente com seu repositório
- Nome do projeto deve ser único no PyPI
- Environment "release" deve existir (já configurado)

### Script commit.py falha
- Certifique-se de estar em um repositório git
- Verifique se poetry está instalado
- Confirme que não há mudanças não commitadas importantes

## 💡 **Dicas**

- **Sempre teste localmente** antes de fazer release
- **Use versionamento semântico**: patch (bugs), minor (features), major (breaking changes)
- **Mantenha o CHANGELOG.md atualizado**
- **Adicione testes** para novas funcionalidades
- **O nome do pacote PyPI deve ser único** globalmente

## 📞 **Suporte**

Se encontrar problemas:
1. Verifique os logs do GitHub Actions
2. Consulte a documentação do PyPI
3. Revise este guia
4. Verifique issues no repositório original

---
**Template criado por:** Gabriel Henrique Pascon  
**Repositório original:** https://github.com/ghpascon/publish_lib_ghp