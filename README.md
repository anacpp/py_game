# WHERE IS MY SNACK?

## 🎮 Sobre o Jogo

"Where Is My Snack?" é um jogo **roguelike** em visão aérea, onde o jogador deve coletar todas as moedas em um labirinto cheio de inimigos e obstáculos. Ao final, é preciso encontrar a **porta de saída** para vencer o jogo. O jogador perde se colidir com um inimigo.

O jogo foi desenvolvido com a biblioteca **PgZero** conforme os requisitos do teste de tutores.

---

## 🧩 Gênero

- Roguelike (visão superior, mapa baseado em células, movimentação animada e suave)

---

## ✅ Funcionalidades

- **Menu principal** com três botões:
  - `Start Game`
  - `Sound ON/OFF`
  - `Exit`
- **Música de fundo** e **efeitos sonoros**
- **Herói com animação** completa para todas as direções
- **Inimigos com sprites animados** e movimentação própria
- **Sistema de colisão** com paredes e inimigos
- **Coleta de moedas** e detecção de vitória
- Mensagens de **"YOU WIN!"** ou **"GAME OVER!"** na tela

---

## 🛠️ Bibliotecas e Módulos Utilizados

Apenas os permitidos:

- `pgzero`
- `pgzero.actor`
- `pgzero.builtins` (para `music`, `sounds`, `Rect`)
- `pygame.Rect` (conforme exceção autorizada)
- Nenhuma outra biblioteca externa foi utilizada.

---

## 🧠 Estrutura do Código

- `main.py`: lógica principal, loop do jogo e menu
- `player.py`: classe `Player` com movimentação, colisão e animação
- `enemies.py`: classe `Enemy` com IA básica e animação
- `settings.py`: mapa, botões do menu e constantes do jogo
- `assets/`: (não incluído aqui) sprites e arquivos de som utilizados pelo jogo

---

## ▶️ Como Jogar

1. Execute o jogo com o 
2. Use as teclas:
- `← ↑ → ↓` para mover o personagem

3. Colete todas as moedas e vá até a **porta de saída** para vencer.

4. Evite os **inimigos**! Se tocar em um, é **game over**.

---

## 📁 Observações

- O jogo foi desenvolvido **exclusivamente para este teste**, com **código original e único**.
- Não há uso de bibliotecas não permitidas.
- A lógica do jogo é funcional e livre de bugs conhecidos.

---

## 🚀 Requisitos Mínimos

- Python 3.x
- Biblioteca `pgzero` instalada
**PgZero**:

  ---
  ## 🛠️ Instalação e Execução

### 1. 📦 Requisitos

Certifique-se de que o **Python 3** está instalado na sua máquina.  
Você pode verificar abrindo o terminal e digitando:

```bash
python3 --version
```

### 2. Instalando a biblioteca pgzero
```bash
pip install pgzero
```

### Executando o Jogo
Após a instalação da biblioteca pgzero, vá até a pasta onde estão os arquivos do jogo e execute no terminal:
```bash
pgzrun main.py
```
Caso não funcione, use:
```bash
python3 -m pgzero main.py
```

