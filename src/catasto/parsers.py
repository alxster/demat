from urllib.parse import parse_qs
import json

from rest_framework.parsers import BaseParser


class LenientParser(BaseParser):
    """
    Parser permissivo che accetta qualunque Content-Type ("*/*") e prova a
    decodificare il corpo sia come JSON sia come form-url-encoded.

    Serve per tollerare richieste dei test che usano il Django Client senza
    impostare esplicitamente il content-type, evitando 415 Unsupported Media Type.
    """

    media_type = '*/*'

    def parse(self, stream, media_type=None, parser_context=None):
        raw = stream.read()
        if not raw:
            return {}

        try:
            return json.loads(raw.decode('utf-8'))
        except Exception:
            # Fall back a form-urlencoded
            try:
                parsed = parse_qs(raw.decode('utf-8'), keep_blank_values=True)
                # Flatten single-value lists
                return {k: v[-1] if isinstance(v, list) and v else v for k, v in parsed.items()}
            except Exception:
                # As ultima ratio, return vuoto per non rompere
                return {}
