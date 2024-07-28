import flet as ft

def main(page: ft.Page):
    # Configurando a página
    page.title = "Calculadora de Combustível"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Criando campos de entrada para os preços
    gasolina_input = ft.TextField(label="Preço da Gasolina (R$)", width=200)
    alcool_input = ft.TextField(label="Preço do Álcool (R$)", width=200)

    # Função para calcular qual combustível é mais vantajoso
    def calcular(e):
        try:
            preco_gasolina = float(gasolina_input.value)
            preco_alcool = float(alcool_input.value)
            if preco_alcool / preco_gasolina <= 0.7:
                resultado.value = "É mais vantajoso abastecer com Álcool."
            else:
                resultado.value = "É mais vantajoso abastecer com Gasolina."
        except ValueError:
            resultado.value = "Por favor, insira valores válidos."
        
        page.update()

    # Botão para realizar o cálculo
    calcular_button = ft.ElevatedButton(text="Calcular", on_click=calcular)

    # Campo para exibir o resultado
    resultado = ft.Text(value="Insira os preços e clique em Calcular.", size=20)

    # Adicionando os componentes à página
    page.add(
        gasolina_input,
        alcool_input,
        calcular_button,
        resultado
    )

# Executando a aplicação
ft.app(target=main)
