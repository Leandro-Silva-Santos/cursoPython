contatos = {
    "leandro@gmail.com": {"nome": "Leandro", "telefone": "2428-4728"},
}

print(contatos["chave"])

contatos.get("chave")
contatos.get("chave", {})
contatos.get("leandro@gmail.com", {})