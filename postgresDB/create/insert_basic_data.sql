-- pracownik
INSERT INTO project.pracownik VALUES(DEFAULT,'Tomasz','Kowalski','tomasz.kowalski@gmail.com','tomasz.kowalski','admin','11-10-2020','specjalista ds. zamowien');
INSERT INTO project.pracownik VALUES(DEFAULT,'Marek','Iwan','marek.iwan@gmail.com','marek.iwan','admin','10-08-2020','specjalista ds. zamowien i zwrotow');
INSERT INTO project.pracownik VALUES(DEFAULT,'Filip','Kowalski','filip.kowalski@gmail.com','filip.kowalski','admin','02-03-2020','administrator kont');
-- producent
INSERT INTO project.producent VALUES(1,'MSI','Zhonghe, Tajpej, Tajwan','1234','serwis@msi.com','(+800) 080 990');
INSERT INTO project.producent VALUES(2,'BenQ','Tajpej, Tajwan','12345','0-62-766-77-71');
INSERT INTO project.producent VALUES(3,'Acer','Nowe Tajpej, Tajwan','12346','contact.pl@acer.com','022 209 89 78');
INSERT INTO project.producent VALUES(4,'Samsung','Seul, Korea Południowa','12347','+48 22 607-93-33');
INSERT INTO project.producent VALUES(5,'iiyama','Chūō, Tokio, Japonia','12348','+48 717 151 857');
INSERT INTO project.producent VALUES(6,'AOC','Tajpej, Tajwan','12349','22 113 40 88');
INSERT INTO project.producent VALUES(7,'LG','Seul, Korea Południowa','1235','801-54-54-54');
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
INSERT INTO project.Monitor VALUES(nextval('project.acer_id_generator'),3,'Acer Nitro VG240YUBMIIPX',600,23.8,'1920x1080',75,'IPS',300);
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
----- galeria
INSERT INTO project.galeria VALUES(DEFAULT,100,'msi/MSI Optix G241VC.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,101,'msi/MSI Optix G24C4.png','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,102,'msi/MSI Optix G27C4.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,103,'msi/MSI Optix G271.png','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,200,'benq/BenQ EL2870U.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,201,'benq/BenQ ZOWIE XL2411P.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,202,'benq/BenQ PD3200U.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,203,'benq/BenQ MOBIUZ EX2710.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,300,'acer/Acer Nitro VG240YBMIIX.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,301,'acer/Acer Predator XB273GPBMIIPRZX.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,302,'acer/Acer EK220QABI.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,303,'acer/Acer Nitro VG240YUBMIIPX.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,400,'samsung/Samsung C24RG50FQUX.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,401,'samsung/Samsung C27F591FDUX.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,402,'samsung/Samsung C49HG90DMUX.png','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,403,'samsung/Samsung Odyssey C27G75TQSUX.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,500,'iiyama/iiyama G-Master GB2530HSU.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,501,'iiyama/iiyama G-Master GB2730QSU.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,502,'iiyama/iiyama XUB2792QSU.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,503,'iiyama/iiyama XUB2792UHSU-B1 4K.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,600,'aoc/AOC 27G2U.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,601,'aoc/AOC 22V2Q.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,602,'aoc/AOC Q3279VWF.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,603,'aoc/AOC CQ32G1.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,700,'lg/LG 27GL63T-B HDR10.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,701,'lg/LG 27GL850-B NanoIPS.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,702,'lg/LG 24MP59G.jpg','2021-01-01');
INSERT INTO project.galeria VALUES(DEFAULT,703,'lg/LG 27GL83A-B.jpg','2021-01-01');