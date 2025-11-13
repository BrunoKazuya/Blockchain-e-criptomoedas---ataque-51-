# Projeto II — Ataque 51% em Blockchains (Simulação Off-Chain)

**Autor:** Bruno Kazuya Yamato Sakaji  
**Disciplina:** SSC0958 – Blockchain e Criptomoedas  
**Data:** Novembro/2025  

---

## Resumo do Projeto
Este projeto implementa uma **simulação off-chain** do ataque 51%, fenômeno em que um agente que controla a maioria do poder de mineração pode causar reorganizações (*reorgs*) e *double-spends*.  
A aplicação é **didática** e foi desenvolvida em **Python**, permitindo visualizar o comportamento das cadeias e estimar probabilidades de sucesso do atacante.

---

## Motivação e Justificativa
A segurança de blockchains depende da suposição de que a maioria dos mineradores é honesta.  
O objetivo aqui é **mostrar intuitivamente o que acontece quando essa suposição é violada**, permitindo entender o impacto de um ataque 51% de forma prática.  

**Por que off-chain?**  
O modelo Python é reprodutível, rápido de executar e foca na dinâmica do consenso sem necessidade de infraestrutura de rede.  

---

## Como executar
- **Execução de amostra (plot):**  
  `python src/simulate_attack51.py --mode sample --p 0.55 --steps 300`

- **Execução estatística (batch):**  
  `python src/simulate_attack51.py --mode batch --p 0.51 --k 6 --trials 5000`

Os resultados são salvos em `sample_evolution.png` e `batch_results.csv`.

---

## Justificativas (requeridas pelo Projeto II)
- **Por que usar blockchain?** O projeto é pedagógico: demonstra a consequência do controle majoritário na segurança de blockchains PoW.  
- **Plataforma escolhida:** Simulação off-chain em Python, evitando complexidades de contrato inteligente e priorizando clareza conceitual.  
- **Aplicações similares:**  
  - *Satoshi Nakamoto (2008)* — Bitcoin whitepaper.  
  - *Eyal & Sirer (2014)* — “Majority is not Enough”.  
  - *Meni Rosenfeld (2014)* — análise de double-spending probabilístico.

---

## Resultados
- O gráfico `sample_evolution.png` mostra a evolução das cadeias (honesta e atacante).  
- A simulação mostra *reorgs* visíveis quando o atacante revela sua cadeia privada.  
- Os resultados em `batch_results.csv` indicam como a probabilidade de sucesso aumenta quando `p > 0.5`.

---

## Limitações
- Modelo simplificado (sem latência de rede, taxas ou pools).  
- Focado na intuição, não em precisão econômica.  

---

## Estrutura do Repositório
```
src/
  simulate_attack51.py
  utils.py
README.md
LICENSE
LOC.txt
slides.pptx
sample_evolution.png
batch_results.csv
```

---

## Entregáveis
- Código no GitHub (com LICENSE).  
- Slides + link do vídeo gravado (submeter no Moodle).  
- Contagem de linhas (`LOC.txt`).  

---

## Licença
Distribuído sob a licença MIT.

---

## Informações de Entrega
- **GitHub:** https://github.com/BrunoKazuya/Blockchain-e-criptomoedas---ataque-51-.git
- **Vídeo:** https://youtu.be/x0Jwx-ioepc
- **Autoavaliação:** 10 / 10  
