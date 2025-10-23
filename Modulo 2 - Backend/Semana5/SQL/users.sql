CREATE TABLE lyfter_car_rental.users
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 100 ),
	full_name character varying(50) NOT NULL,
    email character varying(30) NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(25) NOT NULL,
	DOB date NOT NULL,
	account_status character varying(30) NOT NULL,
    PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS lyfter_car_rental.users
    OWNER to postgres;

SET search_path TO lyfter_car_rental;


insert into users (full_name, email, username, password, DOB, account_status) values ('Abner Gallop', 'agallop0@nasa.gov', 'agallop0', 'nC0%G/Q4DUW''rd.j4nUtM#a', '1991-10-06', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Meghan Gossop', 'mgossop1@123-reg.co.uk', 'mgossop1', 'kX7=p=g$?K4yGAKm', '1951-09-29', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Birgit Checkley', 'bcheckley2@marketwatch.com', 'bcheckley2', 'hI6?i?ps*jqkvtmC1YVI', '1989-12-19', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Malorie Tomik', 'mtomik3@microsoft.com', 'mtomik3', 'sX5~h%IQ<7x2hH@98<#"sk', '1988-03-28', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Rees Lacelett', 'rlacelett4@chronoengine.com', 'rlacelett4', 'tK1+K|YP2mn9hl6q6lk$', '1999-12-18', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Thedric Blackbrough', 'tblackbrough5@yellowbook.com', 'tblackbrough5', 'fW5/_9jbtYZi,U', '1950-02-23', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Ogdan Nelligan', 'onelligan6@google.com.br', 'onelligan6', 'iA9@VDl`+)re/lw,oj>Tc', '2004-10-30', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Adolph Rhymer', 'arhymer7@bluehost.com', 'arhymer7', 'aK6<IKE9jPJY', '1987-12-16', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Harrie Pannaman', 'hpannaman8@admin.ch', 'hpannaman8', 'dG8`{d6S/Tbi3@Q."f*qMT,g', '1995-04-26', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Doralin Swinney', 'dswinney9@mit.edu', 'dswinney9', 'gS1"&J2A@mIwjC&Qk!o=H', '1974-11-17', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Willy Tomczynski', 'wtomczynskia@berkeley.edu', 'wtomczynskia', 'xE2%$4"(MCXO', '1986-04-01', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Shirleen Handlin', 'shandlinb@prnewswire.com', 'shandlinb', 'pG9`Ia.Sgyp|8@Zfet`18e%', '1965-08-02', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Monica Francklin', 'mfrancklinc@goo.ne.jp', 'mfrancklinc', 'qP4?W5?QyZt(#M`aTt', '1950-10-29', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Nadeen Larcher', 'nlarcherd@salon.com', 'nlarcherd', 'eJ3)`pssd#tJ6%M$SQrWl%|9', '1994-05-12', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Barbabas Oki', 'bokie@npr.org', 'bokie', 'rC2#%veROk<l.nUUZ,', '1969-08-12', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Roseann Shasnan', 'rshasnanf@bing.com', 'rshasnanf', 'bY4"pnPrpxI<GsvH\aN@bca', '1960-12-04', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Jermain Hapke', 'jhapkeg@vimeo.com', 'jhapkeg', 'bJ3$vK=4~BJI', '1950-08-12', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Quinton Jahner', 'qjahnerh@furl.net', 'qjahnerh', 'jN5|\GOA&kJmER"/~''', '1960-11-12', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Dame Dorwood', 'ddorwoodi@elpais.com', 'ddorwoodi', 'mW0(\"GYJ#1+NG"(V', '1968-12-24', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Merrel Albrook', 'malbrookj@pinterest.com', 'malbrookj', 'aN2+akf%*!8G$p8', '1978-04-21', 'inactive');
insert into users (full_name, email, username, password, DOB, account_status) values ('Jerry Chicchetto', 'jchicchettok@mozilla.com', 'jchicchettok', 'lO0#VFX3SF/t{4''iYs.,', '1960-10-02', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Michail Walne', 'mwalnel@reddit.com', 'mwalnel', 'oM6?A+e)<O6=\@#kHs9|sC*', '1997-03-26', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Debbi Tomasutti', 'dtomasuttim@gmpg.org', 'dtomasuttim', 'aO9|_Uu2lU_GfSU%Dy\a', '1977-01-08', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Purcell Skingle', 'pskinglen@ted.com', 'pskinglen', 'pV9|Fh4z?C_AZu?vI8FV', '1964-06-14', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Helga Blaver', 'hblavero@stanford.edu', 'hblavero', 'zK7{P=dITM{y4*', '1958-10-04', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Armand Gland', 'aglandp@slashdot.org', 'aglandp', 'gF1!hMk_jx0I&', '1999-06-16', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Beckie Verling', 'bverlingq@washingtonpost.com', 'bverlingq', 'uN8_X4#Yz!P1bS+9GcT2g4&I', '1988-01-28', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Patrice Klagges', 'pklaggesr@mashable.com', 'pklaggesr', 'iS5~$AKS.J3668', '1986-03-18', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Bartholemy Lemar', 'blemars@amazon.co.jp', 'blemars', 'eH9}19vWqo5q)+yR+0k', '1961-11-06', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Dyane Tubbs', 'dtubbst@ox.ac.uk', 'dtubbst', 'xC2$B!p"~u.n+CJoLXm@k', '1955-09-07', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Menard Hurkett', 'mhurkettu@cbc.ca', 'mhurkettu', 'fT0}%M6!Osqi{>,0XO6KY', '1989-11-01', 'inactive');
insert into users (full_name, email, username, password, DOB, account_status) values ('Nolie O''Hengerty', 'nohengertyv@dion.ne.jp', 'nohengertyv', 'lQ7@Z~zavKO{LqAhq).~''', '1973-10-04', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Fergus Yakunchikov', 'fyakunchikovw@fda.gov', 'fyakunchikovw', 'gP2@\c*Zg7W''', '1982-04-25', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Aurora Betteney', 'abetteneyx@mit.edu', 'abetteneyx', 'tL5.+"$V?neg.<0\7?zl<', '1959-01-11', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Tynan Guilbert', 'tguilberty@cargocollective.com', 'tguilberty', 'lJ7)_zYz''oqrdgt`zw', '1997-02-14', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Willi Hursthouse', 'whursthousez@cocolog-nifty.com', 'whursthousez', 'bB1=_1w5TN=YC%\w$', '1959-05-20', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Valry Bjorkan', 'vbjorkan10@go.com', 'vbjorkan10', 'pO3`0,H%pii}w}Ni/e', '1983-05-11', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Devina Kelland', 'dkelland11@time.com', 'dkelland11', 'vU9`(e8St43W0_,H<', '1996-10-03', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Tersina Ortells', 'tortells12@bandcamp.com', 'tortells12', 'sA8)w2FMOq*w?&', '1953-07-02', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Sharyl Boullen', 'sboullen13@mozilla.com', 'sboullen13', 'aV6%!gZy/s}VRMCRN', '1986-02-24', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Onfre Gwin', 'ogwin14@fastcompany.com', 'ogwin14', 'mM4\nRm}kk,qer!G@', '1957-03-31', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Charisse Rockall', 'crockall15@wikia.com', 'crockall15', 'fJ3*nk?IVTZFz*2R}6l', '1998-02-02', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Shelby Coping', 'scoping16@hexun.com', 'scoping16', 'mP2''Z3?,rHXlik''+uh3IX', '1998-05-28', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Myranda Eyden', 'meyden17@shop-pro.jp', 'meyden17', 'eT5?mFcNz_#{', '1973-03-29', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Wallace Rowet', 'wrowet18@nydailynews.com', 'wrowet18', 'qY8\v)a.NuI%'',D', '1972-09-19', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Tedie Hickin', 'thickin19@mediafire.com', 'thickin19', 'gI4+Q?~ltpo+$d33i|v+xE~', '1974-09-12', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Hillery Cadd', 'hcadd1a@arizona.edu', 'hcadd1a', 'oO4|1(eLAf=HmMRJ_R', '1957-04-20', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Zaccaria Tewes', 'ztewes1b@earthlink.net', 'ztewes1b', 'fS2!e&ntswo1%f', '1965-01-20', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Germana Sager', 'gsager1c@salon.com', 'gsager1c', 'yT3#\zn}ev''''pE''IZZ+R,', '1963-09-05', 'active');
insert into users (full_name, email, username, password, DOB, account_status) values ('Dominica De Vere', 'dde1d@ebay.co.uk', 'dde1d', 'wO3~xWNB40)=(7UnLx', '2002-12-28', 'inactive');

