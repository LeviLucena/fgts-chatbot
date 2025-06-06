from validate_docbr import CPF

def validar_cpf(cpf):
    doc = CPF()
    return doc.validate(cpf)
