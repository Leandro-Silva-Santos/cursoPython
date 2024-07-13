CREATE TABLE usuarios (
    id INT,
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário',
    endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
);

CREATE TABLE viagens.destinos (
    id INT,
    nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
    descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE viagens.reservas (
    id INT COMMENT 'Identificador único da reserva',
    id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
    id_destino INT COMMENT 'Referência ao ID do destino da reserva',
    data DATE COMMENT 'Data da reserva',
    status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc.)'
);


INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) 
VALUES (1, "Leandro", "leandro@gmail.com", "2002-08-08", "Rua dos bobos, 0 - Bairro Bobo/SP");

INSERT INTO destinos (id, nome, descricao)
VALUES (1, 'Santana de Parnaíba', 'Linda cidade do interior');

INSERT INTO reservas (id, id_usuario, id_destino, status, data)
VALUES (1, 1, 1,'Pendente', '2024-11-11')

SELECT * FROM usuarios;

SELECT * FROM 'usuarios'
WHERE id = AND nome LIKE "%Leandro%";


UPDATE usuarios
SET id = 4
WHERE email = "teste@teste.com";

DELETE FROM destinos
WHERE nome = "Santana de Parnaíba";


/*Alterando e excluindo tabelas*/
CREATE TABLE usuarios_nova (
    id INT,
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário',
    endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
);

INSERT INTO usuarios_nova (id, nome, email, endereco, data_nascimento)
SELECT id, nome, email, endereco, data_nascimento
FROM usuarios;

DROP TABLES usuarios
ALTER TABLE usuarios_nova RENAME usuarios


ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150)




/* CHAVES PRIMÁRIAS E ESTRANGEIRAS */

ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT, ADD PRIMARY KEY (id)

ALTER TABLE destinos
MODIFY COLUMN id AUTO_INCREMENT,
ADD PRIMARY KEY (ID);

ALTER TABLE reservas
MODIFY COLUMN id AUTO_INCREMENT,
ADD PRIMARY KEY (id);

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY  (id_destino) REFERENCES destinos (id);

INSERT INTO reservas(id_usuario, id_destino, data) VALUES (1, 1, '2024-07-12');

ALTER TABLE reservas
ADD CONSTRAINT fk_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
ON DELETE CASCADE;


/* INNER JOIN */
SELECT * FROM usuarios usuarios
INNER JOIN reservas rs ON us.id = rs.id_usuario
INNER JOIN destinos ds ON rs.id_destino = ds.id;

/* LEFT JOIN */
SELECT * FROM usuarios us
LEFT JOIN reservas rs ON us.id = rs.id_usuario;

/* RIGHT JOIN */
SELECT * FROM reservas rs
RIGHT JOIN destinos ds ON rs.id_destino = ds.id;


/*subconsultas*/
SELECT * FROM usuarios
WHERE id NOT IN (SELECT id_usuario FROM reservas);

SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas FROM usuarios;




/* MONGODB */
/* JSON */
{
"_id":1,
"nome": "Leandro",
"idade": 21,
"data_nascimento": "2002-08-08",
"enderecos": [{
"logradouro": "Rua Turim",
"numero": 223,
"bairro": "Jardim",
"cidade": "Santana"
}],
"interesses":["futebol", "culinaria"],
"reservas": [ ObjectId("123"), Object("234")
]

}

{
"_id":1,
"nome": "Paris",
"descricao": "Capital da França",
"localizacao": {
"type": 'Point',
"cordinates": [-46.661056, -23.587384]
}
}

{
"_id": ObjectId("123"),
"destino": ObjectId("456"),
"data": "2024-08-08",
"status": "pendente",
"usuario": ObjectId(345)
}
