# Exemplo de user authentication e authorization flow com permissions array

# Authenticate user
def authenticate_user(username, password):
  # Verificação de credentials
  if verify_credentials(username, password):
    return {
      'username': username,
      'permissions': get_user_permissions(username)
    }
  else:
    return None


# Verificação de credentials puxando o database
def verify_credentials(username, password):
  # Vai ser realizada a lógica de autenticação (checar username/password pelo database)
  # Retorna True se credentials forem válidas, caso contrário, False
  pass


# Puxar permissões do usuário do database
def get_user_permissions(username):
  # Traz permissões do usuário do database baseado no username
  # Retorna com permissões por um array
  pass


# Recurso de controle de acesso
def check_permission(get_user_permissions, required_permission):
  return required_permission in get_user_permissions


# Exemplo de uso
user = authenticate_user('fulano', 'senha123')

if user:
  if check_permission(user['permissions'], 'admin'):
    print("User has admin privileges.")
  else:
    print("User has no admin privileges.")
else:
  print("Authenticantion failed.")