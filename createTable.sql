CREATE TABLE cliente (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(100 CHAR) NOT NULL,
    idade NUMBER,
    saldo NUMBER(10, 2),
    data_cadastro DATE DEFAULT sysdate
);