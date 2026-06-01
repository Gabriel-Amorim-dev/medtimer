from datetime import datetime, timedelta


def ajustar_para_horario_vigilia(usuario, proximo_horario):
    """Pushes a datetime forward past the user's sleep window."""
    if not usuario.horario_sono_inicio or not usuario.horario_sono_fim:
        return proximo_horario

    for _ in range(10):
        hora_atual = proximo_horario.time()
        inicio = usuario.horario_sono_inicio
        fim = usuario.horario_sono_fim

        if inicio > fim:  # sleep crosses midnight (e.g. 22:00 → 06:00)
            if hora_atual >= inicio or hora_atual < fim:
                if hora_atual >= inicio:
                    data_ajustada = proximo_horario.date() + timedelta(days=1)
                else:
                    data_ajustada = proximo_horario.date()
                proximo_horario = datetime.combine(
                    data_ajustada, fim, tzinfo=proximo_horario.tzinfo
                )
                continue
        else:  # sleep within same day (e.g. 13:00 → 15:00)
            if inicio <= hora_atual < fim:
                proximo_horario = datetime.combine(
                    proximo_horario.date(), fim, tzinfo=proximo_horario.tzinfo
                )
                continue
        break

    return proximo_horario