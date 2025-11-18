# 📂 Organizador de Arquivos Inteligente (Desktop Automation)

> Uma ferramenta de automação desktop com interface gráfica (GUI) desenvolvida para aumentar a produtividade e organização de arquivos pessoais e corporativos.

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)

## 🎯 Sobre o Projeto

Este projeto resolve um problema comum em ambientes corporativos e domésticos: a desorganização de pastas de downloads e documentos.

Diferente de scripts simples, este software possui uma **Interface Gráfica Amigável (GUI)** construída com `Tkinter` e foi compilado em um executável (`.exe`), permitindo que qualquer usuário final utilize a ferramenta sem necessidade de instalar Python ou usar o terminal.

### ✨ Funcionalidades

* **Interface Visual:** Seleção de pastas intuitiva via janela do Windows.
* **Categorização Automática:** Identifica e separa arquivos por extensão:
    * 🖼️ **Imagens:** .jpg, .png, .gif
    * 📄 **Documentos:** .pdf, .docx, .xlsx, .csv
    * 💾 **Instaladores:** .exe, .zip, .rar
    * 🎵 **Mídia:** .mp3, .mp4
* **Tratamento de Erros:** Sistema robusto que evita falhas caso a pasta não exista ou arquivos estejam em uso.
* **Feedback Visual:** Mensagens de status e pop-ups de confirmação.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem base para a lógica de automação.
* **Tkinter:** Criação da Interface Gráfica (GUI).
* **OS & Shutil:** Manipulação de sistema de arquivos (File System).
* **PyInstaller:** Compilação e criação do executável standalone.

## 🚀 Como Usar (Para Desenvolvedores)

1. Clone o repositório:
```bash
git clone [https://github.com/vinicius311006/organizador](https://github.com/vinicius311006/organizador)