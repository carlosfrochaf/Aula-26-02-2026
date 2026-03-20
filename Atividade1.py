

RESERVADAS = {
    "if", "else", "while", "for", "return", 
    "int", "System", "out", "print", "public", "class"
}

codigo = """
public class StarRectangle {
    public void printRectangle(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(" * ");
            }
            System.out.println();
        }
    }
}
"""


tokens = re.findall(r'\b[A-Za-z_]\w*\b', codigo)


reservadas_vistas = {t for t in tokens if t in RESERVADAS}
identificadores = {t for t in tokens if t not in RESERVADAS}

# 4. Saída Formatada
print(f"{' CATEGORIA ':^30}")
print("-" * 30)
print(f"Reservadas ({len(reservadas_vistas)}): {', '.join(reservadas_vistas)}")
print(f"Identificadores ({len(identificadores)}): {', '.join(identificadores)}")
