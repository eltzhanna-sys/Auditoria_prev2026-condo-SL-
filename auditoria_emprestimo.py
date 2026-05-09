# --- Dados do Empréstimo Condodata ---
parcela_contrato = 2967.00
parcela_previsao = 3028.00
total_parcelas = 48

# --- Cálculos ---
diferenca_mensal = parcela_previsao - parcela_contrato
total_excedente_contrato = diferenca_mensal * total_parcelas

print("--- RELATÓRIO: EMPRÉSTIMO CONDODATA ---")
print(f"Parcela real do contrato: R$ {parcela_contrato:.2f}")
print(f"Parcela na previsão orçamentária: R$ {parcela_previsao:.2f}")
print(f"Diferença cobrada a maior por mês: R$ {diferenca_mensal:.2f}")
print("-" * 40)
print(f"VALOR TOTAL EXCEDENTE (ao final de 48x): R$ {total_excedente_contrato:.2f}")

if total_excedente_contrato > 0:
    print("\nALERTA: A previsão está arrecadando valores acima do custo do contrato.")