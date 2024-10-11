# Implementação de sistema bancário
# Versão 1

## André Felipe Oliveira


Para a primeira versão do sistema, implementamos apenas 3 operações: depósito, saque e extrato.

 ### - Operações de depósito
As operações de depósito devem receber valores positivos acumulados em uma variável e devem aparecer na operação de Extrato.
### - Operações de saque
O sistema deve permitir apenas 3 operações de saques diários, com limite de R$ 500,00 para cada um.

Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.

### - Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
