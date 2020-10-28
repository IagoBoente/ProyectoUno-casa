import var

class Clientes():

    def validarDni(dni):
        '''
        Código que controla si el dni es correcto o no
        :return:
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla [int(dni) % 23 ] == dig_control

        except:
            print('Error modulo validar DNI')
            return None
    def validoDni(self):
        '''
        muestra mensaje de dni válido
        :return:
        '''
        try:
            dni = var.ui.editDni.text()
            if Clientes.validarDni(dni):
                print(dni)
                var.ui.lblValidar.setStylesheet('Qlabel {color: green;}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setTexte(dni.upper())
            else:
                var.ui.lblValidar


        except:
            print('Error modulo escribir valido DNI')
            return None