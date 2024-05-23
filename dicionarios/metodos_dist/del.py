contatos = {
    "leandro@gmail.com": {"nome": "Leandro", "telefone": "2428-4728"},
    "silva@gmail.com": {"nome": "Silva", "telefone": "3028-3183"},
    "santos@gmail.com": {"nome": "Santos", "telefone": "4385-7201"},
}

del contatos["leandro@gmail.com"]["telefone"]
del contatos["santos@gmail.com"]

print(contatos)