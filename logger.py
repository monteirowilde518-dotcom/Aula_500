import logging
from typing import Protocol

logger = logging.getLogger(__name__)


class Notificador(Protocol):
    async def enviar(self, destinatario: str, assunto: str, corpo: str) -> None: ...


class NotificadorLog:
    """Implementação de desenvolvimento: só registra no log."""

    async def enviar(self, destinatario: str, assunto: str, corpo: str) -> None:

        logging.info("e-mail enviado para %s: %s", destinatario, assunto)