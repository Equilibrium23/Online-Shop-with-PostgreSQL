INSERT INTO project.typ_dostawy VALUES(DEFAULT,'paczkomat',10,'Inpost');
INSERT INTO project.typ_dostawy VALUES(DEFAULT,'kurier',12,'DPS');
INSERT INTO project.typ_dostawy VALUES(DEFAULT,'poczta',20,'Poczta Polska');



DELETE TOP(1) from project.typ_dostawy WHERE cena_dostawy = 10;

DELETE FROM project.koszyk
                    WHERE id IN (
                    SELECT id FROM
                    project.koszyk WHERE id_uzytkownik={} AND
                    id_monitor = (SELECT monitor_id from project.monitor WHERE nazwa = \'{}\' )
                    LIMIT 1
                    )