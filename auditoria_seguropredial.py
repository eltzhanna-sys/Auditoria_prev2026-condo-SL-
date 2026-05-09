# Dados Reais (Contrato/Apólice)
valor_parcela_real = 976.91
qtd_parcelas = 6
total_anual_real = valor_parcela_real * qtd_parcelas

# Dados da Previsão Orçamentária 2026 (Imagem WhatsApp)
previsao_mensal_unitaria = 501.00
# O documento somou esse valor apenas 1 vez no total anual de R$ 115.447
total_anual_provisionado = 501.00 

# Cálculos de Discrepância
deficit_anual = total_anual_real - total_anual_provisionado
erro_fluxo_caixa_mensal = valor_parcela_real - previsao_mensal_unitaria

print(f"--- RELATÓRIO TÉCNICO: SEGURO PREDIAL ED. SÃO LOURENÇO ---")
print(f"Valor Real da Parcela (6x): R$ {valor_parcela_real}")
print(f"Total Anual Devido: R$ {total_anual_real:.2f}")
print(f"Valor Provisionado no Orçamento: R$ {total_anual_provisionado}")
print(f"-------------------------------------------------------")
print(f"DÉFICIT ANUAL CONSOLIDADO: R$ {deficit_anual:.2f}")
print(f"DÉFICIT NO FLUXO MENSAL (6 meses): R$ {erro_fluxo_caixa_mensal:.2f}")