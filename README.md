# EmailTrigger
automatic email trigger with direct gmail integration, simple code, and bulk sending, supporting text/html email sending

### Corpo de Email 

Aceita tipos text/html,voce pode usar o Css Inline para criar folhas de Stylo para seu Email
como voce pode ver abaixo 👇
![corpo](https://user-images.githubusercontent.com/58236600/208332298-58f20eb3-0058-4556-adae-d6232b6bfe90.png)


### Remetente/Remetentes

No campo > msg['From'],voce deve preencher com o email do remetente do email,com o codigo original ,é possivel apenas a adição de 1 remetente


### Senha de Remetente

O campo password,deve conter o token gerado pelo sistema gmail,um token de uso unico e identificado,siga os passos abaixo para gerar o Token



1º passo:
Acesse seu email tipo Gmail,acesse as configuraçoes da conta,conforme a imagem abaixo


![2](https://user-images.githubusercontent.com/58236600/208333042-9aebcedd-5b64-418f-804f-a797f965a574.png)


2º passo:

Acesse o campo Segurança,apos isso,acesse Senha dos APP

###### É de Extrema importancia que a Verificaçao de 2 etapas esteja Ativada,caso contrario,nao sera possivel acessar o campo senhas de app


![3](https://user-images.githubusercontent.com/58236600/208333257-cf3cbf33-979f-432e-b8c1-5a81a50a723e.png)

3º passo:

Após acessar senhas de app,selecione o app para o qual o token sera gerado,neste caso,Email
E em dispositivo,podera selecionar a opção que mais se adapte a seu caso,recomendo que crie um Nome personalizado


![4](https://user-images.githubusercontent.com/58236600/208333423-669f03f9-06d7-4b67-8d13-b15ccdc967cf.png)


4º passo:
Após todos essas etapas um token sera finalmente gerado,esse token deve ser colocado no codigo de envio de email,no campo correspondente (password) 


![Screenshot_1](https://user-images.githubusercontent.com/58236600/208333650-6066f2be-78f2-4fd8-8259-a2de1eecbe63.png)


### Destinatario/Destinatarios

O campo msg['To'],deve ser preenchido com o endereço do destinatario,varios endereços podem ser adicionados ao campo,bastanto serem separado por " , "
Como no exemplo abaixo 👇


![Screenshot_2](https://user-images.githubusercontent.com/58236600/208334088-8c5cc96b-8d64-466c-b863-56aadf88fb29.png)

