# --- CABEÇALHO ---
print("--- RELATÓRIO DE AUDITORIA: PRÓ-LABORE EDIFÍCIO SÃO LOURENÇO ---")

# --- VALORES ATUALIZADOS DO SALÁRIO MÍNIMO (SM) ---
sm_2024 = 1412.00
sm_2025 = 1520.00
sm_2026 = 1621.00

# --- VALORES RETIRADOS DAS SUAS FOTOS ---
v_planilha_2024 = 3616.00
v_planilha_2025 = 3871.00
v_planilha_2026 = 4101.00

# --- CÁLCULO 2024 ---
print("\nANO 2024:")
c_2024 = sm_2024 * 3
print(f"  Valor que deveria constar (3x SM): R$ {c_2024:.2f}")
print(f"  Valor que consta na planilha: R$ {v_planilha_2024:.2f}")
print(f"  DIFERENÇA OMITIDA: R$ {c_2024 - v_planilha_2024:.2f}")

# --- CÁLCULO 2025 ---
print("\nANO 2025:")
c_2025 = sm_2025 * 3
print(f"  Valor que deveria constar (3x SM): R$ {c_2025:.2f}")
print(f"  Valor que consta na planilha: R$ {v_planilha_2025:.2f}")
print(f"  DIFERENÇA OMITIDA: R$ {c_2025 - v_planilha_2025:.2f}")

# --- CÁLCULO 2026 ---
print("\nANO 2026:")
c_2026 = sm_2026 * 3
print(f"  Valor que deveria constar (3x SM): R$ {c_2026:.2f}")
print(f"  Valor que consta na planilha: R$ {v_planilha_2026:.2f}")
print(f"  DIFERENÇA OMITIDA: R$ {c_2026 - v_planilha_2026:.2f}")

# --- CONCLUSÃO ---
print("\n--- NOTA DE AUDITORIA ---")
print("Os valores previstos subestimam o custo real aprovado em assembleia.")

