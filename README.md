# 🤖 Assistente Virtual com PLN (Processamento de Linguagem Natural)

[![GitHub license](https://img.shields.io/github/license/SEU_USUARIO/NOME_DO_REPOSITORIO?style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)

Um projeto de sistema de assistência virtual desenvolvido em Python, focado no uso de PLN (Processamento de Linguagem Natural) para transformar fala em texto (Speech-to-Text) e texto em áudio (Text-to-Speech), além de executar comandos automatizados.

---

## ✨ Funcionalidades

O Assistente Virtual foi desenvolvido com base nos seguintes módulos e capacidades:

### 🎤 Módulo de Fala (Speech-to-Text)
* **Reconhecimento de Voz:** Captura a fala do usuário através do microfone e a converte em texto (linguagem natural humana).
* **Bibliotecas:** `speech_recognition` e `pyaudio`.

### 🗣️ Módulo de Voz (Text-to-Speech)
* **Síntese de Fala:** Transforma as respostas do assistente (em texto) em áudio.
* **Bibliotecas:** `gTTs` e `playsound`.

### ⚙️ Comandos Automatizados
O assistente obedece a comandos de voz para executar funções específicas, incluindo:
* Abrir e pesquisar no **Wikipedia**.
* Abrir o **YouTube** no navegador padrão.
* Buscar a **localização** de serviços (ex: farmácia mais próxima) via Google Maps.
* Funções de entretenimento (ex: contar piadas via `pyjokes`).

---

## 🚀 Como Rodar o Projeto (Passo a Passo)

### Pré-requisitos

Para rodar este projeto, você precisará ter o Python instalado (versão 3.x recomendada).

### 1. Clonar o Repositório

```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as Dependências
Este projeto requer diversas bibliotecas que devem ser instaladas.
```bash
pip install gTTS playsound speechrecognition pyaudio pyjokes wikipedia webbrowser
```
### Atenção: A instalação do pyaudio pode ser um desafio em alguns sistemas operacionais. Se você encontrar erros, pesquise por soluções específicas para seu ambiente (Windows, macOS ou Linux).
## 3. Executar o Assistente
Execute o arquivo principal (assistente.py ou o nome que você usou) no terminal:
## 📚 Bibliotecas Utilizadas

| Biblioteca | Função Principal |
| :--- | :---: |
| `speech_recognition` | Conversão de Fala para Texto (STT) |
| `gTTs` | Conversão de Texto para Fala (TTS) |
| `playsound` | Reprodução dos arquivos de áudio (.mp3) |
| `pyaudio` | Suporte para entrada/saída de áudio (microfone) |
| `wikipedia` | Execução de pesquisas na Wikipedia |
| `webbrowser` | Abertura de links no navegador padrão |
| `pyjokes` | Funcionalidade extra para piadas |

