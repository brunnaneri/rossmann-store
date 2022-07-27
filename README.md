# Rossmann Store - Sales Predict

Rossmann é uma rede de farmária que está presente em sete países na Europa, composta por mais de 3000 drogarias. 
As vendas das lojas são influenciadas por diversos fatores, como promoções, competição entre lojas próximas, feriados, sazonalidade e localidade. Atualmente, os gerentes de loja da Rossmann têm a tarefa de prever suas vendas diárias com até seis semanas de antecedência, no entanto, como os gerentes fazem suas previsões de venda individualmente, considerando circunstâncias únicas, a precisão dos seus resultados pode ser bastante incerta.

Observação: Este projeto foi inspirado no desafio "Rossmann Store Sales" publicado no Kaggle (https://www.kaggle.com/competitions/rossmann-store-sales). Por isso, trata-se de um problema fictício, no entanto solucionado com passos e análises de um projeto real.

DESCRIÇÃO + FOTO

# 1.0 PROBLEMA DE NEGÓCIO

## 1.1 Descrição do Problema

O CFO da rede pretende fazer uma reforma nas lojas e para saber a viabilidade desse investimento, necessita da previsão de vendas diárias das lojas para as próximas 6 semanas com uma previsão mais assertiva.
Para isso, será disponibilizada uma base de dados dados históricos de vendas de 1.115 lojas Rossmann.

## 1.2 Objetivo

Desse modo, este projeto visa desenvolver um modelo que caracterize bem o comportamento de venda das diferentes lojas incluídas na base de dados e consiga fazer predições bem sucedidas das vendas de cada loja com uma antecedência de seis semanas.

## 1.3 Sumário dos Dados

| Variable                       | Descriptions                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| Id                               | An id that represents a (store, date) duple within the test set|
| Store                            | A unique id for each store                                   |
| Sales                            | The turnover for any given day                          |
| Customers                        | The number of customers on a given day                       |
| Open                             | An indicator for whether the store was open: 0 = closed, 1 = open |
| Stateholiday                     | Indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. A = public holiday, b = easter holiday, c = christmas, 0 = none |
| Schoolholiday                    | Indicates if the (store, date) was affected by the closure of public schools |
| Storetype                        | Differentiates between 4 different store models: a, b, c, d  |
| Assortment                       | Describes an assortment level: a = basic, b = extra, c = extended |
| Competitiondistance              |Distance in meters to the nearest competitor store           |
| Competitionopensince[month/year] | Gives the approximate year and month of the time the nearest competitor was opened |
| Promo                            | Indicates whether a store is running a promo on that day        |
| Promo2                           | Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating |
| Promo2since[year/week]           | Describes the year and calendar week when the store started participating in promo2 |
| Promointerval                    | Describes the consecutive intervals promo2 is started, naming the months the promotion is started anew. E.G. "Feb,may,aug,nov" means each round starts in february, may, august, november of any given year for that store |

# 2.0 PREMISSAS DO NEGÓCIO

Foram feitas as seguintes considerações durante o desenvolvimento do projeto:

- Lojas com 'sales' iguais a 0 foram descartadas.
- Os dias em que as lojas estavam fechadas foram descartados.
- Lojas sem informção (NaN) de "Competition_Distance" foi definido um valor de '200000' para essa distância.

# 3.0 PLANEJAMENTO DA SOLUÇÃO

## 3.1 Produto Final

## 3.2 Processo

### PASSO 1 - Data Collect

### PASSO 2 - Data Description

### PASSO 3 - Feature Engineering

### PASSO 4 - Filtragem de Variáveis

### PASSO 5 - Exploratory Data Analysis (EDA)

### PASSO 6 - Data Preparation

### PASSO 7 - Feature Selection

### PASSO 8 - Machine Learning Model

### PASSO 9 - Fine Tunning

### PASSO 10 - Interpretação e Tradução do Erro

### PASSO 11 - Deploy to Production
