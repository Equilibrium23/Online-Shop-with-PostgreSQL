CREATE SEQUENCE seq_zwrot START 1 INCREMENT 1;

CREATE OR REPLACE FUNCTION utworz_zwrot(id_uzytkownika INTEGER,id_dostawy INTEGER, powod text, id_przedmiotu INTEGER, id_szczegoly_zamowienia INTEGER, typ_zwrotu text)
RETURNS void AS
$$   
    DECLARE
        id_zwrot INTEGER;
    BEGIN
        SELECT into id_zwrot nextval('project.seq_zwrot');

        INSERT INTO project.zwrot VALUES(id_zwrot,id_uzytkownika,id_dostawy,powod,typ_zwrotu,'W trakcie realizacji');
        INSERT INTO project.szczegoly_zwrotu VALUES(DEFAULT,id_przedmiotu,id_zwrot,id_szczegoly_zamowienia);
    END; 
$$ LANGUAGE plpgsql;