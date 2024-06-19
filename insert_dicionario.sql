select * from  `grupo_economico`.`dicionario`

truncate table `grupo_economico`.`dicionario`

#Insert dicionario empresas
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('empresas','porte',3,'Empresa de Pequeno Porte');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('empresas','porte',0,'Não Informado');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('empresas','porte',1,'Micro Empresa');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('empresas','porte',5,'Demais');

#Insert dicionario socios
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',2,'Entre 13 e 20 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',3,'Entre 21 e 30 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',4,'Entre 31 e 40 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',5,'Entre 41 e 50 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',6,'Entre 51 e 60 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',7,'Entre 61 e 70 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',8,'Entre 71 e 80 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',1,'Entre 0 e 12 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',9,'Mais de 80 anos');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','faixa_etaria',0,'Não se aplica');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',67,'Titular Pessoa Física Incapaz ou Relativamente Incapaz (exceto menor)');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',71,'Conselheiro de Administração Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',57,'Sócio Comanditário Pessoa Jurídica Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',66,'Titular Pessoa Física Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',65,'Titular Pessoa Física Residente ou Domiciliado no Brasil');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',74,'Sócio-Administrador Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',56,'Sócio Comanditário Pessoa Física Residente no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',68,'Titular Pessoa Física Menor (Assistido/Representado)');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',70,'Administrador Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',73,'Presidente Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',79,'Titular Pessoa Jurídica Domiciliada no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',29,'Sócio Incapaz ou Relat.Incapaz (exceto menor)');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',37,'Sócio Pessoa Jurídica Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',62,'Representante da Instituição Extraterritorial');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',75,'Fundador Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',78,'Titular Pessoa Jurídica Domiciliada no Brasil');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',72,'Diretor Residente ou Domiciliado no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',48,'Sócio Pessoa Jurídica Domiciliado no Brasil');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',41,'Representante de Organização Internacional');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',46,'Ministro de Estado das Relações Exteriores');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',34,'Titular de Empresa Individual Imobiliária');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',38,'Sócio Pessoa Física Residente no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',47,'Sócio Pessoa Física Residente no Brasil');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',55,'Sócio Comanditado Residente no Exterior');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',30,'Sócio Menor (Assistido/Representado)');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',51,'Candidato a cargo Político Eletivo');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',8,'Conselheiro de Administração');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',58,'Sócio Comanditário Incapaz');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',64,'Administrador Judicial');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',20,'Sociedade Consorciada');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',19,'Síndico (Condomínio)');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',61,'Responsável indígena');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',42,'Oficial de Registro');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',49,'Sócio-Administrador');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',63,'Cotas em Tesouraria');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',25,'Sócio Comanditário');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',26,'Sócio de Indústria');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',69,'Beneficiário Final');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',21,'Sociedade Filiada');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',23,'Sócio Capitalista');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',24,'Sócio Comanditado');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',52,'Sócio com Capital');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',53,'Sócio sem Capital');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',60,'Cônsul Honorário');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',31,'Sócio Ostensivo');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',59,'Produtor Rural');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',0,'Não informada');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',5,'Administrador');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',12,'Inventariante');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',28,'Sócio-Gerente');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',11,'Interventor');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',43,'Responsável');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',13,'Liquidante');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',16,'Presidente');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',17,'Procurador');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',18,'Secretário');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',33,'Tesoureiro');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',50,'Empresário');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',39,'Diplomata');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',32,'Tabelião');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',54,'Fundador');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',9,'Curador');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',10,'Diretor');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',40,'Cônsul');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',22,'Sócio');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',35,'Tutor');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',14,'Mãe');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','qualificacao',15,'Pai');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','tipo',1,'Pessoa Jurídica');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','tipo',2,'Pessoa Física');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('socios','tipo',3,'Estrangeiro');

#Insert dicionario estabelecimento
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','identificador_matriz_filial',1,'Matriz');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','identificador_matriz_filial',2,'Filial');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','situacao_cadastral',3,'Suspensa');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','situacao_cadastral',8,'Baixada');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','situacao_cadastral',4,'Inapta');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','situacao_cadastral',2,'Ativa');
INSERT INTO `grupo_economico`.`dicionario` (`id_tabela`, `nome_coluna`, `chave`, `valor`) VALUES ('estabelecimentos','situacao_cadastral',1,'Nula');


