TSS_PORCENTAJE = 7.09  
ISR_PORCENTAJE = 0.15  

sueldoBruto = float(input("Ingrese el sueldo bruto: "))
otrosDescuentos = float(input("Ingrese otros descuentos: "))

bonificacionAplica = input("¿Aplica bonificación? (s/n): ").lower()

if bonificacionAplica == 's':
    bono = float(input("Ingrese el monto del bono (entre $1,000 y $200,000): "))
    
    while bono < 1000 or bono > 200000:
        print("El bono debe estar entre $1,000 y $200,000.")
        bono = float(input("Ingrese el monto del bono: "))
    bonificacion = bono
    if sueldoBruto < 0 or otrosDescuentos < 0: print("El sueldo bruto y los descuentos deben ser valores positivos.")
else:
    bonificacion = 0

    if bonificacionAplica == 's':
        bonificacionPorcentaje = float(input("Ingrese el porcentaje común de bonificación: ")) / 100
        bonificacion = sueldoBruto * bonificacionPorcentaje

    descuento_tss = sueldoBruto * TSS_PORCENTAJE
    retencion_isr = sueldoBruto * ISR_PORCENTAJE

    sueldoNeto = sueldoBruto + (descuento_tss + retencion_isr + otrosDescuentos) + bonificacion

    print(f"Sueldo Bruto: {sueldoBruto}")
    print(f"Descuento por Seguridad Social (TSS): {descuento_tss}")
    print(f"Porcentaje de Retención del Impuesto sobre la Renta (ISR): {retencion_isr}")
    print(f"Descuentos: {otrosDescuentos}")
    print(f"Bonificación: {bonificacion}")
    print(f"Sueldo Neto: {sueldoNeto}")