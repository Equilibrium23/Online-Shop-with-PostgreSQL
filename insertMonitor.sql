-- MSI
-- DROP SEQUENCE msi_id_generator;
CREATE SEQUENCE msi_id_generator INCREMENT 1 MINVALUE 100 MAXVALUE 199;
INSERT INTO project.Monitor VALUES(nextval('msi_id_generator'),1,'MSI Optix G241VC',699,23.6,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('msi_id_generator'),1,'MSI Optix G24C4',899,23.6,'1920x1080',144,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('msi_id_generator'),1,'MSI Optix G27C4',1100,27,'1920x1080',165,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('msi_id_generator'),1,'MSI Optix G271',1200,27,'1920x1080',144,'IPS',250);

-- BenQ
-- DROP SEQUENCE benq_id_generator;
CREATE SEQUENCE benq_id_generator INCREMENT 1 MINVALUE 200 MAXVALUE 299;
INSERT INTO project.Monitor VALUES(nextval('benq_id_generator'),2,'BenQ EL2870U',1200,28,'3840x2160',60,'TN',300);
INSERT INTO project.Monitor VALUES(nextval('benq_id_generator'),2,'BenQ ZOWIE XL2411P',870,27,'1920x1080',144,'TN',350);
INSERT INTO project.Monitor VALUES(nextval('benq_id_generator'),2,'BenQ PD3200U',3200,32,'3840x2160',60,'IPS',300);
INSERT INTO project.Monitor VALUES(nextval('benq_id_generator'),2,'BenQ MOBIUZ EX2710',1400,27,'1920x1080',144,'IPS',400);


-- Acer
-- DROP SEQUENCE acer_id_generator;
CREATE SEQUENCE acer_id_generator INCREMENT 1 MINVALUE 300 MAXVALUE 399;
INSERT INTO project.Monitor VALUES(nextval('acer_id_generator'),3,'Acer Nitro VG240YBMIIX',600,23.8,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('acer_id_generator'),3,'Acer Predator XB273GPBMIIPRZX',1500,27,'1920x1080',144,'IPS',400);
INSERT INTO project.Monitor VALUES(nextval('acer_id_generator'),3,'Acer EK220QABI',400,23.8,'1920x1080',75,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('acer_id_generator'),3,'Acer Nitro VG240YUBMIIPX',23.8,23.8,'1920x1080',75,'IPS',300);

-- Samsung
-- DROP SEQUENCE samsung_id_generator;
CREATE SEQUENCE samsung_id_generator INCREMENT 1 MINVALUE 400 MAXVALUE 499;
INSERT INTO project.Monitor VALUES(nextval('samsung_id_generator'),4,'Samsung C24RG50FQUX',900,23.5,'1920x1080',144,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('samsung_id_generator'),4,'Samsung C27F591FDUX',1200,27,'1920x1080',60,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('samsung_id_generator'),4,'Samsung C49HG90DMUX',3800,49,'1920x1080',144,'VA',350);
INSERT INTO project.Monitor VALUES(nextval('samsung_id_generator'),4,'Samsung Odyssey C27G75TQSUX',2800,27,'2560x1440',240,'VA',350);

-- iiyama
-- DROP SEQUENCE iiyama_id_generator;
CREATE SEQUENCE iiyama_id_generator INCREMENT 1 MINVALUE 500 MAXVALUE 599;
INSERT INTO project.Monitor VALUES(nextval('iiyama_id_generator'),5,'iiyama G-Master GB2530HSU',700,24.5,'1920x1080',75,'TN',250);
INSERT INTO project.Monitor VALUES(nextval('iiyama_id_generator'),5,'iiyama G-Master GB2730QSU',1150,27,'2560x1440',75,'TN',350);
INSERT INTO project.Monitor VALUES(nextval('iiyama_id_generator'),5,'iiyama XUB2792QSU',1300,27,'2560x1440',75,'IPS',350);
INSERT INTO project.Monitor VALUES(nextval('iiyama_id_generator'),5,'iiyama XUB2792UHSU-B1 4K',1600,27,'3840x2160',60,'IPS',300);

-- AOC
-- DROP SEQUENCE aoc_id_generator;
CREATE SEQUENCE aoc_id_generator INCREMENT 1 MINVALUE 600 MAXVALUE 699;
INSERT INTO project.Monitor VALUES(nextval('aoc_id_generator'),6,'AOC 27G2U',1000,27,'1920x1080',144,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('aoc_id_generator'),6,'AOC 22V2Q',500,21.5,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('aoc_id_generator'),6,'AOC Q3279VWF',1100,31.5,'2560x1440',75,'VA',250);
INSERT INTO project.Monitor VALUES(nextval('aoc_id_generator'),6,'AOC CQ32G1',1500,31.5,'2560x1440',144,'VA',300);

-- LG
-- DROP SEQUENCE lg_id_generator;
CREATE SEQUENCE lg_id_generator INCREMENT 1 MINVALUE 700 MAXVALUE 799;
INSERT INTO project.Monitor VALUES(nextval('lg_id_generator'),7,'LG 27GL63T-B HDR10',1050,27,'1920x1080',144,'IPS',320);
INSERT INTO project.Monitor VALUES(nextval('lg_id_generator'),7,'LG 27GL850-B NanoIPS',2000,27,'2560x1440',144,'IPS',350);
INSERT INTO project.Monitor VALUES(nextval('lg_id_generator'),7,'LG 24MP59G',499,23.8,'1920x1080',75,'IPS',250);
INSERT INTO project.Monitor VALUES(nextval('lg_id_generator'),7,'LG 27GL83A-B',1800,27,'2560x1440',144,'IPS',350);

