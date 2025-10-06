CREATE Table usuarios(
    id INTEGER PRIMARY key,
    Primeiro_nome NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE Table postagem(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor TEXT NOT NULL
);

INSERT INTO usuarios (Primeiro_nome,sobrenome,email,senha)VALUES ('Vitor', 'Daniel', 'vitor@gmail.com', '2789438921');

INSERT INTO usuarios (Primeiro_nome,sobrenome,email,senha)VALUES ('Daniel', 'luz', 'vitor@gmail.com', '2789438922');

INSERT INTO usuarios (Primeiro_nome,sobrenome,email,senha)VALUES ('computador', 'zxzl', 'vitor@gmail.com', '2789438923');

INSERT INTO usuarios (Primeiro_nome,sobrenome,email,senha)VALUES ('escalo', 'psps', 'vitor@gmail.com', '2789438924');

INSERT INTO usuarios (Primeiro_nome,sobrenome,email,senha)VALUES ('projetor', 'dkdlad', 'vitor@gmail.com', '2789438925');




INSERT INTO postagem (titulo,postagem,id_autor)VALUES ('O divergente', 'editora: Rota', '2121212121');
INSERT INTO postagem (titulo,postagem,id_autor)VALUES ('O cavalo', 'editora: Rota', '2121212122');
INSERT INTO postagem (titulo,postagem,id_autor)VALUES ('O windows', 'editora: Rota', '2121212123');
INSERT INTO postagem (titulo,postagem,id_autor)VALUES ('O teclado', 'editora: Rota', '2121212124');
INSERT INTO postagem (titulo,postagem,id_autor)VALUES ('O mouse', 'editora: Rota', '2121212125');






SELECT * FROM usuarios WHERE id = 1;

SELECT * FROM postagem WHERE id_autor = '2121212125';