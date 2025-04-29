// Lista de funcionários
const funcionarios = [
  { codigo: '001', nome: 'Francisco Pereira' },
  { codigo: '002', nome: 'Alexandre Aguado' },
  { codigo: '003', nome: 'Carlos Silva' },
  { codigo: '004', nome: 'Ana Luiza' },
  { codigo: '005', nome: 'Erick Fernandez' }
];

// Carrega os registros no localStorage ou cria um array vazio
const registros = JSON.parse(localStorage.getItem('pontos')) || [];

// Quando o usuário digita um código, preenche o campo "nome" automaticamente
document.getElementById('codigo').addEventListener('input', (e) => {
  const codigo = e.target.value;
  const funcionario = funcionarios.find(f => f.codigo === codigo);
  const nomeField = document.getElementById('nome');

  // Se encontrar o funcionário, exibe o nome no campo, senão, limpa
  if (funcionario) {
    nomeField.value = funcionario.nome;
  } else {
    nomeField.value = '';
  }
});

// Função para registrar um horário (entrada, saída, etc.)
function registrar(tipo) {
  const codigo = document.getElementById('codigo').value;
  const nome = document.getElementById('nome').value;
  const data = document.getElementById('data').value;

  // Verifica se os campos obrigatórios estão preenchidos
  if (!codigo || !nome || !data) return alert("Preencha código, nome e data.");

  // Procura se já existe um registro para o mesmo funcionário na mesma data
  let registro = registros.find(r => r.codigo === codigo && r.data === data);

  // Se não existir, cria um novo objeto de registro e adiciona ao array
  if (!registro) {
    registro = {
      codigo,
      nome,
      data,
      entrada: '',
      saidaAlmoco: '',
      voltaAlmoco: '',
      saida: ''
    };
    registros.push(registro);
  }

  // Registra o horário atual no campo correspondente (tipo: entrada, saída, etc.)
  const horaAtual = new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
  registro[tipo] = horaAtual;

  // Salva os registros atualizados no localStorage
  localStorage.setItem('pontos', JSON.stringify(registros));

  // Atualiza a exibição da tabela de registros
  exibirRegistros();
}

// Exibe os registros de ponto na tabela HTML
function exibirRegistros() {
  const tbody = document.getElementById('registros');
  tbody.innerHTML = ''; // Limpa a tabela antes de atualizar

  // Cria uma linha para cada registro
  registros.forEach((r, index) => {
    tbody.innerHTML += `
      <tr>
        <td>${r.codigo}</td>
        <td>${r.nome}</td>
        <td>${r.data}</td>
        <td>${r.entrada}</td>
        <td>${r.saidaAlmoco} / ${r.voltaAlmoco}</td>
        <td>${r.saida}</td>
        <td>
          <button onclick="editarRegistro(${index})" class="btn-edit">Editar</button>
        </td>
        <td>
          <button onclick="excluirRegistro(${index})" class="btn-delete">Excluir</button>
        </td>
      </tr>
    `;
  });
}

// Permite editar manualmente os horários de um registro já existente
function editarRegistro(index) {
  const novoRegistro = { ...registros[index] };
  const campos = ['entrada', 'saidaAlmoco', 'voltaAlmoco', 'saida'];

  // Para cada campo de horário, solicita novo valor ao usuário
  campos.forEach(campo => {
    const novoValor = prompt(`Editar ${campo} (HH:MM)`, novoRegistro[campo]);
    if (novoValor !== null) novoRegistro[campo] = novoValor;
  });

  // Atualiza o registro com os novos valores
  registros[index] = novoRegistro;
  localStorage.setItem('pontos', JSON.stringify(registros));
  exibirRegistros(); // Atualiza a tabela na tela
}

// Exclui um registro após confirmação do usuário
function excluirRegistro(index) {
  if (confirm("Tem certeza que deseja excluir este registro?")) {
    registros.splice(index, 1); // Remove do array
    localStorage.setItem('pontos', JSON.stringify(registros)); // Atualiza o localStorage
    exibirRegistros(); // Atualiza a tabela
  }
}

// Exibe os registros automaticamente quando a página é carregada
window.onload = exibirRegistros;