answer1=input("Buenos días. En qué podemos ayudarte?") #inicio preguntas generales #el programa tiene un fallo fatal, no discrimina correctamen el si y el no. a veces se intercala pero falla
print("De acuerdo, registramos su solicitud.")
answer2 =input("Podría ahora indicarnos si se trata de: ayuda, traslado o pago?") #favor no ser marica y escribir " ayuda", ni espacio ni mayus inicial

if answer2 == ("ayuda"): #empieza despliege de 4 posibles condiciones de respuesta
    print("De acuerdo, un momento por favor")
    answer21= input("Podría brevemente indicarnos sobre qué exactamente necesita ayuda?")
    print("Ok, entonces nos pondremos en contacto con usted en breve. Manténgase en línea.")

elif answer2 == ("traslado"):
    print("De acuerdo, un momento por favor")
    answer22= input("Podría brevemente indicarnos hacia dónde necesita trasladarse?")
    print("Entendido.")
    answer23= input("Antes de proseguir, le interesaría contratar nuestra cobertura especial de viajes? Cuesta menos de 99 céntimos sólo si la solicita ahora mismo. Indique Sí o No") #como enlazo la respuesta 23 y 22 al mismo sujeto?
    if answer23== ("sí" or "Sí" or "si" or "Si"):
        print("De acuerdo, hemos tomado nota")
    else:
        print("Es una pena, pero podrá solicitarlo en el futuro aunque a un precio superior")
    answer24 = input("Le confirmamos ha solicitado trasladarse a:"+answer22+" ,es esto correcto? Indique Sí o No")
    if answer22== ("Sí" or "Si" or "si" or "sí"):
        print("Excelente, contactaremos con usted de inmediato para continuar con el proceso. En menos de 5 minutos recibirá nuestra llamada.")
    else:
        answer22= input("En ese caso, por favor indíquenos nuevamente la ubicación de su traslado.")
        print("De acuerdo, hemos tomado nota y contactaremos con usted en un plazo de menos de 5 minutos.")

elif answer2 == ("pago"):
    print("Un momento por favor.")
    answerp= input("¿Desea realizar el pago de su tarifa plana? Indique Sí o No")
    if answerp == "Sí" or answerp =="Si" or answerp =="si" or answerp =="sí": #hay que hacer todas las comprobaciones 1 a 1 y ya funciona
        answerp1= input ("Por favor, indíquenos el código de su Identificación para proseguir")
        print(".")
        print(".")
        print(".")
        answerp2= input ("Indíquenos si quiere que realicemos el cobro automáticamente. Indique Sí o No")
        if answerp2 == "Sí" or answerp2 == "Si" or answerp2 =="si" or answerp2 =="sí":
            print("Pago realizado, gracias por su aportación. Será redirigido a la página principal.") #insertamos un codigo magico que le cobre automaticamente y activamos otro codigo que lo envia a la web.
        else:
            print("No se preocupe, contactaremos con usted en los próximos 5 minutos para ayudarle con su pago. Manténgase a la espera.")
    else:
        answerp3 = input("De acuerdo. Indíquenos si quiere que contactemos con usted para realizar el pago de otro producto. Indique Sí o No")
        if answerp3 == ("Sí" or "Si" or "si" or "sí"): #no funciona esta puta mierda
            print ("Contactaremos con usted inmediatemente, esté pendiente del teléfono por favor.") 
        else   :
            print ("Si desea entonces realizar cualquier otra solicitud le instamos a acceder a la web www.patito.com o acceder a cualquiera de los servicios de la web. Gracias por usar este servicio y esperamos escuchar de usted.")
else  : 
    print("De acuerdo contactaremos con usted en respuesta a su solicitud de: "+ answer2 + "  manténgase a la espera, lo contactaremos en menos de 10 minutos.") 
