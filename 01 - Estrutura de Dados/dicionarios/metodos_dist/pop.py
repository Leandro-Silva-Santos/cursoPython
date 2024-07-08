contatos = {
    "leandro@gmail.com": {"nome": "Leandro", "telefone": "2428-4728"},
}

print(contatos.pop("leandro@gmail.com"))

print(contatos.pop("leandro@gmail.com", {}))