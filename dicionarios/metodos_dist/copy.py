contatos = {
    "leandro@gmail.com": {"nome": "Leandro", "telefone": "2428-4728"},
}

copia = contatos.copy()
copia["leandro@gmail.com"] = {"nome": "Lê"}

print(contatos["leandro@gmail.com"])
print(copia["leandro@gmail.com"])