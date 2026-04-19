valor_kwh = 0.65
tempo_uso_horas = 24
potencia_watts = 500

consumo_total = (potencia_watts / 1000) * tempo_uso_horas
custo_final = consumo_total * valor_kwh

print(f"O consumo total é de {consumo_total} kWh")
print(f"O custo total da operação é R$ {custo_final}"
