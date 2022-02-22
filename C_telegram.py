# -*- coding: utf-8 -*-
""""""

import requests


class C_telegram:

  def __init__(self, f_telegram:dict, nombrePrograma:str) -> None:
    """
    nombrePrograma: Nombre de la aplicacion

    f_telegram debe de contener
      * f_telegram['token'] : token del bot
      * f_telegram['canal'] : canal a donde se comunica el bot
    """
    
    self.nombrePrograma = nombrePrograma

    self.status = ['error', '']
    
    self.token = str(f_telegram['token'])
    self.canal = str(f_telegram['canal'])

    _codigo=self.dispararMensaje('Conexión establecida.')

    if(_codigo['status'][0] == 'error'):
      self.status = _codigo['status']
      return

    _codigo = _codigo['out'].status_code   

    if(_codigo != 200):
        self.status = [
            'error', 
            'peticion a telegram mando mensaje {}'.format(_codigo)
            ]
        return

    self.status = ['ok','']

  
  def dispararMensaje(self, _mensaje:str) -> dict:
    """mensaje: mensaje a enviar."""
      
    _url="https://api.telegram.org/";
    
    if(self.nombrePrograma != ''):
      link = '{}bot{}/sendMessage?chat_id={}&text=--- {} ---\n\n{}'
    else:
      link = '{}bot{}/sendMessage?chat_id={}&text={}\n\n{}'
        
    _url = link.format(
        _url, 
        self.token, 
        self.canal, 
        self.nombrePrograma, 
        _mensaje
      )

    try:
      r = requests.get(_url)
    except requests.exceptions.ConnectionError as error:
      return {'status': ['error', error], 'out': requests.models.Response}

    return {'status': ['ok', ''], 'out': r}