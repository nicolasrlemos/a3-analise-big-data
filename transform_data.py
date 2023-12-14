import pandas as pd

# Carregar os dados limpos das três planilhas
customers = pd.read_csv('./cleared_datasets/olist_customers_dataset.csv')
orders = pd.read_csv('./cleared_datasets/olist_orders_dataset.csv')
items = pd.read_csv('./cleared_datasets/olist_order_items_dataset.csv')

# Mesclar as tabelas para criar um DataFrame combinado
merge_customers_orders = pd.merge(orders, customers, on='customer_id')
combined_data = pd.merge(merge_customers_orders, items, left_on='order_id', right_on='order_id')

# Agrupar por estado e contar o número total de itens vendidos
count_per_state = combined_data.groupby('customer_state').size().reset_index(name='amount_sold')

# Gravar CSV
count_per_state.to_csv('./tranformed_datasets/count_per_state.csv', index=False)

# Agrupar por estado e calcular o somatório dos itens vendidos
# somatorio_por_estado = dados_combinados.groupby('customer_state').sum().reset_index()

# Exibir o resultado
# print(somatorio_por_estado)
