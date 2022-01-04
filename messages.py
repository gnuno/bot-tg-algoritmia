# Helpers
def normalize_markdown(text):
    """Replace para evitar errores con caracteres especificos"""
    return text.replace("<sup>","^")\
        .replace("</sup>","")\
        .replace("<sub>","\\_")\
        .replace("</sub>","")\
        .replace('.','\\.')\
        .replace('!','\\!')\
        .replace('-','\\-')\
        .replace('+','\\+')\
        .replace('=','\\=')\
        .replace('(','\\(')\
        .replace(')','\\)')\
        .replace('[','\\[')\
        .replace(']','\\]')\
        .replace('<','\\<')\
        .replace('>','\\>')


# Messages
def help_message():
    message = "*AlgoritmiaUNO Bot* te permite estar al tanto del ultimo desafio de programacion y estara al pendiente de varios eventos para notificarnos!\n\n"
    message += "*/help* - Muestra este mensaje.\n"
    message += "*/challenge* - Obtiene y muestra el desafio actual. Le podes pasar un numero para obtener un desafio especifico\n"
    message += "*/all* - Muestra todos los nombres de desafios con su id.\n"
    message += f"\nEste bot fue posible y llevado a cabo gracias a GNUno, cualquier consulta o pregunta hacela aquí: https://t.me/gnuno\_merlo."
    return normalize_markdown(message)