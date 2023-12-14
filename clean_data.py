from pandas import read_csv


def clean_customers() -> None:
    file_path = './datasets/olist_customers_dataset.csv'
    df = read_csv(file_path)

    print('Limpando...')

    # Removendo linhas com dados ausentes
    df = df.dropna()

    # Removendo duplicatas
    df = df.drop_duplicates()

    # Convertendo colunas para o tipo correto, se necessário
    # Exemplo: df['coluna'] = df['coluna'].astype(int)

    # Outras operações de limpeza de dados, se necessário

    # Salvando o DataFrame limpo de volta para um novo arquivo CSV
    df.to_csv('./cleared_datasets/olist_customers_dataset.csv', index=False)

    print('Limpeza realizada')


def clean_order_items() -> None:
    file_path = './datasets/olist_order_items_dataset.csv'
    df = read_csv(file_path)

    print('Limpando...')

    # Removendo linhas com dados ausentes
    df = df.dropna()

    # Removendo duplicatas
    df = df.drop_duplicates()

    # Convertendo colunas para o tipo correto, se necessário
    # Exemplo: df['coluna'] = df['coluna'].astype(int)

    # Outras operações de limpeza de dados, se necessário

    # Salvando o DataFrame limpo de volta para um novo arquivo CSV
    df.to_csv('./cleared_datasets/olist_order_items_dataset.csv', index=False)

    print('Limpeza realizada')


def clean_orders() -> None:
    file_path = './datasets/olist_orders_dataset.csv'
    df = read_csv(file_path)

    print('Limpando...')

    # Removendo linhas com dados ausentes
    df = df.dropna()

    # Removendo duplicatas
    df = df.drop_duplicates()

    # Convertendo colunas para o tipo correto, se necessário
    # Exemplo: df['coluna'] = df['coluna'].astype(int)

    # Outras operações de limpeza de dados, se necessário

    # Salvando o DataFrame limpo de volta para um novo arquivo CSV
    df.to_csv('./cleared_datasets/olist_orders_dataset.csv', index=False)

    print('Limpeza realizada')


def clean_products() -> None:
    file_path = './datasets/olist_products_dataset.csv'
    df = read_csv(file_path)

    print('Limpando...')

    # Removendo linhas com dados ausentes
    df = df.dropna()

    # Removendo duplicatas
    df = df.drop_duplicates()

    # Convertendo colunas para o tipo correto, se necessário
    # Exemplo: df['coluna'] = df['coluna'].astype(int)

    # Outras operações de limpeza de dados, se necessário

    # Salvando o DataFrame limpo de volta para um novo arquivo CSV
    df.to_csv('./cleared_datasets/olist_products_dataset.csv', index=False)

    print('Limpeza realizada')


clean_customers()
clean_order_items()
clean_orders()
clean_products()
