// Lista de funcionários
const funcionarios = [
  { codigo: '001', nome: 'Francisco Pereira' },
  { codigo: '002', nome: 'Alexandre Aguado' },
  { codigo: '003', nome: 'Carlos Silva' },
  { codigo: '004', nome: 'Ana Luiza' },
  { codigo: '005', nome: 'Erick Fernandez' }
];

// Ao iniciar a pagina, carrega os registros no localStorage ou cria uma tabela vazia
const registros = JSON.parse(localStorage.getItem('pontos')) || [];

// Quando o inserir o código, preenche o nome automaticamente
document.getElementById('codigo').addEventListener('input', (e) => {
  const codigo = e.target.value;
  const funcionario = funcionarios.find(f => f.codigo === codigo);
  const nomeField = document.getElementById('nome');

  // Se encontrar o funcionário, aparece o nome no campo, senão, fica vazio
  if (funcionario) {
    nomeField.value = funcionario.nome;
  } else {
    nomeField.value = '';
  }
});

// Função para registrar os horário (entrada, saída almoço, volta almoço, saída)
function registrar(tipo) {
  const codigo = document.getElementById('codigo').value;
  const nome = document.getElementById('nome').value;
  const data = document.getElementById('data').value;

  // Verifica se os campos obrigatórios estão preenchidos
  if (!codigo || !nome || !data) return alert("Preencha código, nome e data.");

  // Procura se já existe um registro para o mesmo funcionário na mesma data
  let registro = registros.find(r => r.codigo === codigo && r.data === data);

  // Se não existir, cria um novo objeto de registro e adiciona a tabela
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

  // Registra o horário atual no campo correspondente (tipo: entrada, saída almoço, volta almoço, saída)
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

// Permite editar os horários
function editarRegistro(index) {
  const novoRegistro = { ...registros[index] };
  const campos = ['entrada', 'saidaAlmoco', 'voltaAlmoco', 'saida'];

  // Solicita novo valor ao para cada campo de horarios
  campos.forEach(campo => {
    const novoValor = prompt(`Editar ${campo} (HH:MM)`, novoRegistro[campo]);
    if (novoValor !== null) novoRegistro[campo] = novoValor;
  });

  // Atualiza o registro com os novos valores
  registros[index] = novoRegistro;
  localStorage.setItem('pontos', JSON.stringify(registros));
  exibirRegistros();
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