import pandas as pd

def extract_data(filepath):
    df = pd.read_csv(filepath)
    df['news'] = ""
    return df

def generate_marketing_message(name):
    return f"{name}, investir hoje é o primeiro passo para um futuro financeiro mais seguro e próspero!"

def transform_data(df):
    df['news'] = df['name'].apply(generate_marketing_message)
    return df

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Arquivo salvo com sucesso em: {output_path}")

if __name__ == "__main__":
    input_path = "data/SDW2023.csv"
    output_path = "output/marketing_messages.csv"

    df_extracted = extract_data(input_path)
    df_transformed = transform_data(df_extracted)
    load_data(df_transformed, output_path)
