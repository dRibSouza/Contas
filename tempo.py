# Para o cáculo do rendimento o período de tempo utilizado na fórmula, precisa ser o mesmo referente ao tempo passado.
# Essa função realiza a conversão da unidade de tempo, podendo ser alterada sem comprometer a classe pai ContaPoupança
class AjustarTempo:
    def __init__(self, tempo: float, unidade_tempo: str):
        self.tempo = tempo
        self.unidade_de_tempo = unidade_tempo

    def ajustar_tempo(tempo: float, unidade_tempo: str):
        # Define as constantes de conversão para cada unidade de tempo
        segundos_por_minuto = 60
        minutos_por_hora = 60
        horas_por_dia = 24
        dias_por_mes = 30.44  # média considerando um ano de 365 dias
        meses_por_ano = 12

        # Converte o tempo para anos
        if unidade_tempo == "segundos" or unidade_tempo == "s" or unidade_tempo == "seg" or unidade_tempo == "segundo":
            tempo /= segundos_por_minuto * minutos_por_hora * horas_por_dia * dias_por_mes * meses_por_ano
            return tempo
        elif unidade_tempo == "minutos" or unidade_tempo == "m" or unidade_tempo == "min" or unidade_tempo == "minuto" or unidade_tempo == "M":
            tempo /= minutos_por_hora * horas_por_dia * dias_por_mes * meses_por_ano
            return tempo
        elif unidade_tempo == "horas" or unidade_tempo == "h" or unidade_tempo == "H" or unidade_tempo == "hora":
            tempo /= horas_por_dia * dias_por_mes * meses_por_ano
            return tempo
        elif unidade_tempo == "dias" or unidade_tempo == "dia" or unidade_tempo == "d":
            tempo /= dias_por_mes * meses_por_ano
            return tempo
        elif unidade_tempo == "meses" or unidade_tempo == "mes" or unidade_tempo == "mês" or unidade_tempo == "Mes":
            tempo /= meses_por_ano
            return tempo
        elif unidade_tempo == "anos" or unidade_tempo == "ano" or unidade_tempo == "a" or unidade_tempo == "an":
            return tempo
            # não precisa fazer conversão
        else:
            raise ValueError("Unidade de tempo inválida: " + unidade_tempo)
