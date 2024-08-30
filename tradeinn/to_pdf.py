from fpdf import FPDF
import os

repo_root = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(repo_root, "logo.png")


class PDF(FPDF):
    def header(self):
        # Logo
        self.image(image_path)
        self.set_font("Arial", "B", 17)
        self.cell(60)
        self.cell(30, 10, "CATÁLOGO DE PRODUTOS", 0, 0, "C")
        self.ln(20)

    def add_product_row(self, produto):
        self.cell(30, 30, "", 1, 0, "C")
        # self.image(produto['imagem'], x=self.get_x() - 30, y=self.get_y() + 1, w=30, h=30)
        self.cell(100, 30, produto["titulo"], 1, 0, "C")
        self.cell(60, 30, produto["preco"], 1, 1, "C")
