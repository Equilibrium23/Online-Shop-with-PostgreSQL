CREATE SEQUENCE seq_zamowienie START 1 INCREMENT 1;

CREATE OR REPLACE FUNCTION utworz_zamowienie(id_uzytkownika INTEGER,id_dostawy INTEGER, suma DOUBLE PRECISION, data DATE, status varchar)
RETURNS void AS
$$   
    DECLARE
        wiersz RECORD;
        ilosc_przedmiotow bigint;
        suma_z_dostawa double precision;
        id_zamowienie INTEGER;
    BEGIN
        SELECT into id_zamowienie nextval('seq_zamowienie');

        suma_z_dostawa := (SELECT cena_dostawy FROM project.typ_dostawy WHERE id_typu_dostawy = id_dostawy);
        suma_z_dostawa = suma_z_dostawa + suma;
        ilosc_przedmiotow = COUNT(*) FROM project.koszyk WHERE id_uzytkownik = id_uzytkownika;
        INSERT INTO project.zamowienie VALUES(id_zamowienie,id_uzytkownika,id_dostawy,status,suma_z_dostawa,ilosc_przedmiotow,data);

        FOR wiersz IN SELECT id_monitor,ilosc FROM project.koszyk WHERE id_uzytkownik = id_uzytkownika
        LOOP
            INSERT INTO project.szczegoly_zamowienia VALUES(DEFAULT,wiersz.id_monitor,id_zamowienie,wiersz.ilosc);
        END LOOP;
    END; 
$$ LANGUAGE plpgsql;



CREATE SEQUENCE seq_zamowienie START 1 INCREMENT 1;

CREATE OR REPLACE FUNCTION f()
RETURNS void
LANGUAGE plpgsql AS
'   
    DECLARE
        id_zamowienie INTEGER;
    BEGIN
        SELECT into id_zamowienie nextval('seq_zamowienie');
    END; 
';
