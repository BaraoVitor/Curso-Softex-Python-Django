CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE Table cursos(
    id INTEGER PRIMARY key,
    titulo TEXT NOT NULL
);

CREATE Table aluno_cursos(
    id_alunos INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    Foreign Key (id_alunos) REFERENCES aluno(id),
    Foreign Key (id_curso) REFERENCES cursos(id)
)
INSERT INTO alunos(nome) VALUES('Pedro'), ('Michele'), ('Rafael'), ('Carol');

INSERT INTO cursos(titulo) VALUES('backend'),('frontend');
INSERT INTO aluno_cursos(id_usuarios, id_curso) VALUES(1,1),(1,2),(2,1)(3,1);
SELECT * FROM usuarios;
SELECT * FROM cursos;
SELECT * FROM usuarios_cursos;

SELECT U.nome FROM usuarios as U
INNER JOIN usuarios_cursos as UC on UC.id_usuarios = U.id
INNER JOIN cursos as C on UC.id_cursos = C.id;


select count(*) from alunos;


SELECT count(usuario.nome), cursos.titulo FROM usuarios as U
INNER JOIN usuarios_cursos on usuarios_cursos on UC.id_usuarios = U.id
INNER JOIN cursos as C on UC.id_cursos = C.id;
GROUP BY c.titulo;
HAVING count(a.nome) > 2 ;


