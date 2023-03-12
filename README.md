# FactoryMethod
Apresentação do Padrão de Projeto FactoryMethod em Python (Design Patterns) - Programação Orientada a Objeto

Desenvolvedores: 
- João Victor Lopes Silva (https://github.com/Joao-Victor1)
- Larissa de Oliveira Santos (https://github.com/Larissa-Santos16)

O programa inicializa com um menu de seleção, mostrando para usuário as opções de inicializar o programa com tecla A ou sair com a tecla Q. 
No caso do usuário selecionar A: O programa irá pedir para entrar com o Nome e a Relação com a instituição (sendo as opções: Aluno, Professor, Coordenador, Diretor, Administrativo ou Vestibulando).
o programa irá efetuar uma verificação e se a relação for autenticada, aparecerá a mensagem: XXXXXXXX tem relação com a instituição como XXXXXXXXXXXXX. Se não for possível autenticar a relação o programa exibirá a mensagem: XXXXXXXX não tem nenhuma relação com a instituição, acompanhar até a secretaria
No caso do usuário selecionar Q: O programa terminará, e apresentará a mensagem: saindo

# Código

O código funciona com o factory method utilizando a biblioteca ABC (Abstract Base Class)
para definição de uma interface. A interface vai receber como parâmetros o nome e a relação 
do usuário e simular uma verificação no sistema para permitir a passagem pela portaria,
que por sua vez é classe que vai criar os objetos de relação e retornar as mensagens do sistema para o usuário.

# Factory Method

Na programação orientada a objeto (POO), uma fábrica ou Factory é um objeto para a criação de outros objetos – formalmente uma fábrica é uma função ou método que retorna os objetos de uma classe ou protótipo variável
