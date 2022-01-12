class CMDStyle:
    HEADER = '\033[95m'
    
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'

    END = '\033[0m'

def style(style: str, content: str, end: bool = True) -> str:
    return f"{style}{content}{CMDStyle.END if end else ''}"
