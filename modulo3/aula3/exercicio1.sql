CREATE TABLE autores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);
INSERT INTO autores(nome,nacionalidade) VALUES('vitor', 'oi'), ('Maria', 'po');

CREATE TABLE livros (
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao TEXT NOT NULL,
    id_autor INTEGER,
    Foreign Key (id_autor) REFERENCES autores(id)
);

INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES('Foi de base',1999, 1), ('Mouse',2000, 2);

SELECT * FROM livros;

SELECT  livros.titulo,
               autores.nome

FROM autores
INNER JOIN livros on id_autor = autores.id;


SELECT  livros.titulo,
        autores.nome

FROM autores
INNER JOIN livros on id_autor = autores.id;

WHERE nacionalidade = 'Britanica';



