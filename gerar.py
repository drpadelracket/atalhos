#!/usr/bin/env python3
"""Gera mensagens.yml (Espanso) a partir das mensagens padrao (tabela MENSAGENS, base ESCRI).

Cada atalho: ;nome (PT), ;nomeen (EN), ;nomees (ES). Disparam ao carregar em espaco.
Correr: python3 gerar.py
"""
import re
import yaml

M = []  # (atalho, situacao, pt, en, es)


def add(trigger, situacao, pt=None, en=None, es=None):
    M.append((trigger, situacao, pt, en, es))


# ---------------- RAQUETE PRONTA / PAGAMENTOS ----------------
add("pronta", "RAQUETE PRONTA",
"""Viva 😁

A sua raquete está pronta.
Enviamos e-mail mas pode não ter visto.

Pode fazer o checkout da mesma aqui:

https://portal.drpadelracket.com

Pedimos, encarecidamente, que envie o comprovativo de pagamento após o mesmo ser efetuado. 👍""",
"""Hello 😁

Your racket is ready.

We have sent you an email, but you may not have seen it.

You can complete the checkout here:

https://portal.drpadelracket.com

We kindly ask you to send us the payment receipt once the payment has been completed 👍""",
"""¡Hola 😁!

Tu pala ya está lista.

Puedes hacer el checkout aquí:
https://portal.drpadelracket.com

Si el pago se realiza por Revolut, te pedimos encarecidamente que envíes el comprobante de pago una vez efectuado. 👍""")

add("prontaprotetor", "RAQUETE PRONTA - ACONSELHAR PROTETOR",
"""Viva 😁
A sua raquete está pronta.
Pode fazer o checkout da mesma aqui: https://portal.drpadelracket.com

Neste caso, para proteger a pintura e a raquete, aconselhamos a seleção de um protetor novo (no link acima).

Pedimos, encarecidamente, que envie o comprovativo de pagamento após o mesmo ser efetuado. 👍""",
"""Hello 😁

Your racket is ready.

You can complete the checkout here:
https://portal.drpadelracket.com

In this case, to protect both the paintwork and the racket, we recommend selecting a new protector (available via the link above).

We kindly ask you to send us the payment receipt once the payment has been completed 👍""",
"""¡Hola 😁!

Su pala ya está lista.

Puedes hacer el checkout aquí:
https://portal.drpadelracket.com

En este caso, para proteger la pintura y la pala, le recomendamos seleccionar un protector nuevo (disponible en el mismo enlace).

Le pedimos encarecidamente que nos envíe el comprobante de pago una vez realizado. 👍""")

add("prontasemprotetor", "RAQUETE PRONTA - CHEGOU SEM PROTETOR",
"""Viva 😁
A sua raquete está pronta.
Pode fazer o checkout da mesma aqui: https://portal.drpadelracket.com

A sua raquete chegou-nos sem protetor. Recomendamos aplicar um, que ajuda a proteger a pintura e a raquete de impactos. No checkout pode adicioná-lo por apenas 5€.

Pedimos, encarecidamente, que envie o comprovativo de pagamento após o mesmo ser efetuado. 👍""",
"""Hello 😁

Your racket is ready.

You can complete the checkout here:
https://portal.drpadelracket.com

Your racket arrived without a protector. We recommend adding one, which helps protect the paint and the racket from impacts. At checkout you can add it for just 5€.

We kindly ask you to send us the payment receipt once the payment has been completed 👍""",
"""¡Hola 😁!

Su pala ya está lista.

Puede hacer el checkout aquí:
https://portal.drpadelracket.com

Su pala nos llegó sin protector. Le recomendamos colocar uno, que ayuda a proteger la pintura y la pala de los impactos. En el checkout puede añadirlo por solo 5€.

Le pedimos encarecidamente que nos envíe el comprobante de pago una vez realizado. 👍""")

add("prontaremovido", "RAQUETE PRONTA - PROTETOR REMOVIDO NA REPARAÇÃO",
"""Viva 😁
A sua raquete está pronta.
Pode fazer o checkout da mesma aqui: https://portal.drpadelracket.com

Neste caso, para podermos avançar com a reparação, foi necessário remover o protetor existente.
Assim sendo, para proteger a pintura e a raquete, aconselhamos a seleção de um protetor novo (no link acima).

Pedimos, encarecidamente, que envie o comprovativo de pagamento após o mesmo ser efetuado. 👍""",
"""Hello 😁

Your racket is ready.

You can complete the checkout here:
https://portal.drpadelracket.com

In this case, in order to proceed with the repair, it was necessary to remove the existing protector.

Therefore, to protect both the paintwork and the racket, we recommend selecting a new protector (available via the link above).

We kindly ask you to send us the payment receipt once the payment has been completed 👍""",
"""¡Hola 😁!

Su pala ya está lista.

Puede hacer el checkout aquí:
https://portal.drpadelracket.com

En este caso, para poder avanzar con la reparación, fue necesario retirar el protector existente.

Por ello, para proteger la pintura y la pala, le recomendamos seleccionar un protector nuevo (disponible en el mismo enlace).

Le pedimos encarecidamente que nos envíe el comprobante de pago una vez realizado. 👍""")

add("prontagrip", "RAQUETE PRONTA - ACONSELHAR GRIP",
"""Viva 😁

A sua raquete está pronta.
Pode fazer o checkout da mesma aqui: https://portal.drpadelracket.com

Neste caso, percebemos que o seu grip está desgastado, assim aconselhamos a seleção de um novo (no link acima).

Pedimos, encarecidamente, que envie o comprovativo de pagamento após o mesmo ser efetuado. 👍""",
"""Hello 😁

Your racket is ready.

You can complete the checkout here:
https://portal.drpadelracket.com

In this case, we noticed that your grip is worn, so we recommend selecting a new one (available via the link above).

We kindly ask you to send us the payment receipt once the payment has been completed 👍""",
"""Hola 😁!

Su pala ya está lista.
Puede realizar el checkout en el siguiente enlace: https://portal.drpadelracket.com

En este caso, hemos notado que su grip está desgastado, por lo que le recomendamos seleccionar uno nuevo (en el mismo enlace anterior).

Le pedimos, por favor, que envíe el comprobante de pago una vez realizado. 👍""")

add("prontagarantia", "RAQUETE PRONTA - GARANTIA OU OFERTA",
"""Viva 😁

A sua raquete está pronta.
Pode fazer o checkout da mesma aqui: https://portal.drpadelracket.com""",
"""Hello 😁

Your racket is ready.

Please let us know how you would like it to be shipped back.""",
"""Hola 😁
Su raqueta está lista.
Enviamos un correo electrónico, pero puede que no lo haya visto.
Confírmenos por favor cómo desea el reenvío.""")

add("tardio", "PAGAMENTO TARDIO / RAQUETES SEM PAGAMENTO",
"""Viva,

A sua raquete está pronta. A mesma encontra-se neste estado há algum tempo.

Por favor, solicitamos que realize o pagamento e que nos envie o comprovativo assim que for efetuado. 👍

Pode fazer o checkout da mesma aqui:
https://portal.drpadelracket.com

Posto isto, iremos expedir a sua raquete.

Gratos pela sua compreensão 😀""",
"""Hello,

Your racket is ready and has been in this status for some time.

We kindly ask you to proceed with the payment and send us the proof of payment once it has been completed 👍

You can complete the checkout here:
https://portal.drpadelracket.com

Once this is done, we will proceed with shipping your racket.

Thank you for your understanding 😀""",
"""Hola,

Su raqueta ya está lista y lleva en este estado desde hace algún tiempo.

Le solicitamos, por favor, que realice el pago y nos envíe el comprobante tan pronto como lo haya efectuado. 👍

Puede hacer el checkout aquí:
https://portal.drpadelracket.com

Una vez recibido, procederemos al envío de su raqueta.

¡Gracias por su comprensión! 😀""")

add("naoreclamada", "PAGAMENTO TARDIO / NÃO RECLAMADA",
"""Viva,

A sua raquete está pronta e disponível há algum tempo.

Para que possamos proceder com o envio, pedimos gentilmente que efetue o pagamento e nos envie o comprovativo até ao final da semana.
Caso não demonstre intenção de reaver a raquete, iremos considerá-la como não reclamada e poderemos descartá-la para evitar acumulação no armazém.

Pode realizar o pagamento diretamente aqui:
https://portal.drpadelracket.com

Agradecemos a sua compreensão e estamos à disposição para qualquer dúvida! 😀""",
"""Hello,

Your racket has been ready and available for some time.

In order for us to proceed with shipping, we kindly ask you to complete the payment and send us the proof of payment by the end of the week.

If no intention to retrieve the racket is shown, it will be considered unclaimed and may be discarded to avoid accumulation in our warehouse.

You can complete the payment directly here:
https://portal.drpadelracket.com

Thank you for your understanding, and we remain at your disposal for any questions! 😀""",
"""Hola,

Su raqueta ya está lista y disponible desde hace algún tiempo.

Para que podamos proceder con el envío, le rogamos que realice el pago y nos envíe el comprobante antes de que finalice la semana.
En caso de no manifestar intención de recuperar la raqueta, la consideraremos como no reclamada y podremos desecharla para evitar acumulación en el almacén.

Puede realizar el pago directamente en el siguiente enlace:
https://portal.drpadelracket.com

¡Agradecemos su comprensión y quedamos a su disposición para cualquier consulta! 😀""")

add("tardioclube", "PAGAMENTO TARDIO - CLUBES",
"""Viva,

Esperamos que esteja tudo bem consigo!

Passamos por aqui para saber se deseja receber de volta a sua raquete, que já se encontra pronta há algum tempo.

Caso tenha interesse, basta efetuar o pagamento e enviar-nos o respetivo comprovativo, para que possamos avançar com o envio.

Se, por outro lado, já não fizer sentido reaver a raquete, pedimos apenas que nos dê essa indicação, para podermos organizar o nosso espaço em armazém.

O pagamento pode ser realizado diretamente através do link abaixo:

https://portal.drpadelracket.com

Ficamos a aguardar o seu feedback e, como sempre, estamos à disposição para qualquer esclarecimento.

Cumprimentos""",
"""Hello,

We hope all is well with you!

We are reaching out to ask whether you would like to receive your racket back, as it has been ready for some time.

If you are interested, simply make the payment and send us the receipt so we can proceed with the shipping.

If, on the other hand, it no longer makes sense to get the racket back, please just let us know so we can organise our warehouse space.

The payment can be made directly through the link below:

https://portal.drpadelracket.com

We look forward to your feedback and, as always, we are available for any questions.

Best regards""",
"""Hola,

¡Esperamos que todo vaya bien!

Le escribimos para saber si desea recibir de vuelta su pala, que ya está lista desde hace algún tiempo.

Si le interesa, solo tiene que realizar el pago y enviarnos el comprobante para que podamos proceder con el envío.

Si, por el contrario, ya no tiene sentido recuperar la pala, le pedimos simplemente que nos lo indique para poder organizar nuestro espacio en el almacén.

El pago puede realizarse directamente a través del siguiente enlace:

https://portal.drpadelracket.com

Quedamos a la espera de su respuesta y, como siempre, estamos a su disposición para cualquier aclaración.

Saludos cordiales""")

add("pago", "PAGAMENTO RECEBIDO",
"""Obrigado 🙏

Vamos aplicar o acabamento final à raquete (verniz) e logo que o processo de cura esteja terminado, faremos o envio da raquete.
Irá receber um tracking code no e-mail assim que a raquete for enviada.

Pode consultar mais serviços para si aqui: https://www.drpadelracket.com""",
"""Thank you 🙏

We are going to apply the final finish to the racket (varnish), and as soon as the curing process is complete, we will ship it.
You will receive a tracking code by email as soon as the racket has been shipped.

You can check more services for you here: https://www.drpadelracket.com/en""",
"""Gracias 🙏

Recibirá un código de seguimiento por correo electrónico en cuanto su raqueta sea enviada.

Puede consultar más servicios disponibles para usted aquí:
https://www.drpadelracket.com""")

add("metodos", "MÉTODOS DE PAGAMENTO",
"""O pagamento é feito quando a raquete estiver pronta.
Pode ser feito por MBWAY, referência MB, etc.""",
"""The payment is made once the racket is ready.

It can be made via Revolut, bank transfer or Stripe.""",
"""El pago podrá ser por Revolut, transferencia o tarjeta (Stripe), después de que la pala esté lista.""")

add("nif", "NIF", "518123189")
add("nib", "NIB", "PT50001800036232353002020")

add("stripe", "LINKS STRIPE PAGAMENTO (ESPANHA)",
"""https://buy.stripe.com/6oUbJ3d2l0pu7lO8KccMM0a - 34€

https://buy.stripe.com/14A00l2nH7RW5dGe4wcMM0e - 39€

https://buy.stripe.com/5kQ7sNd2l4FK21u5y0cMM0f - 44€

https://buy.stripe.com/dRmcN7gex4FK49C2lOcMM0c - 49€

https://buy.stripe.com/8x24gB0fz3BG49Cd0scMM0d - 54€""")

# ---------------- PORTAL ----------------
add("portal", "ACEDER AO PORTAL",
"""Viva,
Pode acompanhar o estado da sua raquete no nosso portal:
https://portal.drpadelracket.com
Para entrar só precisa do e-mail que nos indicou 😁""",
"""Hello,
You can follow the status of your racket on our portal:
https://portal.drpadelracket.com
To log in, you only need the email you gave us 😁""",
"""Hola,
Puede seguir el estado de su pala en nuestro portal:
https://portal.drpadelracket.com
Para entrar solo necesita el e-mail que nos indicó 😁""")

add("registo", "RAQUETE ENTREGUE/ENVIADA PELO CLIENTE (REGISTO NO PORTAL)",
"""Viva

Para registarmos o seu serviço, basta usar o nosso portal:
👉 https://portal.drpadelracket.com

1. Entre com o seu e-mail
Se for a primeira vez, carregue em "Criar ficha de cliente" e preencha os seus dados. No fim, o portal leva-o direto ao passo 2.

2. Registe a sua raquete
Carregue em "+ Registar raquete", adicione fotos, escolha a marca e indique onde deixou a raquete.
Tem mais do que uma? Faça um registo para cada raquete.

⚠️ IMPORTANTE: criar a ficha não chega. A raquete só fica registada depois do passo 2.

No mesmo portal pode acompanhar cada etapa da reparação e, quando estiver pronta, escolher a entrega e pagar.

Por favor, confirme assim que concluir.""",
"""To register your service, simply use our portal:
👉 https://portal.drpadelracket.com

1. Enter your email address
If this is your first time, click on ‘Create customer profile’ and fill in your details. Once you’ve done that, the portal will take you straight to step 2.

2. Register your racket
Click on “+ Register racket”, add photos, choose the brand and indicate where you left the racket.
Do you have more than one? Create a separate registration for each racket.

⚠️ IMPORTANT: simply creating the profile isn’t enough. The racket is only registered once you’ve completed step 2.

On the same portal, you can track each stage of the repair and, once it’s ready, choose your delivery option and pay.

Please confirm once you’ve finished.""",
"""Hola

Para registrar su servicio, solo tiene que usar nuestro portal:
👉 https://portal.drpadelracket.com

1. Entre con su e-mail
Si es la primera vez, pulse en "Crear ficha de cliente" y rellene sus datos. Al terminar, el portal le lleva directamente al paso 2.

2. Registre su pala
Pulse en "+ Registrar pala", añada fotos, elija la marca e indique dónde dejó la pala.
¿Tiene más de una? Haga un registro para cada pala.

⚠️ IMPORTANTE: crear la ficha no es suficiente. La pala solo queda registrada después del paso 2.

En el mismo portal puede seguir cada etapa de la reparación y, cuando esté lista, elegir la entrega y pagar.

Por favor, confírmenos cuando haya terminado.""")

add("obrigadoform", "AGRADECIMENTO PÓS PREENCHIMENTO FORM",
"""Já recebemos os registos e está tudo bem preenchido, obrigado 🙏
Sobre os prazos de recolha:
- Clubes Parceiros: recolhemos em até 4 dias úteis.
- Ponto DPD: depende do timing da transportadora.

Tem urgência? Serviço Express por 14€:
- Clube Parceiro - Recolha no dia útil seguinte + prioridade máxima.
- Ponto DPD - Prioridade máxima assim que a raquete chegar às nossas instalações.

Pode consultar mais serviços para si durante o processo aqui:
https://www.drpadelracket.com/

Assim que a raquete estiver pronta receberá e-mail e, caso não o veja, mensagem via WhatsApp 😁""",
"""We have already received the registrations and everything is filled in correctly, thank you 🙏

You can check out more services for you during the process here:
https://www.drpadelracket.com/en

As soon as the racket is ready, you will receive an email and, if you don’t see it, a message via WhatsApp 😁""",
"""Ya hemos recibido los registros y todo está correctamente completado, gracias! 🙏

Puede consultar más servicios disponibles para usted durante el proceso aquí:
https://www.drpadelracket.com/es-es

En cuanto la raqueta esté lista, recibirá un correo electrónico y, si no lo visualiza, un mensaje por WhatsApp 😁""")

add("maqueteversao", "MAQUETE - NOVA VERSÃO",
"""Viva,
A proposta de maquete da sua raquete já está no portal. Pode aprová-la ou pedir alterações lá:
https://portal.drpadelracket.com""",
"""Hello,
The mockup proposal for your racket is now on the portal. You can approve it or ask for changes there:
https://portal.drpadelracket.com""",
"""Hola,
La propuesta de maqueta de su pala ya está en el portal. Puede aprobarla o pedir cambios allí:
https://portal.drpadelracket.com""")

add("maquetemsg", "MAQUETE - NOVA MENSAGEM",
"""Viva,
Tem uma nova mensagem sobre a maquete da sua raquete no portal:
https://portal.drpadelracket.com""",
"""Hello,
You have a new message about your racket mockup on the portal:
https://portal.drpadelracket.com""",
"""Hola,
Tiene un nuevo mensaje sobre la maqueta de su pala en el portal:
https://portal.drpadelracket.com""")

# ---------------- ORÇAMENTOS ----------------
add("fotos", "ORÇAMENTAR - PEDIR FOTOS",
"""Viva,
Para receber um orçamento basta enviar fotos da sua raquete (zona danificada e, idealmente, frente, verso, laterais, topo e coração).

Posto isto, iremos explicar os passos seguintes 🙂
Muito obrigado!""",
"""Hello,
To receive a quote, simply send us photos of your racket (damaged area and, ideally, front, back, sides, top and heart).

After that, we'll explain the next steps 🙂
Thank you very much!""",
"""Hola,
Para recibir un presupuesto, solo tiene que enviarnos fotos de su pala (zona dañada e, idealmente, delante, detrás, laterales, parte superior y corazón).

A partir de ahí, le explicaremos los siguientes pasos 🙂
¡Muchas gracias!""")

add("orc", "ORÇAMENTO REPARAÇÃO (trocar valor)",
"""Viva,

Reparação estrutural: 39€
-Recupera a performance (perdida com o dano).
-Inclui acabamento estético: aplicação de cor primária na zona reparada
-Inclui entrega/recolha
-Inclui garantia de 4 meses.

Acabamento estético premium - replica os padrões originais (opcional)
Sujeito a avaliação/orçamentação após a reparação.

Se desejar avançar indique-me por favor para lhe explicar como funciona a recolha.""",
"""Hello,

Structural repair: €39
-Restores performance (lost due to the damage).
-Includes cosmetic finish: base colour applied to the repaired area
-Includes pick-up/delivery
-Includes a 4-month warranty.

Premium cosmetic finish - replicates the original patterns (optional)
Subject to assessment/quote after the repair.

If you would like to proceed, please let me know and I will explain how the pick-up works.""",
"""Hola,

Reparación estructural: 39 €
-Recupera la performance (perdida con el daño).
-Incluye acabado estético: aplicación de color base en la zona reparada
-Incluye recogida/entrega
-Incluye garantía de 4 meses.

Acabado estético premium - replica los diseños originales (opcional)
Sujeto a evaluación/presupuesto después de la reparación.

Si desea avanzar, indíqueme por favor para explicarle cómo funciona la recogida.""")

add("orcsempintura", "ORÇAMENTO REPARAÇÃO S/PINTURA",
"""Viva,

Reparação estrutural: 39€
-Recupera a performance (perdida com o dano).
-Inclui pintura base (uma única cor) - neste caso não é possível replicar os padrões originais.
-Inclui entrega/recolha
-Inclui garantia de 4 meses.

Se desejar avançar indique-me por favor para lhe explicar como funciona a recolha.""",
"""Hello,

Structural repair: €39
-Restores performance (lost due to the damage).
-Includes base paint (a single colour) - in this case it is not possible to replicate the original patterns.
-Includes pick-up/delivery
-Includes a 4-month warranty.

If you would like to proceed, please let me know and I will explain how the pick-up works.""",
"""Hola,

Reparación estructural: 39 €
-Recupera la performance (perdida con el daño).
-Incluye pintura base (un único color) - en este caso no es posible replicar los diseños originales.
-Incluye recogida/entrega
-Incluye garantía de 4 meses.

Si desea avanzar, indíqueme por favor para explicarle cómo funciona la recogida.""")

add("orcsemgarantia", "ORÇAMENTO S/GARANTIA (trocar valor)",
"""Viva,

Reparação estrutural: 34€
-Recupera a performance (perdida com o dano), neste caso não a 100%
-Inclui acabamento estético: aplicação de cor primária na zona reparada
-Inclui entrega/recolha
-Neste caso não inclui a garantia habitual de 4 meses.

Acabamento estético premium - replica os padrões originais (opcional)
Sujeito a avaliação/orçamentação após a reparação.

Se desejar avançar indique-me por favor para lhe explicar como funciona a recolha.""",
"""Hello,

Structural repair: €34
-Restores performance (lost due to the damage), in this case not 100%
-Includes cosmetic finish: base colour applied to the repaired area
-Includes pick-up/delivery
-In this case it does not include our usual 4-month warranty.

Premium cosmetic finish - replicates the original patterns (optional)
Subject to assessment/quote after the repair.

If you would like to proceed, please let me know and I will explain how the pick-up works.""",
"""Hola,

Reparación estructural: 34 €
-Recupera la performance (perdida con el daño), en este caso no al 100%
-Incluye acabado estético: aplicación de color base en la zona reparada
-Incluye recogida/entrega
-En este caso no incluye la garantía habitual de 4 meses.

Acabado estético premium - replica los diseños originales (opcional)
Sujeto a evaluación/presupuesto después de la reparación.

Si desea avanzar, indíqueme por favor para explicarle cómo funciona la recogida.""")

add("orclimite", "ORÇAMENTO NO LIMITE + AJUDA COMPRAR",
"""Viva,

Está um pouco no limite daquilo que costumamos aconselhar reparar (contra nós falamos), já que está muito partida numa zona de contacto com a bola.

Se mesmo assim desejar avançar:
Reparação estrutural: X€
-Recupera a performance, neste caso não a 100%
-Inclui acabamento estético: aplicação de cor primária na zona reparada
-Inclui entrega/recolha
-Neste caso não inclui a garantia habitual de 4 meses.

Como alternativa, podemos ajudar a comprar uma raquete nova abaixo do preço de mercado, ou fazer uma 100% personalizada com a nossa produção própria.""",
"""Hello,

This is a bit on the limit of what we usually recommend repairing (even if it goes against our own interest), as it is badly broken in an area that makes contact with the ball.

If you would still like to proceed:
Structural repair: X€
-Restores performance, in this case not 100%
-Includes cosmetic finish: base colour applied to the repaired area
-Includes pick-up/delivery
-In this case it does not include our usual 4-month warranty.

As an alternative, we can help you buy a new racket below market price, or make a 100% customised one with our own production.""",
"""Hola,

Está un poco en el límite de lo que solemos aconsejar reparar (aunque vaya en contra de nuestro interés), ya que está muy rota en una zona de contacto con la bola.

Si aun así desea avanzar:
Reparación estructural: X€
-Recupera la performance, en este caso no al 100%
-Incluye acabado estético: aplicación de color base en la zona reparada
-Incluye recogida/entrega
-En este caso no incluye la garantía habitual de 4 meses.

Como alternativa, podemos ayudarle a comprar una pala nueva por debajo del precio de mercado, o hacer una 100% personalizada con nuestra producción propia.""")

add("orccork", "ORÇAMENTO CORK (trocar valor)",
"""Viva,

Reparação estrutural: 49€ - 54€
-Recupera a performance (perdida com o dano).
-Inclui acabamento estético - aplicação local de pintura texturizada aproximada à original.
-Inclui entrega/recolha
-Inclui garantia de 4 meses.

Acabamento estético premium (opcional)
Sujeito a avaliação/orçamentação após a reparação.

Se desejar avançar indique-me por favor para lhe explicar como funciona a recolha.""",
"""Hello,

Structural repair: €49 - €54
-Restores performance (lost due to the damage).
-Includes cosmetic finish - local application of textured paint close to the original.
-Includes pick-up/delivery
-Includes a 4-month warranty.

Premium cosmetic finish (optional)
Subject to assessment/quote after the repair.

If you would like to proceed, please let me know and I will explain how the pick-up works.""",
"""Hola,

Reparación estructural: 49 € - 54 €
-Recupera la performance (perdida con el daño).
-Incluye acabado estético - aplicación local de pintura texturizada aproximada a la original.
-Incluye recogida/entrega
-Incluye garantía de 4 meses.

Acabado estético premium (opcional)
Sujeto a evaluación/presupuesto después de la reparación.

Si desea avanzar, indíqueme por favor para explicarle cómo funciona la recogida.""")

add("orccorksemgarantia", "ORÇAMENTO CORK S/ GARANTIA (trocar valor)",
"""Viva,

Reparação estrutural: 49€
-Recupera a performance (perdida com o dano), neste caso não a 100%
-Inclui acabamento estético - aplicação local de pintura texturizada aproximada à original.
-Inclui entrega/recolha
-Neste caso não inclui a garantia habitual de 4 meses.

Acabamento estético premium (opcional)
Sujeito a avaliação/orçamentação após a reparação.

Se desejar avançar indique-me por favor para lhe explicar como funciona a recolha.""",
"""Hello,

Structural repair: €49
-Restores performance (lost due to the damage), in this case not 100%
-Includes cosmetic finish - local application of textured paint close to the original.
-Includes pick-up/delivery
-In this case it does not include our usual 4-month warranty.

Premium cosmetic finish (optional)
Subject to assessment/quote after the repair.

If you would like to proceed, please let me know and I will explain how the pick-up works.""",
"""Hola,

Reparación estructural: 49 €
-Recupera la performance (perdida con el daño), en este caso no al 100%
-Incluye acabado estético - aplicación local de pintura texturizada aproximada a la original.
-Incluye recogida/entrega
-En este caso no incluye la garantía habitual de 4 meses.

Acabado estético premium (opcional)
Sujeto a evaluación/presupuesto después de la reparación.

Si desea avanzar, indíqueme por favor para explicarle cómo funciona la recogida.""")

add("orcpintura", "ORÇAMENTO PINTURA S/REPARAÇÃO",
"""Viva,

Neste caso específico, não é necessário qualquer reparação da fibra. 😀

A pintura para replicar os padrões originais ficará por 29€.👍

O orçamento acima mencionado já inclui a entrega e a recolha nos nossos pontos de recolha.""",
"""Hello,

In this specific case, no fiber repair is required 😀

The painting to replicate the original patterns will cost €29 👍

The above-mentioned quote already includes pick-up and delivery at our collection points.""",
"""Hemos analizado el estado de la pala y parece que el daño es únicamente a nivel de pintura, sin afectar su estructura ni rendimiento.
Queremos ser sinceros: en estos casos, la reparación puede no compensar económicamente, ya que los costes logísticos (transporte de ida y vuelta) están siempre incluidos en el precio final.
Aun así, si deseas dejarla como nueva, el servicio completo de restauración estética tiene un coste total de 29 € (todo incluido).
Quedamos a tu disposición para cualquier duda.""")

add("orcrugoso", "ORÇAMENTO RUGOSO",
"""Viva,

A aplicação da rugosidade ficará por 29€. 😀

No custo do serviço já está incluída entrega e recolha nos nossos pontos de recolha. 👍""",
"""Hello,

The application of the surface roughness will cost €29 😀

The service price already includes pick-up and delivery at our collection points, as well as a 4-month warranty 👍""",
"""Hola,

La aplicación de la rugosidad tendrá un coste de 29 € 😀

El precio del servicio ya incluye la recogida y entrega en nuestros puntos de recogida, así como una garantía de 4 meses 👍""")

add("orceuropa", "ORÇAMENTO REPARAÇÃO EUROPA",
None,
"""The repair cost is €59

This price includes:

-collection and delivery of the racket

-4-month repair warranty

-paintwork replicating the original design

Would you like to go ahead with the repair? Please let me know your feedback on the offer and if you’d like to proceed.""",
"""El coste de la reparación es de 59 €

Este precio incluye:

-recogida y entrega de la pala

-garantía de reparación de 4 meses

-pintura replicando el acabado original

¿Le gustaría seguir adelante con la reparación?""")

add("semorc", "S/ORÇAMENTO + AJUDA COMPRAR",
"""Viva,

Infelizmente (e contra nós falamos) neste tipo de caso poderá não valer a pena reparar.
Visto que é uma zona grande de contacto com a bola, o toque poderá ficar alterado com possibilidade de voltar a partir.

Como opção, se for o caso, pode também indicar-nos alguma raquete que deseje comprar - conseguimos, na maioria dos casos, vendê-la a um preço abaixo do mínimo do mercado.
Além disso, temos agora produção própria de raquetes, com possibilidade de criação de modelos 100% personalizados ou de venda em bruto a um preço muito competitivo""",
"""Hello,

Unfortunately (and speaking against our own interest), in this type of case it may not be worthwhile to proceed with a repair.

As this is a large ball-contact area, the feel of the racket may be altered, with a risk of it breaking again.

As an alternative, if applicable, you may let us know which racket you would like to purchase - in most cases, we are able to offer it at a price below the market minimum.

In addition, we now have our own racket production, with the possibility of creating 100% customized models or selling unbranded rackets at a very competitive price.""",
"""Hola,

Lamentablemente (y aunque vaya en contra de nuestros intereses), en este tipo de caso puede que no valga la pena realizar la reparación.
Dado que se trata de una zona de gran contacto con la bola, el tacto podría verse afectado y existe la posibilidad de que vuelva a romperse.

Como opción, si lo prefieres, también puedes indicarnos alguna pala que desees comprar; en la mayoría de los casos, podemos ofrecerla a un precio inferior al mínimo del mercado.

Además, ahora contamos con producción propia de palas, con la posibilidad de crear modelos 100 % personalizados o de venderlas en bruto a un precio muy competitivo.""")

add("avancar", "ENVIAR A SEGUIR AO ORÇAMENTO (SEMPRE)",
"""Se desejar avançar indique-me por favor para lhe explicar como funciona a recolha.""",
"""If you’d like to proceed, please let me know so I can explain how the collection works.""",
"""Si quieres seguir adelante, avísame por favor para que te explique cómo funciona la recogida.""")

add("acabamento", "EXEMPLOS ACABAMENTO",
"""Viva! Pode ver exemplos do acabamento aqui: https://acabamento-drpadel.vercel.app/ 🙂""",
"""Hello! You can see examples of the finish here: https://acabamento-drpadel.vercel.app/ 🙂""",
"""¡Hola! Puede ver ejemplos del acabado aquí: https://acabamento-drpadel.vercel.app/ 🙂""")

# ---------------- ENVIO / RECOLHA ----------------
add("envio", "ENVIO RAQUETE",
"""Para enviar a sua raquete de forma rápida, segura e conveniente, escolha uma das seguintes opções:

Opção 1: Clubes Parceiros

* Pode deixar a raquete num dos nossos clubes parceiros: https://bit.ly/clubes-parceiros


Opção 2: Pontos Pickup da DPD

1. Embale a sua raquete: Coloque a raquete numa caixa ou bolsa adequada para transporte.

2. Escolha o ponto Pickup: Encontre o ponto Pickup da DPD mais próximo de si através deste link: https://bit.ly/pontos-pickup-pt

3. Preencha este link https://bit.ly/entregar-ponto-dpd com os seus dados e apresente o QR CODE que é gerado no final em qualquer ponto DPD.

4. Depois de entregar confirme por favor que recebeu um SMS da DPD com a confirmação.

Assim que deixe a raquete, por favor, avise-nos.""",
"""To send your racket quickly, safely, and conveniently, please choose one of the following options:
(WhatsApp: save our contact so you can access the links we share.)

Option 1: Partner Clubs
You can drop off the racket without a cover at one of our partner clubs: https://bit.ly/clubes-parceiros

Option 2: DPD Pickup Points

Pack your racket: Place the racket in a box or suitable bag for transport.

Choose the Pickup point: Find the nearest DPD Pickup point through this link: https://bit.ly/pontos-pickup-pt

Show the QR code: At the Pickup point, present the QR code that we will send you next.


Once you have dropped off the racket, please let us know. 😀""",
"""A través del siguiente enlace puedes pedir la recogida de tu pala:
👉🏼 https://bit.ly/recogida-drpadel

WhatsApp: guarda nuestro contacto para acceder a los enlaces compartidos.

Verás que hay dos opciones:
🏠 Recogida en casa
📍 Recogida en punto pickup

⚠️ Actualmente, solo está disponible la opción de recogida en punto pickup.
Por favor, selecciona esa opción al completar el formulario.

🛎️ Muy importante: cuando dejes la pala en el punto pickup, avísanos enviándonos un mensaje, para que podamos hacer el seguimiento correctamente. ¡Gracias por tu colaboración!""")

add("recolhaeuropa", "RECOLHA EUROPA",
"""Através deste link - https://bit.ly/dpd-pickup-europe - pode criar o seu próprio pedido de recolha para a sua raquete.
No final do formulário, será gerado um código QR - basta apresentar este código QR ao entregar a sua encomenda num Ponto Pickup da DPD (balcão).
Por favor, note: não é possível efetuar entregas em cacifos (lockers) - apenas é suportada a entrega presencial num balcão da DPD.
Depois de entregar a raquete, informe-nos, por favor.""",
"""Through this link - https://bit.ly/dpd-pickup-europe - you can create your own pickup request for your racket.
At the end of the form, a QR code will be generated - simply present this QR code when dropping off your package at a DPD Pickup Point (counter).
Please note: locker drop-offs are not available - only in-person drop-off at a DPD counter is supported.
Once you’ve dropped off the racket, please let us know.""",
"""A través de este enlace - https://bit.ly/dpd-pickup-europe - puede crear su propia solicitud de recogida para su pala.
Al final del formulario, se generará un código QR: simplemente presente este código QR al entregar su paquete en un Punto Pickup de DPD (mostrador).
Tenga en cuenta: no están disponibles las entregas en taquillas - solo se admite la entrega en persona en un mostrador de DPD.
Una vez haya entregado la pala, por favor avísenos.""")

add("paiseseuropa", "PAÍSES EUROPA (RECOLHA)",
None,
"""Belgium, Denmark, Estonia, Finland, France, Germany, Latvia, Luxembourg, Netherlands, Poland, Portugal, Slovakia, Slovenia, Sweden, Spain""")

add("outrospaises", "NÃO CONSEGUIMOS DE MOMENTO (OUTROS PAÍSES)",
None,
"""Hi,

Thank you for reaching out to us.

At the moment, our repair logistics are limited to Portugal, Spain, and other European countries. Unfortunately, we are not yet able to process repairs from other countries.

However, please note that customizations and sales are available internationally - only repairs are currently restricted due to logistics.

We are actively working on expanding our services, and we will notify you as soon as we have logistics in place for your country.

If you have any suggestions or ideas that could help us improve or speed up this process, we would be happy to hear them.

Thank you for your understanding and support.

Best regards""")

add("ilhas", "ENVIO ILHAS (CTT)",
"""Viva! Pode enviar a raquete por CTT para:
Machado Sports
Rua Damião de Góis, nº 2, Cave
4480-762 Vila do Conde

Depois de reparada, enviamos de volta para si, com o reenvio incluído 🙂 Assim que enviar, avise-nos por favor.""",
"""Hello! You can send the racket by post (CTT) to:
Machado Sports
Rua Damião de Góis, nº 2, Cave
4480-762 Vila do Conde
Portugal

Once it's repaired, we'll send it back to you, return shipping included 🙂 Please let us know once you've sent it.""",
"""¡Hola! Puede enviar la pala por correo (CTT) a:
Machado Sports
Rua Damião de Góis, nº 2, Cave
4480-762 Vila do Conde
Portugal

Una vez reparada, se la enviamos de vuelta, con el reenvío incluido 🙂 Avísenos, por favor, cuando la envíe.""")

add("condicoes", "CONDIÇÕES DE RECOLHA",
"""De forma a conseguirmos oferecer as recolhas e entregas estabelecemos que devem ser recolhidas no mínimo 2 raquetes ou que tenham passado 4 dias desde a entrega inicial no clube.

Se preferir um serviço mais rápido, disponibilizamos uma opção express, que garante a recolha no dia útil seguinte por um custo adicional de 14€, tal como prioridade interna.

Estamos à disposição para qualquer dúvida.""",
"""Hello,

In order for us to be able to offer the established pick-up and delivery service, we require a minimum of 2 rackets to be collected, or that 4 days have passed since the initial delivery at the club.

If you prefer a faster service, we offer an Express option, which guarantees pick-up on the next business day for an additional cost of €14, as well as internal priority handling.

We remain at your disposal for any questions.""",
"""Con el fin de poder ofrecer recogidas y entregas de forma eficiente, hemos establecido que deben reunirse un mínimo de 2 raquetas o haber pasado 4 días desde la entrega inicial en el club.

Si prefiere un servicio más rápido, disponemos de una opción exprés, que garantiza la recogida al siguiente día hábil, además de prioridad interna, por un coste adicional de 14 €.

Estamos a su disposición para cualquier duda.""")

add("prazos", "PRAZOS - RECOLHA DE RAQUETES",
"""Sobre os prazos de recolha:
- Clubes Parceiros: recolhemos em até 4 dias úteis.
- Ponto DPD: depende do timing da transportadora.

Tem urgência? Serviço Express por 14€:
- Clube Parceiro - Recolha no dia útil seguinte + prioridade máxima.
- Ponto DPD - Prioridade máxima assim que a raquete chegar às nossas instalações.""",
"""Regarding deadlines:
- Partner Clubs: we collect within up to 4 working days.
- DPD Pickup Point: depends on the courier’s timing.

Is it urgent? Express Service for €14:
- Partner Club: collection on the next working day plus maximum priority.
- DPD Pickup Point: maximum priority as soon as the racket arrives at our facilities.""",
"""Sobre los plazos:
- Clubes colaboradores: recogemos en un máximo de 4 días laborables.
- Punto DPD: depende de los tiempos de la empresa de transporte.

¿Tiene urgencia? Servicio Express por 14€:
- Club colaborador: recogida el siguiente día laborable y máxima prioridad.
- Punto DPD: máxima prioridad en cuanto la pala llegue a nuestras instalaciones.""")

add("pedidorecolha", "PEDIDO DE RECOLHA",
"""Viva,

Gostaríamos de avisar que procedemos com o pedido de recolha para hoje para o seu clube/morada.
Caso até ao momento da chegada do estafeta tenha mais alguma raquete para reparar ou personalizar, poderá seguir nesta recolha 👍

Gratos pela compreensão,
Dr.Padel Racket""",
"""Hello,

We would like to inform you that we have scheduled the pick-up for today at your club/address.

If, before the courier arrives, you have any additional rackets that you would like to repair or customize, they may be included in this pick-up 👍

Thank you for your understanding,

Dr. Padel Racket""",
"""Hola,

Queremos informarle que hemos solicitado la recogida para hoy en su club/domicilio.
Si hasta el momento de la llegada del mensajero tiene alguna otra raqueta que desee reparar o personalizar, puede incluirla en esta misma recogida. 👍

Gracias por su comprensión,
Dr. Padel Racket""")

add("embrulhar", "COMO EMBRULHAR RAQUETE",
"""Para garantir um envio seguro, pode utilizar um dos envelopes almofadados ou envolver a raquete em algum material de proteção.
Normalmente, não existem problemas com os envios, uma vez que são manuseados com cuidado por parte do clube e transportadora.""",
"""To ensure safe packaging you can either use one of the padded envelopes they sell or wrap it in some protective material.
Usually, there are no issues with the shipments, as they are handled carefully by them.""",
"""Para garantizar un embalaje seguro, puede utilizar uno de los sobres acolchados que venden o envolver la pala en algún material de protección.
Normalmente, no hay problemas con los envíos, ya que son manipulados con cuidado por su parte.""")

add("express", "EXPRESS",
"""Serviço Express
Com o Serviço Express, garantimos a recolha da sua raquete no dia útil seguinte.
Assim que for recebida nas nossas instalações, será tratada com prioridade máxima em todas as etapas do processo, sem entrar na fila de espera habitual por ordem de chegada.

Este serviço tem um custo adicional de 14€.""",
"""With the Express Service, as soon as it is received at our facilities, it will be given top priority at every stage of the process, without entering the usual waiting queue based on order of arrival.

This service has an additional cost of €14.""",
"""Con el Servicio Express, en cuanto sea recibida en nuestras instalaciones, será tratada con la máxima prioridad en todas las etapas del proceso, sin entrar en la cola de espera habitual por orden de llegada.

Este servicio tiene un coste adicional de 14 €.""")

# ---------------- DURANTE A REPARAÇÃO ----------------
add("chegou", "RAQUETE CHEGOU UPSELL",
"""Viva 😄

A raquete já chegou às nossas instalações e encontra-se agora em processo de avaliação e reparação.

Durante este período, é possível usufruir de preços especiais em serviços complementares.

👉 Ver condições exclusivas:
https://bit.ly/descontos-extras

Uma ótima oportunidade para personalizar ou dar um upgrade à raquete com condições únicas.""",
"""Hi 😄,

Your racket has arrived at our facilities and is now undergoing evaluation and repair.

During this period, you can take advantage of special prices on complementary services.

👉 View exclusive conditions:
https://bit.ly/descontos-extras

A great opportunity to customize or upgrade your racket with unique conditions.""",
"""Hola 😄,

Su raqueta ya ha llegado a nuestras instalaciones y se encuentra actualmente en proceso de evaluación y reparación.

Durante este período, puede beneficiarse de precios especiales en servicios complementarios.

👉 Ver condiciones exclusivas:
https://bit.ly/descontos-extras

Una excelente oportunidad para personalizar o mejorar su raqueta con condiciones únicas.""")

add("estado", "ESTADO RAQUETE",
"""Viva,

Neste momento a sua raquete encontra-se em (ACABAMENTO/PINTURA/REPARAÇÃO).

Tencionamos entregar o mais breve possível 😀""",
"""Hello,

At the moment, your racket is in (FINISHING / PAINTING / REPAIR).

We intend to deliver it as soon as possible 😀""",
"""Hola,

En este momento, su pala se encuentra en (ACABADO / PINTURA / REPARACIÓN).

Nuestra intención es entregarla lo antes posible 😀""")

add("atraso", "ATRASO PINTURA",
"""Viva,

A pintura é um serviço demorado e individual onde temos que produzir as cores uma a uma para cada raquete. Agregado a este facto, neste momento também nos encontramos com um elevado volume de trabalho.

Se desejar pode ativar o serviço express que faz com que passe para a frente da respetiva fila.😁

Agradecemos a sua compreensão 🙏""",
"""Hello,

Painting is a time-consuming and individualized service, as we need to produce the colors one by one for each racket. In addition, we are currently experiencing a high workload.

If you wish, you may activate the Express Service, which allows your racket to move to the front of the corresponding queue 😁

Thank you for your understanding 🙏""",
"""Hola,

La pintura es un servicio laborioso e individualizado, ya que debemos producir los colores uno a uno para cada pala. Además, en este momento nos encontramos con un alto volumen de trabajo.

Si lo desea, puede activar el Servicio Express, lo que permitirá que su pala pase al frente de la cola correspondiente 😁

Agradecemos su comprensión 🙏""")

add("quantotempo", "QUANTO TEMPO DEMORA?",
"""Pode consultar aqui o tempo de serviço atual 🙂
https://www.drpadelracket.com/pages/faq""",
"""You can check our current service time here 🙂
https://www.drpadelracket.com/en/pages/faq""",
"""Puede consultar aquí el tiempo de servicio actual 🙂
https://www.drpadelracket.com/es/pages/faq""")

add("faq", "FAQS",
"""Confira a nossa secção de Perguntas Frequentes (FAQ) e encontre rapidamente as informações que precisa.

https://www.drpadelracket.com/pages/faq""",
"""Check out our Frequently Asked Questions (FAQ) section and quickly find the information you need.

https://www.drpadelracket.com/en/pages/faq""",
"""Consulte nuestra sección de Preguntas Frecuentes (FAQ) y encuentre rápidamente la información que necesita:

https://www.drpadelracket.com/es/pages/faq""")

# ---------------- GARANTIA / QUALIDADE ----------------
add("garantia", "TEM GARANTIA?",
"""Sim, as nossas reparações têm 4 meses de garantia, exceto quando a quebra é extensa e numa zona de contacto com a bola 🙂""",
"""Yes, our repairs come with a 4-month warranty, except when the break is extensive and in an area that makes contact with the ball 🙂""",
"""Sí, nuestras reparaciones tienen 4 meses de garantía, excepto cuando la rotura es extensa y en una zona de contacto con la bola 🙂""")

add("garantianao", "GARANTIA NÃO APLICADA",
"""Viva,

A garantia é aplicada nos casos em que a reparação volta a partir com bola e não tem sinais de ter batido em superfícies duras (Exemplo: Vidro do Campo ou Malha Lateral).

Desta forma, não se aplica neste caso porém é possível fazer uma atenção no preço de reparação 👍""",
"""Hello,

The warranty applies in cases where the repaired area breaks again due to ball impact and shows no signs of having hit hard surfaces (for example, court glass or side fencing).

For this reason, the warranty does not apply in this case; however, it is possible to offer a price adjustment on the repair 👍""",
"""Hola,

La garantía se aplica en los casos en que la reparación se vuelve a romper por impacto con la bola y no presenta signos de haber golpeado superficies duras (por ejemplo: el cristal de la pista o la malla lateral).

Por lo tanto, no se aplica en este caso, aunque podemos ofrecerle una atención especial en el precio de la reparación. 👍""")

add("performance", "PERFORMANCE RAQUETE",
"""Viva,

Trabalhamos em cooperação com professores de padel e com jogadores de nível M2 e M1, desta forma as raquetes são testadas por estas pessoas com o intuito de perceber a qualidade das reparações. 😀

Os únicos casos que temos feedback que existe perda percentual da performance da raquete é quando a fissura da fibra é extensa e abrange o sweet spot (zona centra da face) da mesma.
Caso contrário, a tensão da raquete é recuperada na sua totalidade 👍""",
"""Hello,

We work in cooperation with padel coaches and with M2 and M1 level players. In this way, the rackets are tested by these players in order to assess the quality of the repairs 😀

The only cases in which we receive feedback indicating a percentage loss of racket performance are when the fiber crack is extensive and affects the sweet spot (the central area of the face).

Otherwise, the racket’s tension is fully restored 👍""",
"""Hola,

Trabajamos en colaboración con profesores de pádel y jugadores de nivel M2 y M1. De este modo, las raquetas son probadas por ellos con el objetivo de evaluar la calidad de las reparaciones. 😀

Los únicos casos en los que hemos recibido comentarios sobre una pérdida de rendimiento son aquellos en los que la fisura de la fibra es extensa y abarca el sweet spot (zona central de la cara) de la raqueta.
Fuera de esos casos, la tensión de la raqueta se recupera en su totalidad. 👍""")

add("oquefazemos", "O QUE FAZEMOS?",
"""Utilizamos fibra de carbono semelhante à da raquete e fazemos com que se "funda" com a original, restaurando o toque e a performance da raquete.""",
"""We use carbon fiber similar to the racket’s original material and make it “blend” with the existing structure, restoring the racket’s feel and performance.""",
"""Utilizamos fibra de carbono similar a la de la raqueta y hacemos que se “funda” con la original, restaurando así el tacto y el rendimiento de la raqueta.""")

add("partida", "CLIENTE DIZ QUE VAI JOGAR COM RAQUETE PARTIDA",
"""Não recomendamos jogar com raquetes danificadas, pois perdem o toque original e há grande probabilidade de aumentar a sua quebra.
Podemos, contudo, ajudar a encontrar uma solução de substituição - temos opções a preços acessíveis, incluindo modelos recondicionados e raquetes da nossa própria produção.""",
"""We do not recommend playing with damaged rackets, as they lose their original feel and there is a high likelihood of further damage or breakage.

However, we can help you find a replacement solution - we offer affordable options, including refurbished models and rackets from our own production.""",
"""No recomendamos jugar con palas dañadas, ya que pierden su tacto original y existe una alta probabilidad de que el daño o la rotura aumenten.

No obstante, podemos ayudarle a encontrar una solución de sustitución: disponemos de opciones a precios accesibles, incluidos modelos reacondicionados y palas de producción propia.""")

add("defeito", "PINTURA ORIGINAL A SALTAR POR DEFEITO DE FABRICO",
"""Pelo que vemos na foto, o problema parece estar relacionado com a pintura original de fábrica da raquete. Infelizmente, mesmo uma nova pintura na zona poderia apresentar o mesmo comportamento ao longo do tempo.

No entanto, podemos aproveitar esta situação para transformar completamente a raquete com uma personalização total - criando um design único ao seu gosto.""",
"""Based on what we can see in the photo, the issue appears to be related to the racket’s original factory paint. Unfortunately, even a new paint application in that area could show the same behavior over time.

However, we can take advantage of this situation to completely transform the racket with a full customization - creating a unique design tailored to your preferences.""",
"""Por lo que podemos ver en la foto, el problema parece estar relacionado con la pintura original de fábrica de la pala. Lamentablemente, incluso una nueva aplicación de pintura en esa zona podría presentar el mismo comportamiento con el paso del tiempo.

No obstante, podemos aprovechar esta situación para transformar completamente la pala con una personalización total, creando un diseño único a su gusto.""")

add("carbono", "PADRÕES CARBONO NÃO REPLICADOS",
"""Viva,

Efetivamente, foram replicados os padrões da sua raquete de acordo com o modelo original. Julgamos, no entanto, que a sua observação esteja relacionada com o padrão do carbono, correto?
Importa esclarecer que este é o único elemento que não é totalmente replicável, uma vez que o carbono é uma fibra natural cujo tom e aspeto visual variam consoante o ângulo de incidência da luz e a orientação das fibras. Por esse motivo, podem existir ligeiras diferenças visuais, ainda que o acabamento e a qualidade estrutural se mantenham inalterados.
Ainda assim, agradecemos o seu feedback, que é fundamental para continuarmos a melhorar os nossos processos e garantir os mais elevados padrões de qualidade.
Ficamos ao dispor para qualquer esclarecimento adicional.
Com os melhores cumprimentos,""",
"""Hello,

The patterns of your racket were indeed replicated according to the original model. We believe, however, that your comment relates to the carbon pattern, is that correct?
Please note that this is the only element that cannot be fully replicated, as carbon is a natural fibre whose tone and visual appearance vary depending on the angle of the light and the orientation of the fibres. For this reason, there may be slight visual differences, although the finish and structural quality remain unchanged.
Nevertheless, we thank you for your feedback, which is essential for us to keep improving our processes and ensure the highest quality standards.
We remain available for any further clarification.
Best regards,""",
"""Hola,

Efectivamente, se replicaron los diseños de su pala de acuerdo con el modelo original. Creemos, sin embargo, que su comentario está relacionado con el patrón del carbono, ¿es así?
Cabe aclarar que este es el único elemento que no es totalmente replicable, ya que el carbono es una fibra natural cuyo tono y aspecto visual varían según el ángulo de incidencia de la luz y la orientación de las fibras. Por ese motivo, pueden existir ligeras diferencias visuales, aunque el acabado y la calidad estructural se mantienen inalterados.
Aun así, le agradecemos su comentario, que es fundamental para seguir mejorando nuestros procesos y garantizar los más altos estándares de calidad.
Quedamos a su disposición para cualquier aclaración adicional.
Saludos cordiales,""")

# ---------------- FEEDBACK ----------------
add("feedback", "PEDIR FEEDBACK",
"""Olá!
Agradecemos a sua confiança e o facto de ter recorrido aos nossos serviços.

Gostaríamos muito de saber como correu a experiência: já recebeu a sua raquete? O resultado correspondeu às suas expectativas?

A sua opinião é essencial para continuarmos a melhorar.
Pode deixar o seu feedback aqui (demora menos de 1 minuto):
🔗 https://bit.ly/feedback-dr

Muito obrigado!""",
"""Hello!

Thank you for your trust and for choosing our services.

We would love to know how your experience went: have you already received your racket? Did the result meet your expectations?

Your feedback is essential for us to continue improving.

You can leave your feedback here (it takes less than 1 minute):

🔗 https://bit.ly/feedback-dr

Thank you very much!""",
"""Hola!

Le agradecemos su confianza y el haber recurrido a nuestros servicios.

Nos encantaría saber cómo fue su experiencia: ¿ya ha recibido su pala? El resultado cumplió con sus expectativas?

Su opinión es esencial para que podamos seguir mejorando.

Puede dejar su opinión aquí (tarda menos de 1 minuto):

🔗 https://bit.ly/feedback-dr

Muchas gracias!""")

add("review", "BOM FEEDBACK POR ESCRITO - REPARAÇÃO",
"""Muito obrigado pelo feedback e pela confiança 🙏🏼
Ficamos felizes por saber que ficou satisfeito.

Se desejar ajudar-nos a chegar a mais gente na mesma situação poderá fazê-lo aqui com uma crítica positiva no google: https://bit.ly/reviews-google-dr .

Obrigado mais uma vez e esperamos poder ajudar numa próxima 😁""",
"""Thank you very much for your feedback and for your trust 🙏🏼

We are happy to hear that you were satisfied.

If you would like to help us reach more people in a similar situation, you can do so by leaving a positive review on Google here:
https://bit.ly/reviews-google-dr

Thank you once again, and we hope to be able to help you again in the future 😁""",
"""Muchas gracias por su comentario y por la confianza 🙏🏼
Nos alegra saber que quedó satisfecho.

Si desea ayudarnos a llegar a más personas en la misma situación, puede hacerlo dejando una reseña positiva en Google:
https://g.co/kgs/YqnsXa5

¡Gracias una vez más y esperamos poder ayudarle en una próxima ocasión! 😁""")

add("reviewpers", "BOM FEEDBACK POR ESCRITO - PERSONALIZAÇÃO",
"""Muito obrigado pelas suas palavras! 🙏

Ficamos muito felizes por saber que gostou do resultado final e que a raquete superou as suas expectativas!

Foi um prazer trabalhar na sua raquete e dar vida à sua ideia.

Se possível, agradecíamos muito uma avaliação no Google com foto: https://bit.ly/reviews-google-dr

Um abraço de toda a equipa Dr.Padel!""",
"""Thank you very much for your kind words! 🙏

We are truly delighted to know that you liked the final result and that the racket exceeded your expectations!

It was a great pleasure working on your racket and bringing your vision to life.

If possible, we would be very grateful if you could leave us a Google review with a photo: https://bit.ly/reviews-google-dr

Best regards from the entire Dr.Padel team!""",
"""¡Muchas gracias por sus palabras! 🙏

¡Nos alegra mucho saber que le ha gustado el resultado final y que la pala ha superado sus expectativas!

Ha sido un placer trabajar en su pala y dar vida a su idea.

Si es posible, le agradeceríamos mucho una reseña en Google con foto: https://bit.ly/reviews-google-dr

¡Un saludo de todo el equipo Dr.Padel!""")

add("naoprecisa", "CLIENTE JÁ NÃO PRECISA",
"""Ok, bons jogos! Se um dia precisar de reparação ou personalização, estamos por cá.""",
"""Ok, enjoy your games! If you ever need a repair or a custom racket, we're here.""",
"""¡Ok, buenos partidos! Si algún día necesitas una reparación o una pala personalizada, aquí estamos.""")

# ---------------- PERSONALIZAÇÃO ----------------
add("pers", "PERSONALIZAÇÃO - PRIMEIRA RESPOSTA (PT/EUROPA)",
"""Olá! 👋

O valor depende da raquete base e do design. Para a base, temos os nossos modelos próprios e também raquetes de marca (Adidas, Bullpadel, Nox, etc.).

Pode criar o seu design aqui: https://studio.drpadelracket.com
E ver alguns exemplos do nosso trabalho aqui: https://galeria-drpadel.netlify.app

Tem alguma ideia de design (cores, nome, logótipo)? E prefere uma raquete com mais potência, mais controlo ou equilibrada?""",
"""Hi! 👋

The price depends on the base racket and the design. For the base, we have our own models and also brand rackets (Adidas, Bullpadel, Nox, etc.).

You can create your design here: https://studio.drpadelracket.com
And see some of our work here: https://galeria-drpadel.netlify.app

Do you have a design idea in mind (colours, name, logo)? And do you prefer a racket with more power, more control or balanced?""",
"""¡Hola! 👋

El precio depende de la pala base y del diseño. Para la base, tenemos nuestros modelos propios y también palas de marca (Adidas, Bullpadel, Nox, etc.).

Puedes crear tu diseño aquí: https://studio.drpadelracket.com
Y ver algunos ejemplos de nuestro trabajo aquí: https://galeria-drpadel.netlify.app

¿Tienes alguna idea de diseño (colores, nombre, logo)? ¿Y prefieres una pala con más potencia, más control o equilibrada?""")

add("dubai", "PERSONALIZAÇÃO - PRIMEIRA RESPOSTA (DUBAI)",
None,
"""Hello! See how it works: https://dr-padel-guide.vercel.app and here are some examples of rackets we've made: https://galeria-drpadel.netlify.app Is it for you or a gift?""")

add("galeria", "PERSONALIZAÇÃO - GALERIA DE EXEMPLOS",
"""Pode ver alguns exemplos que já fizemos aqui: https://galeria-drpadel.netlify.app""",
"""Here are some examples of rackets we've made: https://galeria-drpadel.netlify.app""",
"""Aquí puedes ver algunos ejemplos que ya hemos hecho: https://galeria-drpadel.netlify.app""")

add("30", "PERSONALIZAÇÃO - DEPÓSITO 30%",
"""Para avançarmos com o projeto, pedimos uma adjudicação de 30% (X€).
As maquetes finais são feitas em conjunto depois do pagamento, com revisões ilimitadas até aprovar para produção.
Os restantes 70% (X€) só são pagos quando a raquete estiver pronta e já tiver recebido fotos e vídeos, antes do envio.
Prazo habitual: 1-2 semanas de produção + 2-4 dias de transporte.
Posso enviar o link de pagamento?""",
"""To move forward with the project, we ask for a 30% deposit (X€).
The final mockups are created together after payment, with unlimited revisions until you approve them for production.
The remaining 70% (X€) is only paid once the racket is ready and you have received photos and videos, before shipping.
Usual timeline: 1-2 weeks of production + 2-4 days of shipping.
Shall I send you the payment link?""",
"""Para avanzar con el proyecto, pedimos una señal del 30% (X€).
Las maquetas finales se hacen en conjunto después del pago, con revisiones ilimitadas hasta que las apruebe para producción.
El 70% restante (X€) solo se paga cuando la pala esté lista y haya recibido fotos y vídeos, antes del envío.
Plazo habitual: 1-2 semanas de producción + 2-4 días de transporte.
¿Le envío el enlace de pago?""")

add("adjudicado", "PERSONALIZAÇÃO - PÓS-PAGAMENTO ADJUDICAÇÃO (FICHA + TIMELINE + EXTRAS)",
"""Obrigado, pagamento recebido!

Próximos passos:

1. Preencha a nossa ficha rápida (2 min), para a design team ter tudo certo desde o início: https://bit.ly/custom-racket-drpadel
2. A design team prepara as maquetes e envia-as para aprovação. Revisões ilimitadas até ficar 100% satisfeito.
3. Depois de aprovar, a raquete entra em produção. Enviamos fotos e vídeos antes do envio.

Timeline completa do seu projeto: https://portal.drpadelracket.com/timeline

Quer acrescentar algum extra? https://portal.drpadelracket.com/extras""",
"""Thank you, payment received!

Here's what happens next:

1. Fill in our quick form (2 min) so our design team has everything right from the start: https://bit.ly/custom-racket-drpadel
2. Our design team prepares your mockups and sends them for your approval. Unlimited revisions until you're 100% happy.
3. Once you approve, your racket goes into production. We'll send you photos and videos before shipping.

Full timeline of your project: https://portal.drpadelracket.com/timeline

Would you like to add any extras? https://portal.drpadelracket.com/extras""",
"""¡Gracias, pago recibido!

Próximos pasos:

1. Rellene nuestra ficha rápida (2 min), para que nuestro equipo de diseño tenga todo correcto desde el principio: https://bit.ly/custom-racket-drpadel
2. Nuestro equipo de diseño prepara las maquetas y se las envía para su aprobación. Revisiones ilimitadas hasta que esté 100% satisfecho.
3. Una vez aprobada, la pala entra en producción. Le enviamos fotos y vídeos antes del envío.

Timeline completo de su proyecto: https://portal.drpadelracket.com/timeline

¿Quiere añadir algún extra? https://portal.drpadelracket.com/extras""")

add("lficha", "LINK - FICHA DE PERSONALIZAÇÃO", "https://bit.ly/custom-racket-drpadel")

add("original", "RAQUETE ORIGINAL VS MOLDE SEMELHANTE",
"""Esta raquete é feita por nós com um molde semelhante ao original, não é a original da marca. As sensações podem ser parecidas, mas o peso e o toque não são exatamente iguais.""",
"""This racket is made by us with a mould similar to the original, it is not the brand's original racket. The feel can be similar, but the weight and touch are not exactly the same.""",
"""Esta pala la fabricamos nosotros con un molde similar al original, no es la original de la marca. Las sensaciones pueden ser parecidas, pero el peso y el tacto no son exactamente iguales.""")

add("vidro", "FIBRA DE VIDRO - SUGERIR NOVA PERSONALIZADA",
"""Neste caso, por ser uma raquete de fibra de vidro, não conseguimos personalizar a pintura. Pode compensar mais criar uma nova já personalizada à sua medida 🙂""",
"""As this is a fiberglass racket, we can't customise the paint on it. It may be worth more to create a new one, already customised to your taste 🙂""",
"""Al ser una pala de fibra de vidrio, no podemos personalizar la pintura. Puede compensar más crear una nueva ya personalizada a tu gusto 🙂""")

add("oem", "MARCA PRÓPRIA / OEM - PRIMEIRA RESPOSTA",
"""Olá! Obrigado pelo contacto. Para marca própria começamos sempre por desenvolver uma amostra. Já tem o design e a performance que procura definidos?""",
"""Hello! Thanks for reaching out. For private label we always start by developing a sample. Do you already have the design and the performance you're looking for defined?""",
"""¡Hola! Gracias por el contacto. Para marca propia siempre empezamos desarrollando una muestra. ¿Ya tienes definidos el diseño y el rendimiento que buscas?""")

# ---------------- LINKS SOLTOS ----------------
add("lportal", "LINK - PORTAL DE CLIENTES", "https://portal.drpadelracket.com")
add("lstudio", "LINK - RACKET STUDIO", "https://studio.drpadelracket.com")
add("lgaleria", "LINK - GALERIA", "https://galeria-drpadel.netlify.app")
add("lguide", "LINK - GUIA DE PERSONALIZAÇÃO", "https://dr-padel-guide.vercel.app")
add("lextras", "LINK - EXTRAS", "https://portal.drpadelracket.com/extras")
add("ltimeline", "LINK - TIMELINE DA PERSONALIZAÇÃO", "https://portal.drpadelracket.com/timeline")


# ---------------- GERAR ----------------
class Literal(str):
    pass


def literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(Literal, literal_representer)


def limpa(t):
    t = t.replace(" ", "").replace(" ", " ")
    t = re.sub(r"<(https?://[^>]+)>", r"\1", t)
    t = re.sub(r"[ \t]+\n", "\n", t)  # espacos no fim das linhas
    return t.strip()


def main():
    matches = []
    vistos = set()
    for trig, sit, pt, en, es in M:
        for suf, txt, lang in (("", pt, "PT"), ("en", en, "EN"), ("es", es, "ES")):
            if not txt:
                continue
            t = ";" + trig + suf
            assert t not in vistos, t
            vistos.add(t)
            matches.append({
                "trigger": t,
                "replace": Literal(limpa(txt)),
                "word": True,
                "label": f"{sit} ({lang})",
            })
    cab = (
        "# GERADO AUTOMATICAMENTE por gerar.py - nao editar a mao.\n"
        "# Fonte: tabela MENSAGENS (base ESCRI, Airtable).\n"
        "# Atalhos: ;nome (PT), ;nomeen (EN), ;nomees (ES). Disparam ao carregar em espaco.\n"
    )
    corpo = yaml.dump({"matches": matches}, allow_unicode=True, sort_keys=False, width=10000)
    with open("mensagens.yml", "w", encoding="utf-8") as f:
        f.write(cab + corpo)

    # lista para o README
    linhas = ["| Atalho | Mensagem | Línguas |", "|---|---|---|"]
    for trig, sit, pt, en, es in M:
        langs = ", ".join(l for l, x in (("PT", pt), ("EN", en), ("ES", es)) if x)
        linhas.append(f"| `;{trig}` | {sit} | {langs} |")
    with open("LISTA.md", "w", encoding="utf-8") as f:
        f.write("# Lista de atalhos\n\nPT: `;nome` - EN: `;nomeen` - ES: `;nomees`. Escreve o atalho e carrega em espaço.\n\n")
        f.write("\n".join(linhas) + "\n")
    print(len(matches), "atalhos gerados")


if __name__ == "__main__":
    main()
