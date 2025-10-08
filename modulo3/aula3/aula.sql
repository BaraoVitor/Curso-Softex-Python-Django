CREATE Table professores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);
CREATE Table alunos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    Foreign Key (id_professor) REFERENCES professores(id)
);

INSERT INTO professores(nome) VALUES('Vitor');
SELECT * FROM professores;

INSERT INTO alunos(nome,id ) VALUES ('joao', 1);

INSERT INTO alunos(nome,id_professor) VALUES ('Mara', 1);

SELECT * FROM alunos;

SELECT alunos.nome as nome_aluno, professores.nome as nome_professores

FROM alunos
INNER JOIN professores ON alunos.id_professor



