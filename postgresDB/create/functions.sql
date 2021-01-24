create function pobierz_koszyk(user_id integer) returns TABLE(nazwa text, ilosc integer, cena_jednostkowa double precision, suma double precision)
language sql
as 
$$
	SELECT m.nazwa,k.ilosc ilosc,m.cena as cena_jednostkowa,k.cena as suma FROM project.koszyk k,project.monitor m WHERE k.id_monitor = m.id_monitor AND k.id_uzytkownik = user_id;
$$;

create function pobierz_typy_dostawy() returns SETOF text
language plpgsql
as
$$
	DECLARE
        row RECORD;
    BEGIN
        FOR row IN SELECT nazwa_dostawy,cena_dostawy,firma_oblugujaca FROM project.typ_dostawy ORDER BY cena_dostawy
        LOOP
            RETURN next row.nazwa_dostawy ||' ' || row.firma_oblugujaca || ' cena: ' || row.cena_dostawy; 
        END LOOP;
    END;
$$;


create function utworz_zamowienie(id_uzytkownika integer, id_dostawy integer, suma double precision, data date, status character varying) returns void
language plpgsql
as
$$
	DECLARE
        wiersz RECORD;
        ilosc_przedmiotow bigint;
        suma_z_dostawa double precision;
        id_zamowienie INTEGER;
    BEGIN
        SELECT into id_zamowienie nextval('project.seq_zamowienie');

        suma_z_dostawa := (SELECT cena_dostawy FROM project.typ_dostawy WHERE id_typu_dostawy = id_dostawy);
        suma_z_dostawa = suma_z_dostawa + suma;
        ilosc_przedmiotow = sum(ilosc) FROM project.koszyk WHERE id_uzytkownik = id_uzytkownika;
        INSERT INTO project.zamowienie VALUES(id_zamowienie,id_uzytkownika,id_dostawy,status,suma_z_dostawa,ilosc_przedmiotow,data);

        FOR wiersz IN SELECT id_monitor,ilosc FROM project.koszyk WHERE id_uzytkownik = id_uzytkownika
        LOOP
            INSERT INTO project.szczegoly_zamowienia VALUES(DEFAULT,wiersz.id_monitor,id_zamowienie,wiersz.ilosc);
        END LOOP;
    END;
$$;

CREATE OR REPLACE FUNCTION utworz_zwrot(id_uzytkownika INTEGER,id_dostawy INTEGER, powod text, id_przedmiotu INTEGER, id_szczegoly_zamowienia INTEGER, typ_zwrotu text)
RETURNS void AS
$$   
    DECLARE
        id_zwrot INTEGER;
    BEGIN
        SELECT into id_zwrot nextval('project.seq_zwrot');
        INSERT INTO project.zwrot VALUES(id_zwrot,id_uzytkownika,id_dostawy,powod,typ_zwrotu,'W trakcie realizacji',now());
        INSERT INTO project.szczegoly_zwrotu VALUES(DEFAULT,id_przedmiotu,id_zwrot,DEFAULT,id_szczegoly_zamowienia);
    END; 
$$ LANGUAGE plpgsql;



create or REPLACE function zwrot_trigger() returns TRIGGER
language plpgsql
as
$$
	DECLARE
        max_ilosc INTEGER;
    BEGIN
		SELECT into max_ilosc ilosc FROM project.szczegoly_zamowienia  WHERE id_szczegoly_zamowienia = new.id_szczegoly_zamowienia;  
		if ( new.ilosc <= max_ilosc ) THEN
			RETURN NEW;
		ELSE
			RAISE NOTICE 'przekroczona ilosc';
			RETURN NULL;
		END IF;
    END;
$$;

CREATE trigger szczeg_zwrotu_trigger BEFORE UPDATE ON project.szczegoly_zwrotu FOR EACH ROW EXECUTE PROCEDURE zwrot_trigger();




create or REPLACE function zamowienie_trigger() returns TRIGGER
language plpgsql
as
$$
	DECLARE
        max_ilosc INTEGER;
    BEGIN
		SELECT into max_ilosc ilosc FROM project.monitor  WHERE id_monitor = new.id_monitor;  
		if ( new.ilosc <= max_ilosc ) THEN
			UPDATE project.monitor SET ilosc = max_ilosc-new.ilosc WHERE id_monitor = new.id_monitor;
			RETURN NEW;
		ELSE
			RAISE NOTICE 'przekroczona ilosc';
			RETURN NULL;
		END IF;
    END;
$$;

CREATE trigger szczeg_zamowienia_trigger BEFORE INSERT ON project.szczegoly_zamowienia FOR EACH ROW EXECUTE PROCEDURE zamowienie_trigger();




create or REPLACE function zakonczony_zwrot() returns TRIGGER
language plpgsql
as
$$
	DECLARE
        id INTEGER;
        dodatkowa_ilosc INTEGER;
		max_ilosc INTEGER;
    BEGIN
		SELECT into id,dodatkowa_ilosc id_monitor,ilosc FROM project.szczegoly_zwrotu WHERE id_zwrot = new.id_zwrot; 
		SELECT into max_ilosc ilosc FROM project.monitor WHERE id_monitor = id; 
		if ( new.status_zwrotu = 'Zrealizowane' ) THEN
			UPDATE project.monitor SET ilosc = max_ilosc+dodatkowa_ilosc WHERE id_monitor = id;
		END IF;
		RETURN NEW;
    END;
$$;

CREATE trigger koniec_zwrotu_trigger BEFORE UPDATE ON project.zwrot FOR EACH ROW EXECUTE PROCEDURE zakonczony_zwrot();