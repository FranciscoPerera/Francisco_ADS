# Folha de Ponto
Este projeto tem como objetivo criar um sistema simples de folha de ponto para registrar as entradas e saídas dos funcionários, incluindo horários de entrada, saída para almoço, volta do almoço e saída do expediente.

## Funcionalidades

- **Registro de horários**: Permite registrar os horários de entrada, saída para almoço, volta do almoço e saída do expediente.
- **Visualização dos registros**: Mostra todos os registros feitos para os funcionários no formato de tabela.
- **Edição e exclusão de registros**: É possível editar ou excluir registros existentes.
- **Armazenamento local**: Utiliza o `localStorage` para salvar os registros localmente no navegador.

## Como Usar

1. **Entrada de dados**: 
   - Preencha o **código do funcionário** (previamente cadastrado) e a **data** do registro.
   - O nome do funcionário será preenchido automaticamente com base no código inserido.
   
2. **Registrar horários**:
   - Clique nos botões de "Entrada", "Saída Almoço", "Volta Almoço" ou "Saída" para registrar os respectivos horários.
   
3. **Editar ou excluir registros**:
   - A tabela exibirá todos os registros feitos.
   - Você pode editar ou excluir qualquer registro clicando nos botões correspondentes.

## Tecnologias Utilizadas

- **HTML**: Marcação do conteúdo da página.
- **Tailwind CSS**: Framework de CSS para estilização.
- **JavaScript**: Manipulação da lógica de dados e interação com o `localStorage`.