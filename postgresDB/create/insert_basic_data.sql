-- pracownik
INSERT INTO project.pracownik VALUES(DEFAULT,'Tomasz','Kowalski','tomasz.kowalski@gmail.com','tomasz.kowalski','pracownik1','11-10-2020','specjalista ds. zamowien');
INSERT INTO project.pracownik VALUES(DEFAULT,'Marek','Iwan','marek.iwan@gmail.com','marek.iwan','pracownik2','10-08-2020','specjalista ds. zamowien i zwrotow');
INSERT INTO project.pracownik VALUES(DEFAULT,'Filip','Kowalski','filip.kowalski@gmail.com','filip.kowalski','pracownik3','02-03-2020','administrator kont');
-- producent
INSERT INTO project.producent VALUES(1,'MSI','Zhonghe, Tajpej, Tajwan','1234','serwis@msi.com','(+800) 080 990');
INSERT INTO project.producent VALUES(2,'BenQ','Tajpej, Tajwan','1234','-----','0-62-766-77-71');
INSERT INTO project.producent VALUES(3,'Acer','Nowe Tajpej, Tajwan','1234','contact.pl@acer.com','022 209 89 78');
INSERT INTO project.producent VALUES(4,'Samsung','Seul, Korea Południowa','1234','-----','+48 22 607-93-33');
INSERT INTO project.producent VALUES(5,'iiyama','Chūō, Tokio, Japonia','1234','-----','+48 717 151 857');
INSERT INTO project.producent VALUES(6,'AOC','Tajpej, Tajwan','1234','-----','22 113 40 88');
INSERT INTO project.producent VALUES(7,'LG','Seul, Korea Południowa','1234','-----','801-54-54-54');
-- monitor
---------------------- MSI
INSERT INTO project.Monitor VALUES(nextval('project.msi_id_generator'),1,'MSI Optix G241VC',699,23.6,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('project.msi_id_generator'),1,'MSI Optix G24C4',899,23.6,'1920x1080',144,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('project.msi_id_generator'),1,'MSI Optix G27C4',1100,27,'1920x1080',165,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('project.msi_id_generator'),1,'MSI Optix G271',1200,27,'1920x1080',144,'IPS',250);
---------------------- BenQ
INSERT INTO project.Monitor VALUES(nextval('project.benq_id_generator'),2,'BenQ EL2870U',1200,28,'3840x2160',60,'TN',300);
INSERT INTO project.Monitor VALUES(nextval('project.benq_id_generator'),2,'BenQ ZOWIE XL2411P',870,27,'1920x1080',144,'TN',350);
INSERT INTO project.Monitor VALUES(nextval('project.benq_id_generator'),2,'BenQ PD3200U',3200,32,'3840x2160',60,'IPS',300);
INSERT INTO project.Monitor VALUES(nextval('project.benq_id_generator'),2,'BenQ MOBIUZ EX2710',1400,27,'1920x1080',144,'IPS',400);
---------------------- Acer
INSERT INTO project.Monitor VALUES(nextval('project.acer_id_generator'),3,'Acer Nitro VG240YBMIIX',600,23.8,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('project.acer_id_generator'),3,'Acer Predator XB273GPBMIIPRZX',1500,27,'1920x1080',144,'IPS',400);
INSERT INTO project.Monitor VALUES(nextval('project.acer_id_generator'),3,'Acer EK220QABI',400,23.8,'1920x1080',75,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('project.acer_id_generator'),3,'Acer Nitro VG240YUBMIIPX',23.8,23.8,'1920x1080',75,'IPS',300);
---------------------- Samsung
INSERT INTO project.Monitor VALUES(nextval('project.samsung_id_generator'),4,'Samsung C24RG50FQUX',900,23.5,'1920x1080',144,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('project.samsung_id_generator'),4,'Samsung C27F591FDUX',1200,27,'1920x1080',60,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('project.samsung_id_generator'),4,'Samsung C49HG90DMUX',3800,49,'1920x1080',144,'VA',350);
INSERT INTO project.Monitor VALUES(nextval('project.samsung_id_generator'),4,'Samsung Odyssey C27G75TQSUX',2800,27,'2560x1440',240,'VA',350);
---------------------- iiyama
INSERT INTO project.Monitor VALUES(nextval('project.iiyama_id_generator'),5,'iiyama G-Master GB2530HSU',700,24.5,'1920x1080',75,'TN',250);
INSERT INTO project.Monitor VALUES(nextval('project.iiyama_id_generator'),5,'iiyama G-Master GB2730QSU',1150,27,'2560x1440',75,'TN',350);
INSERT INTO project.Monitor VALUES(nextval('project.iiyama_id_generator'),5,'iiyama XUB2792QSU',1300,27,'2560x1440',75,'IPS',350);
INSERT INTO project.Monitor VALUES(nextval('project.iiyama_id_generator'),5,'iiyama XUB2792UHSU-B1 4K',1600,27,'3840x2160',60,'IPS',300);
---------------------- AOC
INSERT INTO project.Monitor VALUES(nextval('project.aoc_id_generator'),6,'AOC 27G2U',1000,27,'1920x1080',144,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('project.aoc_id_generator'),6,'AOC 22V2Q',500,21.5,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('project.aoc_id_generator'),6,'AOC Q3279VWF',1100,31.5,'2560x1440',75,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('project.aoc_id_generator'),6,'AOC CQ32G1',1500,31.5,'2560x1440',144,'VA',300);
---------------------- LG
INSERT INTO project.Monitor VALUES(nextval('project.lg_id_generator'),7,'LG 27GL63T-B HDR10',1050,27,'1920x1080',144,'IPS',320);
INSERT INTO project.Monitor VALUES(nextval('project.lg_id_generator'),7,'LG 27GL850-B NanoIPS',2000,27,'2560x1440',144,'IPS',350);
INSERT INTO project.Monitor VALUES(nextval('project.lg_id_generator'),7,'LG 24MP59G',499,23.8,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('project.lg_id_generator'),7,'LG 27GL83A-B',1800,27,'2560x1440',144,'IPS',350);
-- typ dostawy
INSERT INTO project.typ_dostawy VALUES(DEFAULT,'paczkomat',10,'Inpost');
INSERT INTO project.typ_dostawy VALUES(DEFAULT,'kurier',12,'DPS');
INSERT INTO project.typ_dostawy VALUES(DEFAULT,'poczta',20,'Poczta Polska');
