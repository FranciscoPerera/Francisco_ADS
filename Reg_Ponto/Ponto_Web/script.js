const funcionarios = [
  { codigo: '001', nome: 'Francisco Pereira' },
  { codigo: '002', nome: 'Alexandre Aguado' },
  { codigo: '003', nome: 'Carlos Silva' },
  { codigo: '004', nome: 'Ana Luiza' },
  { codigo: '005', nome: 'Erick Fernandez' }
];

const registros = JSON.parse(localStorage.getItem('pontos')) || [];

document.getElementById('codigo').addEventListener('input', (e) => {
  const codigo = e.target.value;
  const funcionario = funcionarios.find(f => f.codigo === codigo);
  const nomeField = document.getElementById('nome');

  if (funcionario) {
    nomeField.value = funcionario.nome;
  } else {
    nomeField.value = '';
  }
});

function registrar(tipo) {
  const codigo = document.getElementById('codigo').value;
  const nome = document.getElementById('nome').value;
  const data = document.getElementById('data').value;

  if (!codigo || !nome || !data) return alert("Preencha código, nome e data.");

  let registro = registros.find(r => r.codigo === codigo && r.data === data);
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

  const horaAtual = new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
  registro[tipo] = horaAtual;
  localStorage.setItem('pontos', JSON.stringify(registros));
  exibirRegistros();
}

function exibirRegistros() {
  const tbody = document.getElementById('registros');
  tbody.innerHTML = '';
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

function editarRegistro(index) {
  const novoRegistro = { ...registros[index] };
  const campos = ['entrada', 'saidaAlmoco', 'voltaAlmoco', 'saida'];

  campos.forEach(campo => {
    const novoValor = prompt(`Editar ${campo} (HH:MM)`, novoRegistro[campo]);
    if (novoValor !== null) novoRegistro[campo] = novoValor;
  });

  registros[index] = novoRegistro;
  localStorage.setItem('pontos', JSON.stringify(registros));
  exibirRegistros();
}

function excluirRegistro(index) {
  if (confirm("Tem certeza que deseja excluir este registro?")) {
    registros.splice(index, 1);
    localStorage.setItem('pontos', JSON.stringify(registros));
    exibirRegistros();
  }
}

window.onload = exibirRegistros;
