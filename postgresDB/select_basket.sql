-- SELECT id_monitor,COUNT(*) as ilosc,cena as cena_jednostkowa,sum(cena) as suma FROM project.koszyk WHERE id_uzytkownik = 1 GROUP BY id_monitor,cena;

-- SELECT m.nazwa,COUNT(*) as ilosc,k.cena as cena_jednostkowa,sum(m.cena) as suma FROM project.koszyk k,project.monitor m WHERE k.id_monitor = m.id_monitor AND k.id_uzytkownik = 1 GROUP BY k.id_monitor,k.cena, m.nazwa;

CREATE OR REPLACE FUNCTION pobierz_koszyk(user_id INTEGER)
RETURNS TABLE(nazwa text , ilosc integer, cena_jednostkowa DOUBLE PRECISION, suma DOUBLE PRECISION)
LANGUAGE SQL AS
'
    SELECT m.nazwa,k.ilosc ilosc,m.cena as cena_jednostkowa,k.cena as suma FROM project.koszyk k,project.monitor m WHERE k.id_monitor = m.id_monitor AND k.id_uzytkownik = user_id;
';

pobierz_koszyk(1);