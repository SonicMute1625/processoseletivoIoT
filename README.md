# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_CLI_TOKEN
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo: Luiz Felipe Miranda de Souza**
- **GitHub:https://github.com/SonicMute1625 **

---

## Visão Geral da Solução

O objetivo deste projeto é simular um contador de produção não-intrusivo para linhas de montagem manuais ou semiautomáticas que operam sem CLP.
O sistema embarcado simulado monitora a passagem de peças em uma esteira através de um sensor óptico (LDR), incrementando um contador de produção a cada peça detectada, calculando o tempo de ciclo entre peças e identificando micro-paradas na linha (quando a esteira fica travada por tempo excessivo).

O usuário (operador da linha) interage com o sistema através de um botão físico, que permite resetar o turno a qualquer momento, zerando o contador e os cronômetros acumulados.
Toda a telemetria e os alertas são reportados via comunicação Serial.

---

## Arquitetura do Sistema Embarcado

O firmware (src/main.py) é organizado como uma máquina de estados não-bloqueante, executada em um loop principal que roda indefinidamente sem nenhuma chamada bloqueante longa (sleep), garantindo que o sistema nunca perca uma janela de estímulo dos sensores.

Fluxo principal (main()):

Inicializacao -> imprime mensagem de boot
loop infinito:
    processar_sensor_lux()    -> maquina de estados da esteira
    processar_botao_reset()   -> leitura debounced do botao
    pequena pausa de polling (10ms, nao bloqueante)

Estrutura de estados da esteira (processar_sensor_lux):

LIVRE: estado de repouso, sensor detecta luz (linha desobstruída)
BLOQUEADO: peça obstruindo o feixe de luz

Transições:

LIVRE → BLOQUEADO: início da passagem de uma peça (marca o instante inicial do bloqueio)
BLOQUEADO → LIVRE: peça passou completamente → incrementa o contador de produção
Permanência prolongada em BLOQUEADO (> 5s): dispara alerta de micro-parada (uma única vez por evento)

Temporização: toda a lógica de tempo (duração do bloqueio, debounce do botão) usa time.ticks_ms() e time.ticks_diff(), que lidam corretamente com overflow do contador de ticks, mais seguro que subtração direta de timestamps.

Interação entre componentes: o sensor LDR e o botão são lidos de forma independente a cada iteração do loop; o botão pode resetar o estado da esteira a qualquer momento, inclusive no meio de um bloqueio em andamento.

---

## Componentes Utilizados na Simulação

Placa: ESP32 DevKit C v4

Sensor óptico (LDR): módulo de 4 pinos (VCC, GND, DO, AO), identificado como ldr1 no diagram.json.
Função: detectar a interrupção do feixe de luz pela passagem de peças na esteira, através da leitura analógica (AO) conectada ao ADC do ESP32.

Botão (btn1): botão de reset manual do turno, ligado ao pino digital D15 com pull-down interno do ESP32.
Função: permitir ao operador zerar contadores e cronômetros a qualquer momento.

Interface Serial (UART): usada para reportar todos os eventos (inicialização, contagem, alertas, reset) em texto legível.

Componente	  Pino do componente	Pino do ESP32
LDR (ldr1)	  VCC	                3V3
LDR (ldr1)	  GND	                GND
LDR (ldr1)	  AO	                D34 (ADC)
Botão (btn1)	1.l	                3V3
Botão (btn1)	2.l	                GND
Botão (btn1)	2.r	                D15

---

## Decisões Técnicas Relevantes

Organização do código: o firmware é dividido em funções de responsabilidade única (ler_ldr_bruto, resetar_turno, processar_botao_reset, processar_sensor_lux), facilitando leitura e manutenção. Constantes de configuração (limiares, pinos, tempos) ficam centralizadas no topo do arquivo.

Estados explícitos em vez de flags soltas: o estado da esteira é representado por uma variável de string ("LIVRE" / "BLOQUEADO"), tornando a lógica de transições mais legível do que múltiplas variáveis booleanas.

Leitura do LDR em ADC bruto, não em lux reconstruído: a primeira versão do firmware tentava reconstruir o valor de "lux" a partir da tensão do ADC, usando a fórmula teórica do datasheet do componente (parâmetros gamma e rl10).
Essa abordagem se mostrou pouco confiável: uma calibração empírica (leitura direta do ADC em diferentes valores de lux configurados no simulador) revelou que a relação real do componente simulado é inversa à esperada pela fórmula teórica, causando falsos positivos de bloqueio.
A solução final compara diretamente o valor bruto do ADC (0–4095) contra dois limiares calibrados empiricamente (claro/escuro), eliminando a dependência de uma fórmula sensível a erros de calibração.

Debounce por estabilidade contínua: o componente wokwi-pushbutton usado no diagram.json tem o atributo bounce ativado, simulando o ricochete mecânico real de um botão físico.
O debounce do firmware não dispara na primeira mudança de nível após um intervalo mínimo, em vez disso, exige que o pino permaneça estável no novo nível por um período contínuo antes de considerar o evento válido, filtrando o ricochete simulado.

Alerta de micro-parada único por evento: uma flag (alerta_microparada_emitido) evita que o alerta seja reimpresso repetidamente enquanto a condição de bloqueio prolongado persiste, disparando a mensagem apenas uma vez por ocorrência.

---

## Resultados Obtidos

Cenário testado	Resultado
test_1 — Contagem Normal de Peças	✅ Passou
test_2 — Detecção de Micro-parada na Esteira	✅ Passou
test_3 — Reset Manual de Turno	❌ Falhou (timeout na simulação)

O sistema atende corretamente aos requisitos de inicialização, contagem de peças (com transição de borda para evitar contagem duplicada) e detecção de micro-parada (limiar de 5 segundos).
O reset manual de turno também funciona do ponto de vista funcional, a mensagem "Turno resetado com sucesso. Contadores zerados." é emitida corretamente no momento esperado, porém a simulação automatizada do test_3 não finaliza dentro do tempo limite (10000ms) definido pelo Wokwi CI, resultando em falha do pipeline por timeout mesmo com o comportamento do firmware correto.
Os testes manuais no Wokwi funcionaram sem nenhum problema.

---

## Comentários Adicionais (Opcional)



---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
