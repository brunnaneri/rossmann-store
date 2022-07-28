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

Os resultados, ou seja, as predições, poderão ser acessadas via celular, através de um BOT do Telegram, em que o número da loja, 'Store ID, será repassado pelo usuário que irá receber a predição das vendas para as próximas seis semanas.

## 3.2 Processo
A resolução foi realizada seguindo a metodologia CRISP-DM que é uma abordagem cíclica que agiliza a entrega de resultado/valor do projeto.

### PASSO 1 - Data Collect

Os dados foram coletados do site do Kaggle.

### PASSO 2 - Data Description

Ocorreu o primeiro contato com os dados em si. Aqui foram feitas a primeiras análises para se ter um overview dos dados. 

A análise descritiva é composta pelas etapas de Descrição dos Dados, Substituição dos Dados faltantes e por fim a Estatística descritiva dos dados.

A base de dados é composta por 1017209 linhas que correspondem as vendas realizadas pelas 1115 lojas.

### PASSO 3 - Feature Engineering

Etapa de criação de novas features (colunas) derivadas as originais e criação de hipóteses que serão avaliadas na etapa de análise exploratória dos dados.

### PASSO 4 - Filtragem de Variáveis

Nesse passo é feita a filtragem de colunas e seleção de linhas do dataset com a finalidade de analisar e pensar nas restrições do negócios, eliminando os dados que não agregam informação ou que não poderão ser usados no modelo por não estarem disponíveis na hora da predição.

- Feature 'open' foi excluída porque foram filtrados apenas do dados em que 'open' = 1 (loja aberta), que é de fato o que nos interessa e nos serve para o problema de negócio;
- Feature 'costumers' foi excluída porque é uma informação que não temos disponível no momento da predição, é um dado consequente.

### PASSO 5 - Exploratory Data Analysis (EDA)

Essa etapa é de grande importância, nela ocorre a validação ou não das hipóteses de negócio que foram levantadas. A análise exploratória dos dados foi feita a partir dos seguintes passos:

Análise Univarida: avaliando uma variável por vez.
Análise Bivariada: Nesse momento se faz a análise/validação das hipóteses levantas do passo anterior. É feita a análise entre a variável resposta e as variáveis/atributos que atuam sob essa variável reposta.
Análise Multivariada: Se busca redução da dimensionalidade do dataset, a fim de deixar o modelo menos complexo, sem que para tal haja perda de informações. 
                      Isso é possível através da análise de correlação entre as variáveis que atuam sob a variável resposta, de forma que, dada um alta correlação                           entre elas, a eliminação de uma delas não resultaria em uma grande perda de informação.

### PASSO 6 - Data Preparation

Preparação dos dados de forma que possibilite um melhor aprendizado do modelo de ML a ser aplicado, visto que a maioria desses tem um melhor desempenho quando se tem dados numéricos e em mesma escala.

Foram realizadas as seguintes operações, quando necessárias:
Reescala: dados numéricos que não tem distribuição normal.
Encoding: transformando dados categóricos em numéricos.
Transformação de Natureza: transformando dados de natureza cíclica (dias, meses...), respeitando suas características.
Transformação de grandeza: ocorre na variável resposta. A ideia é deixar a distribuição da variável mais próxima de uma normal.

### PASSO 7 - Feature Selection

A seleção de atributos tem o objetivo de identificar e selecionar variáveis que caracterizam bem o fenômeno e por isso são relevantes para o modelo. Para isso, foi utilizado o algoritmo Boruta (https://github.com/scikit-learn-contrib/boruta_py) e comparado seu resultado com as análises feitas na etapa de EDA.

O algoritmos de machine learning foram treinados considerando as variáveis selecionadas nessa etapa.

### PASSO 8 - Machine Learning Models

Foram treinados e avaliados diferentes algoritmos de regressão de modelos de machine learning de aprendizado supervisionado, sendo estes: Linear Regression, Linear Regression Regularized, XGBoost Regression, Random Forest Regression.

Inicialmente os modelos foram treinados utilizando todos os dados de treino separados anteriormente, na etapa de feature selection. As métricas utilizadas para avaliar a performance dos modelos foram: MAE, MAPE e RMSE.

- MAE (Mean Absolute Error): erro absoluto médio entre os valores observados(reais) e as predições.
<img src="https://user-images.githubusercontent.com/101215927/181344941-dbaac27e-2221-4e26-a8ff-3c4f48822715.png" width=20% height=20% title="mae" alt="project_cover_image"/>

- MAPE (Mean Absolute Percentual Error): erro absoluto médio percentual.
<img src="https://user-images.githubusercontent.com/101215927/181345120-3f150605-5ac9-49ea-81ce-664e7f3d969e.png" width=20% height=20% title="mape" alt="project_cover_image"/>

- RMSE (Mean Squared Error): raiz quadrática média dos erros entre os valores observados e as predições.
<img src="https://user-images.githubusercontent.com/101215927/181345180-a912121c-0fd3-4634-9785-87578a6dd6a5.png" width=20% height=20% title="rmse" alt="project_cover_image"/>

Foi criado um modelo de média (Average Model) considerado como baseline, que serve como referência comparativa para que se possa medir a qualidade dos modelos de Machine Learning treinados.

Os resultados dos desempenhos dos modelos estão descritos abaixo:

|Name_Model|	MAE|	MAPE|	RMSE|
|:----------------|:------------------:|:-----------------------:|-----------------------:|
|Linear Regression|	1862.386337|	0.293202|	2655.269908|
|Lasso|	1896.790622| 0.289654|	2749.113591|
|Random Forest Regressor|	694.649487|	0.104069|	1024.258728|
|XGBoost Regressor|	879.265789|	0.126879|	1305.154484|

Observou-se um melhor desempenho nos modelos baseado em árvores, Random Forest e XGBoost, e um desempenho ruim nos modelos de Linear Regression e Linear Regression Regularized, demonstrando um certo nível de complexidade do problema.

Em seguida, os modelos foram treinados novamente utilizando a técnica de Cross-Validation (CV), a qual permite medir o desempenho em vários intervalos de tempo no conjunto de dados total, diminuindo a influência do período escolhido para realizar treinamento e validação.

O cross-validation consiste, basicamente, em dividir os dados em diferentes partes para testar o modelo e assim obter a performance real, que corresponde, no caso, a média dos erros de cada iteração +/- desvio padrão.

Por se tratar de um problema em que o tempo influencia, foi necessário considerar esta variável na separação dos datasets em treino e validação nas iterações do cross-validation. O esquema foi da seguinte forma:

<img src="https://user-images.githubusercontent.com/101215927/181352576-460c9580-aca1-4fea-aaec-886fcfa98b1c.png" width=80% height=50% title="cross" alt="project_cover_image"/>

A porção de dados de validação corresponde a seis semanas em cada iteração.

O desempenho dos modelos está descrito na tabela a seguir:

Name_Model|	MAE CV |	MAPE CV	|RMSE CV|
|:----------------|:------------------:|:-----------------------:|-----------------------:|
|Linear Regression	|2080.12+/-341.75|	0.29+/-0.02|	2971.27+/-519.47|
|Lasso|	2143.28+/-395.1|	0.29+/-0.01|	3090.02+/-577.04|
|Random Forest Regressor|	854.45+/-269.82	|0.12+/-0.03	|1288.03+/-417.62|
|XGBoost Regressor|	984.61+/-177.97|	0.14+/-0.02|	1402.0+/-247.48|

Analisando os resultados, o algoritmo XGBoost Regressor foi escolhido para seguir na solução deste problema de negócio. Mesmo o Random Forest Regressor tendo um desempenho um pouco acima do XGBoost, fatores como tempo de execução do algoritmo e espaço de memória do modelo também foram considerados na escolha do modelo, os quais são consideravelmente maiores no Random Forest.

### PASSO 9 - Hyperparameter Fine Tunning

Nesta etapa busca-se uma melhora da performance do modelo através da otimização dos seus parâmetros. Para isso, foi utilizado o método Random Search para treinar novamente o algoritmo, aplicando o cross-validation, totalizando 25 iterações. Os parâmetros calibrados foram: n_estimators, eta, max_depth, subsample e colsample_bytree. Todas as iterações estão detalhadas no notebook, contendo seus parâmetros e valores de MAE, MAPE e RMSE.

O modelo foi escolhido baseado na sua performance e tempo de execução, visando otimizar também a operacionabilidade. Os resultados do desempenho podem ser observados na tabela seguir:

MODEL|MAE|MAPE|RMSE|
|:----------------|:------------------:|:-----------------------:|-----------------------:|
XGBoost Regressor | 897.98+/-141.27 │ 0.12+/-0.01 │ 1284.86+/-201.52 

Por fim, o modelo foi treinado com toda base de dados:
```python
param_tuned = {'n_estimators': 1750, 
                'eta': 0.03, 
                'max_depth': 5, 
                'subsample': 0.3, 
               'colsample_bytree': 0.7}

xgb_model_tuned = xgb.XGBRegressor( objective='reg:squarederror',
                                n_estimators=param_tuned['n_estimators'],
                                eta=param_tuned['eta'],
                                max_depth=param_tuned['max_depth'],
                                subsample=param_tuned['subsample'],
                                colsample_bytree=param_tuned['colsample_bytree'] ).fit( x_train, y_train )
```                                   
A performance do modelo com os dados de teste foi:

|Name_Model|	MAE|	MAPE|	RMSE|
|:----------------|:------------------:|:-----------------------:|-----------------------:|
|XGBoost Regressor|	685.688619|	0.101687|	988.820648|

### PASSO 10 - Interpretação e Tradução do Erro

Neste passo, os resultados do modelo, os erros, são analisados a fim de avaliar a performance do algoritmo e também são traduzido como resultados do negócio, em valores financeiros considerando diferentes cenários.

#### Business Performance

Considerando o MAE calculado para cada loja no conjunto de dados de teste, foi possível calcular o pior e melhor cenário para cada uma destas.
A seguir, está descrita expectativa de venda para as cinco primeiras lojas:

|store	prediction	MAE	MAPE	worst_scenario	best_scenario
|1|	161278.609375|	275.730621|	0.062825|	161002.878754|	161554.33999|
|2|	182446.890625|	396.693313|	0.081775|	182050.197312|	182843.58393|
|3|	262568.281250|	566.920126|	0.079047|	262001.361124|	263135.20137|
|4|	348689.750000|	861.404574|	0.082938|	347828.345426|	349551.15457|
|5|	173324.593750|	387.789676|	0.084827|	172936.804074|	173712.38342|



### PASSO 11 - Deploy to Production

## 3.3 Entrada

### 3.3.1 Fonte de Dados

### 3.3.2 Ferramentas

# 4.0 TOP INSIGHTS
Durante a análise exploratória de dados, na etapa de validação das hipóteses, foram gerados insights ao time de negócio.

Insights são informações novas, ou que contrapõe crenças até então estabelecidas do time de negócios, que devem ser acionáveis e assim direcionar resultados futuros.

# 5.0 MODELO DE MACHINE LEARNING APLICADO

COLOCAR A SESSAO 8.0 FINE TUNNING

# 6.0 PERFORMANCE DO MODELO

COLOCAR A SESSÃO 9.0

COLOCAR UM GIF DO TELEGRAM

# 7.0 CONCLUSÕES

# 8.0 PRÓXIMOS PASSOS
