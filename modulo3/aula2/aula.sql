CREATE TABLE alunos (
    id integer PRIMARY KEY,
    nome TEXT not NULL,
    idade INTEGER
);
INSERT INTO alunos (nome, idade) VALUES ('joao', 20);
INSERT INTO alunos(nome, idade) VALUES ('Maria', 50);
select nome,idade from  alunos;

select nome,idade from  alunos WHERE id = 20;

UPDATE alunos SET idade = 21 WHERE nome ='joao';

DELETE FROM alunos WHERE nome='Maria';





