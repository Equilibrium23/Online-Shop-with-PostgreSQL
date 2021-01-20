CREATE OR REPLACE FUNCTION pobierz_typy_dostawy()
RETURNS setof text
LANGUAGE plpgsql AS
'   
    DECLARE
        row RECORD;
    BEGIN
        FOR row IN SELECT nazwa_dostawy,cena_dostawy,firma_oblugujaca FROM project.typ_dostawy ORDER BY cena_dostawy
        LOOP
            RETURN next row.nazwa_dostawy ||'' '' || row.firma_oblugujaca || '' cena: '' || row.cena_dostawy; 
        END LOOP;
    END; 
';
