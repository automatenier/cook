
import gspread
import os
import re

def format_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if digits.startswith('0'):
        digits = '62' + digits[1:]
    elif digits.startswith('8'):
        digits = '62' + digits
    if len(digits) >= 11:
        return f"{digits[:2]} {digits[2:5]}-{digits[5:9]}-{digits[9:]}"
    return phone

def append_leads():
    creds_path = '.pass/service_account.json'
    client = gspread.service_account(filename=creds_path)
    spreadsheet_id = '1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8'
    sh = client.open_by_key(spreadsheet_id)
    ws = sh.get_worksheet(0) 

    # Clean up previous batch of 158
    total_rows = len(ws.get_all_values())
    if total_rows > 158:
        print(f"Cleaning up previous batch...")
        ws.delete_rows(total_rows - 157, total_rows)

    raw_data = """
1	25/01/2025	Muhammad Ichsan	Ressa yuniar	ressayn06@gmail.com	Jakarta Barat	+6281528796952	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
2	26/01/2025	Lian Pakpahan	Sulaiman Firdaus	sulaimanfirdaus386@gmail.com	Bekasi	+6288806181660	Meta	New Lead	Digital	META Ads	JORDAN
3	27/01/2025	rivaldi	Fajar karunia	fajar.karunia12.fk@gmail.com	Kota Jakarta Timur	+6287741093195	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
4	28/01/2025	Lala	inu nurjanah	inuunurjanah@gmail.com	bandung barat	+6283170000044	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
5	29/01/2025	Fenliung	tio revi	tiorevi@gmail.com	Bogor	+6287873777804	Meta	New Lead	Digital	META Ads	JORDAN
6	30/01/2025	rivaldi	Achmad Sofian	achmadsofianas12@gmail.com	Jakarta Utara	+6287789033386	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
7	31/01/2025	tiara	Jhon Chen Van Parhusip	chenvanjhon@yahoo.com	Bandung	+6281336384181	Meta	New Lead	Digital	META Ads	JORDAN
8	28/02/2025 23:11:40	Bayu	pullajaa	saepulmizan150910@gmail.com	mbung anjing	+62881022110967		RUMAH	New Lead	Meta FB/IG	JORDAN
9	28/02/2025 07:08:39	lian	media Horizontal	mediahozt@gmail.com	Jakarta	+628161860789		RUMAH	New Lead	Meta FB/IG	JORDAN
10	26/02/2025 22:33:20	ademaulana	Archil Ckll	mhmdsehasehha@gmail.com	Bandung	+6285871769832		RUMAH	New Lead	Meta FB/IG	JORDAN
11	26/02/2025 06:55:58	lian	pandu adit	aditpandu31@gmail.com	Bekasi	+6285814847300		RUMAH	New Lead	TikTok Ads	JORDAN
12	24/02/2025 20:48:57	Nunik Sulistyowati	Fauzi	witadjuwita1@gmail.com	Dewi	+6281910218716		RUMAH	New Lead	Meta FB/IG	JORDAN
13	24/02/2025 07:20:28	lian	Aburubayyie Muhammadamir	aburubayyie@gmail.com	Jakarta	081281372036		RUMAH	New Lead	General Website	JORDAN
14	23/02/2025 14:37:07	lian	Iman Aja'ahh	imanajaah8@gmail.com	Medan	+6282368279159		RUMAH	New Lead	Meta FB/IG	JORDAN
15	22/02/2025 21:37:15	lian	Raymond Pardede	raymondprdd@gmail.com	Bekasi	+6281289681253		RUMAH	New Lead	Meta FB/IG	JORDAN
16	21/02/2025 22:59:39	Muhammad Ichsan	Anggiani Syarifatul Maulidah	anggiafama25@gmail.com	Cikarang	+6282128842821		RUMAH	New Lead	TikTok Ads	JORDAN
17	21/02/2025 13:50:23	Lala	david ruland David	rulandd672@gmail.com	Kota Tangerang	+6282267465517		RUMAH	New Lead	TikTok Ads	JORDAN
18	20/02/2025 16:47:45	lian	RezaF Karundeng	rezafkarundeng@gmail.com	Jakarta Pusat	+6285762221931		RUMAH	New Lead	TikTok Ads	JORDAN
19	19/02/2025 08:45:53	Nunik Sulistyowati	Nikmatulloh	ullohnikmat@gmail.com	Bekasi	087776622821		RUMAH	New Lead	General Website	JORDAN
20	18/02/2025 17:48:18	Fenliung	Wongky razhu	wongkyrazhu@gmail.com	Bali	081211141114		RUKO	New Lead	General Website	JORDAN
21	17/02/2025 21:29:44	lian	devi ks	devikartikasari26@gmail.com	Bandung	+628987324776		RUMAH	New Lead	Meta FB/IG	JORDAN
22	17/02/2025 16:53:28	Nunik Sulistyowati	Katerina putri	sangputridewiirma6596@gmail.com	Jakarta Selatan	085774416896		RUMAH	New Lead	General Website	JORDAN
23	16/02/2025 17:57:42	Lala	Bilqis Hikmah	bilqisdurotulhikmah91@gmail.com	Bilqs	+6281395445513		RUMAH	New Lead	Meta FB/IG	JORDAN
24	15/02/2025 15:35:22	Muhammad Ichsan	Mangupengg	anggsupriatna2118@gmail.com	Rancaekek	+6281299499637		RUMAH	New Lead	Meta FB/IG	JORDAN
25	14/02/2025 19:26:22	Fenliung	habibi	hbibimhammad@gmail.com	Bandung	008997647002		RUMAH	New Lead	Meta FB/IG	JORDAN
26	14/02/2025 07:05:53	Fenliung	Riza	nurhudariza@gmail.com	Bekasi	081310621921		RUMAH	New Lead	General Website	JORDAN
27	13/02/2025 17:02:51	Fenliung	Carolina Ningo	carolina_ningo@yahoo.com	Joglo	+60168774045		RUMAH	New Lead	TikTok Ads	JORDAN
28	13/02/2025 05:17:48	rivaldi	RidwanKurniawan	ridwankurniawan13939@gmail.com	Kawali ciamis	+6282126668443		RUMAH	New Lead	Meta FB/IG	JORDAN
29	12/02/2025 06:19:29	lian	Febri Era era	febriera29@gmail.com	Jakarta Timur	+6285945581179		RUMAH	New Lead	TikTok Ads	JORDAN
30	11/02/2025 07:10:19	Fenliung	Putera	rlputra09@gmail.com	Cikarang	+6281314948918		RUMAH	New Lead	Meta FB/IG	JORDAN
31	09/02/2025 21:43:19	Nunik Sulistyowati	Roby	martasila811@gmail.com	Pati	+6282333820226		RUMAH	New Lead	Meta FB/IG	JORDAN
32	09/02/2025 03:23:59	Lala	Juanfran	juanzulaika0123@gmail.com	Bogor	088299784749		RUMAH	New Lead	General Website	JORDAN
33	07/02/2025 21:19:26	Lala	Pjs Bdg Automotive Equipment	pjsbdg911@gmail.com	Bandung	+6281572030580		RUMAH	New Lead	Meta FB/IG	JORDAN
34	06/02/2025 16:34:13	Muhammad Ichsan	Sofian Ansori	kancilpian12@gmail.com	Tasikmalaya	+62895405610816		RUMAH	New Lead	Meta FB/IG	JORDAN
35	05/02/2025 12:54:28	Bayu	supriatna supriatna	supriatnaadhya@gmail.com	Bekasi Regency	+6287824009646		RUMAH	New Lead	TikTok Ads	JORDAN
36	04/02/2025 13:52:55	lian	رحمات رحمات	noyoud234@gmail.com	Bandung	+6283899919898		RUMAH	New Lead	Meta FB/IG	JORDAN
37	03/02/2025 23:35:43	Muhammad Ichsan	Putra	sanjayputraherlmbang8q@gmail.com	Jakarta Utara	088224877155		RUMAH	New Lead	General Website	JORDAN
38	02/02/2025 22:53:36	lian	joko adi pribadi	sijokul210588@gmail.com	banjar patroman	+6281324084859		RUMAH	New Lead	TikTok Ads	JORDAN
39	02/02/2025 07:37:33	Bayu	Kinan	kinantiulyasa@gmail.com	Karawang	0895702707462		RUMAH	New Lead	General Website	JORDAN
40	01/02/2025 19:03:53	rivaldi	Fadlhan Husaeny	fadlhanhusaeny@gmail.com	bandung	+628999027916		RUMAH	New Lead	Meta FB/IG	JORDAN
41	01/03/2025	Muhammad Ichsan	Dewa Putranto	pps.kgt@gmail.com	Jakarta	+6285817701729	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
42	02/03/2025	ade maulana	Nisa Nurhasanah	nisa_zambrota@yahoo.com	Bekasi	+6281211677230	Meta	New Lead	Digital	META Ads	JORDAN
43	02/03/2025	muppy	𝕯𝖊𝖗𝖗𝖊𝖓 𝕮𝖍𝖗𝖎𝖘𝖙𝖔𝖋𝖊𝖗 𝕷𝖎𝖒𝖓𝖆𝖗𝖙𝖆	derrenliem2@gmail.com	Tangerang	+6281316791828	Meta	New Lead	Digital	META Ads	JORDAN
44	03/03/2025	Bayu	Guguja Wenamtol Karek	celinapapua@gmail.com	Wonda	+6281258597418	Meta	New Lead	Digital	META Ads	JORDAN
45	03/03/2025	ade maulana	Dewi	dewi@gmail.com	Bekasi	085283318799	-	New Lead	Digital	Whatsapp	JORDAN
46	04/03/2025	Lian Pakpahan	DianCheisar	diancheisar@gmail.com	Bekasi	+6285691851386	Meta	New Lead	Digital	META Ads	JORDAN
47	06/03/2025	Lian Pakpahan	Daniel	revine.daniel@gmail.com	Jakarta	008111988208	Meta	New Lead	Digital	META Ads	JORDAN
48	07/03/2025	Bayu	Rizki Budie Kusuma	rizkikusuma672@gmail.com	Cibarusah	0085691425528	Meta	New Lead	Digital	META Ads	JORDAN
49	07/03/2025	muppy	Dwi Wahyu Nugroho	dwiwahyunugroho88@gmail.com	Yogyakarta City	+6281222446202	Meta	New Lead	Digital	META Ads	JORDAN
50	08/03/2025	Lian Pakpahan	wiweweeeee	weninuranggraeni609@gmail.com	Weni nuranggraeni	+6289626470901	Meta	New Lead	Digital	META Ads	JORDAN
51	09/03/2025	rivaldi	Afandi	fandi.mohammad68@gmail.com	Cibubur	087738000988	Call Me	New Lead	Digital	Website	JORDAN
52	10/03/2025	Fenliung	Irsan Junud	junud094@gmail.com	Soe	+628114398870	Meta	New Lead	Digital	META Ads	JORDAN
53	11/03/2025	Muhammad Ichsan	NoviTrianto	hanmaulana78@gmail.com	Jakarta	+6282289855218	Meta	New Lead	Digital	META Ads	JORDAN
54	11/03/2025	Nunik Sulistyowati	Diyana Eka Sari	diekri48@gmail.com	Cikarang	+628159971692	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
55	12/03/2025	Lala	sidiq.nur	nursidik1881@gmail.com	Bekasi	+6285920553010	Meta	New Lead	Digital	META Ads	JORDAN
56	13/03/2025	Lala	Aryana Ayu Shahab	aryanaayuamandani@gmail.com	Bekasi	+6285228157231	Meta	New Lead	Digital	META Ads	JORDAN
57	13/03/2025	Lala	Deka Fadlila	dekafadlilaputra@gmail.com	Cibubur	081296566151	Brosur	New Lead	Digital	Website	JORDAN
58	15/03/2025	Lala	Tedy Nugraha	tedy@gm.com	Depok	+6285851449661	Meta	New Lead	Digital	META Ads	JORDAN
59	15/03/2025	Lala	Dini Agustina	dini.9893@gmail.com	Cikarang	+6281219101448	Meta	New Lead	Digital	META Ads	JORDAN
60	16/03/2025	Lala	Silvi Marliana	silvimarliana2229@gmail.com	Cikarang	085863567049	Call Me	New Lead	Digital	Website	JORDAN
61	17/03/2025	Lala	Panca Calvin Sianipar	calvinpanca@gmail.com	Karawang	+6282310698876	Meta	New Lead	Digital	META Ads	JORDAN
62	17/03/2025	Lala	Iqbal Tanuwijaya	iqbaltanuwijaya@gmai.com	Bekasi	081296009595	Brosur	New Lead	Digital	Website	JORDAN
63	18/03/2025	Lala	Bhima Chandra Bhuana Bhima	cb.bhima@gmail.com	South Tangerang	+6281289883441	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
64	19/03/2025	ade maulana	hermawan susanto	santo1987batman@yahoo.co.id	Jakarta	+6285264674189	Meta	New Lead	Digital	META Ads	JORDAN
65	19/03/2025	rivaldi	herman	herman420@gmail.com	Bekasi	081617208957	Brosur	New Lead	Digital	Website	JORDAN
66	20/03/2025	Fenliung	gembel eliet	wawanwahid031@gmail.com	Cikarang	0081210387128	Meta	New Lead	Digital	META Ads	JORDAN
67	21/03/2025	Fenliung	Septi Indah Wulandari	septiwulandarii2017@gmail.com	Bogor	+6289690072599	Meta	New Lead	Digital	META Ads	JORDAN
68	22/03/2025	Muhammad Ichsan	Ummu Adzkia_ Al'Fawwaz	septianahanunanggit@gmail.com	Bekasi	+6285693478112	Meta	New Lead	Digital	META Ads	JORDAN
69	23/03/2025	Nunik Sulistyowati	Arif Nugraha	bonoz_31@yahoo.co.id	Jakarta	+6281377072772	Meta	New Lead	Digital	META Ads	JORDAN
70	22/03/2025	Nunik Sulistyowati	Reza	reza@gmail.com	Bekasi	081294099951	-	New Lead	Digital	Instagram Ads Office	JORDAN
71	24/03/2025	Lala	rayhan fahrezi gunawan	rayhanfahrezi218@gmail.com	Cikarang pusat	0088210889671	Meta	New Lead	Digital	META Ads	JORDAN
72	25/03/2025	Lala	Hikmat Muhammad	hikmat_muhamad87@yahoo.co.id	Bekasi	+6285695078639	Meta	New Lead	Digital	META Ads	JORDAN
73	26/03/2025	ade maulana	hoe	ieuasdaqoiue@gmail.com	Parung	08973217391	Call Me	New Lead	Digital	Website	JORDAN
74	27/03/2025	Wilda	Mate Hermawan	rahmat.hermawan08@gmail.com	Bekasi	+6282114296863	Meta	New Lead	Digital	META Ads	JORDAN
75	27/03/2025	rivaldi	Gilang SanaSini	gilangmuhammadhs@gmail.com	Jatinangor	+6287816985146	Meta	New Lead	Digital	META Ads	JORDAN
76	28/03/2025	Muhammad Ichsan	Fuad Widiatmoko	fuadwidiatmoko7@gmail.com	Cikarang	087840058296	Call Me	New Lead	Digital	Website	JORDAN
77	28/03/2025	Bayu	Arya Darmawan	darmawanarya0899@gmail.com	Karawang	+6281294712321	Meta	New Lead	Digital	META Ads	JORDAN
78	29/03/2025	muppy	Budi Pamungkas	budi.pamungkas39@gmail.com	Karawang	081381069895	Brosur	New Lead	Digital	Website	JORDAN
79	30/03/2025	rivaldi	P.Kharisma	puguhkharisma.pk@gmail.com	karawang	+6287899502977	Meta	New Lead	Digital	META Ads	JORDAN
80	31/03/2025	Muhammad Ichsan	Ifud	ifudg@yahoo.co.id	Bekasi	082188164345	120219675216751000	New Lead	Digital	Website	JORDAN
81	31/03/2025	ade maulana	Iqball Alfikri	iqballalfikri16@gmail.com	Bandung	+6283829907503	Meta	New Lead	Digital	META Ads	JORDAN
82	30/04/2025	Fenliung	Dimas	abdurasyiidfikarse@gmail.com	Cikarang	082120556639	Call Me	New Lead	Digital	Website	JORDAN
83	14/04/2025	Lian Pakpahan	Adinda Prastika	adindaprastika05@gmail.com	Kabupaten Kota Bekasi	+6285222143812	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
84	25/04/2025	Aira	Dian	agsyam88@gmail.com	Tasikmalaya	085353994725	Brosur	New Lead	Digital	Website	JORDAN
85	30/04/2025	Nunik Sulistyowati	aimar husein	aimarimamhusein26@gmail.com	Jakarta Barat	+6281283993994	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
86	27/04/2025	Lian Pakpahan	Tobu	alifardianysah22@gmil.com	Muarabungo	+62895412962650	Meta	New Lead	Digital	META Ads	JORDAN
87	11/04/2025	Agent	Andi	andi38028@gmail.com	Bandung	081285707092	Brosur	New Lead	Digital	Website	JORDAN
88	29/04/2025	Rian	Anwar	anwar@gmail.com	jakarta	081381858498	-	New Lead	Digital	META Ads	JORDAN
89	07/04/2025	Fenliung	Aryo Yoka	aryo_van7@yahoo.co.id	Jakarta	+628158028949	Meta	New Lead	Digital	META Ads	JORDAN
90	07/04/2025	Lian Pakpahan	Bagas Wicaksono	bagas2444@yahoo.co.id	Bekasi	+6287863239235	Meta	New Lead	Digital	META Ads	JORDAN
91	24/04/2025	Astuti	Andhika Boy	boyandhika82@gmail.com	Bekasi	+62812345445	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
92	09/04/2025	Bayu	Cholid Rudy Susanto	cholidrudy373@gmail.com	Nganjuk	+6285234138350	Meta	New Lead	Digital	META Ads	JORDAN
93	12/04/2025	muppy	Dafa Ar	davacsxcsx@gmail.com	dava csx csx	+62895365077769	Meta	New Lead	Digital	META Ads	JORDAN
94	01/04/2025	muppy	Dika Hanggara	dika.hanggara70@gmail.com	Bekasi	+6287833227758	Meta	New Lead	Digital	META Ads	JORDAN
95	27/04/2025	Lala	Irsyadul Fikri	dudulhansamu@rocketmail.com	Amsterdam	+818019848895	Meta	New Lead	Digital	META Ads	JORDAN
96	11/04/2025	Wilda	Endra White	endrawhite18@gmail.com	Kota Administrasi Jakarta Utara	+6281311396998	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
97	28/04/2025	Fenliung	Zidd Real	ezigendut062@gmail.com	Kuningan	+6289504959424	Meta	New Lead	Digital	META Ads	JORDAN
98	05/04/2025	Lian Pakpahan	Peti	fauziahpeti@gmail.com	Tambun Selatan	085691338526	Brosur	New Lead	Digital	Website	JORDAN
99	20/04/2025	Lian Pakpahan	Chicko	grabrgm@gmail.com	Bekasi	+6285772185099	Meta	New Lead	Digital	META Ads	JORDAN
100	30/04/2025	Fenliung	Harris Pratama	harrispratama527@gmail.com	JAKARTA UTARA	+6288296968606	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
101	01/04/2025	Bayu	Heryana Amri	heryana.amri@gmail.com	Cikarang	+628111043267	Meta	New Lead	Digital	META Ads	JORDAN
102	07/04/2025	Muhammad Ichsan	Ilyas	ilyasamiftahudin59@gmail.com	Lampung	+6283822760207	Meta	New Lead	Digital	META Ads	JORDAN
103	07/04/2025	rivaldi	moh irfan irfan	irf120771@gmail.com	Kota Bekasi kranji	+6285283139103	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
104	12/04/2025	muppy	Jayadi	jayadimitra@gmail.com	Bekasi	+6287803415965	Meta	New Lead	Digital	META Ads	JORDAN
105	14/04/2025	muppy	YeniJuliyani	julliel460@gmail.com	Cikarang	+628888633911	Meta	New Lead	Digital	META Ads	JORDAN
106	16/04/2025	Fenliung	RefanGz	kishiofficiall@gmail.com	Bandung	+6285720279905	Meta	New Lead	Digital	META Ads	JORDAN
107	17/04/2025	Fenliung	Yayah Muzakiyatul Fitri	laudyamouza@gmail.com	Bekasi	+6285721670994	Meta	New Lead	Digital	META Ads	JORDAN
108	29/04/2025	Aira	Novi T	Maliqa0811@gmail.com	Jakarta	+6281585506453	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
109	17/04/2025	Lala	Muhammad Diki Effendi	mdickyeffendi171291@gmail.com	Jakarta Pusat	06285778111207	Call Me	New Lead	Digital	Website	JORDAN
110	24/04/2025	muppy	Renoirco	mhsyaefudin8@gmail.com	Cikarang	+6282249029207	Meta	New Lead	Digital	META Ads	JORDAN
111	10/04/2025	Muhammad Ichsan	@aganpeot_	muhammadafghaniramadhan@gmail.com	Bandung	+6285187967296	Meta	New Lead	Digital	META Ads	JORDAN
112	04/04/2025	Lian Pakpahan	naufal Wahid	naufal.tejo@yahoo.com	jakarta	+6281286388941	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
113	18/04/2025	Fenliung	Novya	noviawulandari1998@gmail.com	Kerawang	017660016073	Brosur	New Lead	Digital	Website	JORDAN
114	19/04/2025	muppy	Oky	okyhilda04@gmail.com	Bekasi	081315153451	Brosur	New Lead	Digital	Website	JORDAN
115	19/04/2025	Bayu	Patricia Fian	patricia0125pp@gmail.com	Kota Bekasi	+6281326100100	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
116	06/04/2025	muppy	Joko Ebezz	qnantea@gmail.com	Cikarang	+6281214167876	Meta	New Lead	Digital	META Ads	JORDAN
117	23/04/2025	Bayu	رفا سيتي آرياني	refasitiaryani@gmail.com	Refa	+6285724019267	Meta	New Lead	Digital	META Ads	JORDAN
118	05/04/2025	rivaldi	Rian Destrieyanto	riandestrieyanto18@gmail.com	Karawang	089655694097	Call Me	New Lead	Digital	Website	JORDAN
119	30/04/2025	Lian Pakpahan	Sugeng riyadi	riyadimsr@gmail.com	Batang	+6282271507756	Meta	New Lead	Digital	META Ads	JORDAN
120	03/04/2025	Bayu	Rully Putra	rully0811@gmail.com	Bekasi	+6281319774184	Meta	New Lead	Digital	META Ads	JORDAN
121	07/04/2025	ade maulana	SERA	selarafikana@gmail.com	Palembang	+6285783913575	Meta	New Lead	Digital	META Ads	JORDAN
122	27/04/2025	Astuti	Siva H	sifa.hasanah@gmail.com	Kota Administrasi Jakarta Timur	+628111789954	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
123	28/04/2025	Muhammad Ichsan	Ajeng P	sriajengprameswari2@gmail.com	South Jakarta	+6282240871828	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
124	15/04/2025	Bayu	Syahlimatul Sadiah	syahlimatuls@gmail.com	Bekasi	0895338473800	Brosur	New Lead	Digital	Website	JORDAN
125	04/04/2025	Nunik Sulistyowati	Anti	taz24taz09@gmail.com	Bekasi	081388710592	120218567877141000	New Lead	Digital	Website	JORDAN
126	06/04/2025	rivaldi	Yudha Irwansyah	uzumaki.kabuto123@gmail.com	Semarang	+6281228630100	Meta	New Lead	Digital	META Ads	JORDAN
127	06/04/2025	Fenliung	John Nainggolan Golan	voltanainggolan87@gmail.com	Kota Bekasi	+6282260863455	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
128	20/04/2025	Muhammad Ichsan	William Ariowibowo Kadar	william.ariowibowo@gmail.com	Bandung	081321076800	120220961075301000	New Lead	Digital	Website	JORDAN
129	17/04/2025	Fenliung	Yusup	yusup@gmail.com	Karawang	085121067654	-	No Response	Digital	Instagram Ads Office	JORDAN
130	01/06/2025	Astuti	Novi	ryanovierwb1@gmail.com	Tangsel	085225871996	Brosur	New Lead	Digital	Website	JORDAN
131	02/06/2025	Muhammad Ichsan	Tias Leite	julidejesus576@gmail.com	T	+6285133547548	Meta	New Lead	Digital	META Ads	JORDAN
132	03/06/2025	Muhammad Ichsan	Dewi C Dewi	cristiyantidewi@ymail.com	Jakarta Pusat	+6282298268846	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
133	04/06/2025	Muhammad Ichsan	Isye Ristiyanti	isye.ristiyanti26@gmail.com	bandung	+6285101801260	Meta	New Lead	Digital	META Ads	JORDAN
134	06/06/2025	Lala	Firmansyah Said	firmansyahsaid93@gmail.com	Jakarta	+6287783006212	Meta	New Lead	Digital	META Ads	JORDAN
135	08/06/2025	Lala	azaz test	azaz@savasa.id	Bekasi	0892342348234	Call Me	New Lead	Digital	Website	JORDAN
136	09/06/2025	ade maulana	priyatna hadi santoso	hdi212oakley@gmail.com	Jakarta	+6285714191329	Meta	New Lead	Digital	META Ads	JORDAN
137	09/06/2025	Bayu	Sosan Elen Sosan elen	Sosanelen580@gmail.com	Kab. Bekasi	+6285778596580	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
138	11/06/2025	Bayu	Muhammad Marpaung	mronijanesmarpaunh@gmail.com	Kab. Bekasi	+6282333021197	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
139	12/06/2025	ade maulana	Raden Reggie Winaldy	reggiwinaldy23@gmail.com	Bekasi	+6282260170738	Meta	New Lead	Digital	META Ads	JORDAN
140	13/06/2025	Rian	Tumpuk Priyo	xeuxi09@gmail.com	Jakarta	+628174958637	Meta	New Lead	Digital	META Ads	JORDAN
141	13/06/2025	Astuti	Filius Oktario	filiusoktario@yahoo.co.id	Pangkalpinang	+628117172251	Meta	New Lead	Digital	META Ads	JORDAN
142	14/06/2025	edi kurniawan	Miqdad Zaidan Alkhair	miqdad.khair3@gmail.com	Jakarta	+628119988700	Meta	New Lead	Digital	META Ads	JORDAN
143	15/06/2025	Fenliung	Darius Candra	dariuscandra16@gmail.com	Jakarta	+6281287989637	Meta	New Lead	Digital	META Ads	JORDAN
144	16/06/2025	Lala	Dw Bspak	dewi.sw0202@gmail.com	Bekesong	+6285777737869	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
145	16/06/2025	Bayu	ALA PIKO COFFEE	Hidrianiy@gmail.com	Lampung	081271128081	Meta	New Lead	Digital	META Ads	JORDAN
146	17/06/2025	ade maulana	Achii Prastyo	karsihnovitasari2592@gmail.com	Cikarang	+6285924332484	Meta	New Lead	Digital	META Ads	JORDAN
147	17/06/2025	Rian	Jundullah	jundullahalhasany26@gmail.com	Tambun Selatan Bekasi	+628811938067	Meta	New Lead	Digital	META Ads	JORDAN
148	18/06/2025	Aira	Moses Dhony	cy_mdp@yahoo.com	Jakarta	+6281353795480	Meta	New Lead	Digital	META Ads	JORDAN
149	20/06/2025	edi kurniawan	DINA PUSPITA NINGRUM	dnpsptnngrm@gmail.com	Bekasi	085891834535	Brosur	New Lead	Digital	Website	JORDAN
150	21/06/2025	Lala	indah Dwi utari	nandapraseptia42@gmail.com	Kota Bekasi	+6281210298992	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
151	22/06/2025	Bayu	Febriansyah	febriansyahg1@gmail.com	Cibitung	081219592596	Call Me	New Lead	Digital	Website	JORDAN
152	23/06/2025	ade maulana	Salam Jamal	kaisarperkeleng@gmail.com	Jakarta	+628111548880	Meta	New Lead	Digital	META Ads	JORDAN
153	24/06/2025	Rian	Gathany	hartono805.c@gmail.com	Jakarta	+6281292873906	Meta	New Lead	Digital	META Ads	JORDAN
154	25/06/2025	Rian	Muslim	Muslimmusaz29@gmail.com	Bekasi	085758392130	Call Me	New Lead	Digital	Website	JORDAN
155	26/06/2025	Astuti	aqilla Melisa	aqillacaramello@gmail.com	Jakarta Barat	+6281282312525	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
156	28/06/2025	Astuti	Sopie	sofiefabruar@gmail.com	Jakarta	087741335973	Call Me	New Lead	Digital	Website	JORDAN
157	29/06/2025	Aira	MUHAMMAD FATIHUL HAQ	0365aispku@gmail.com	Bengkalis	083148997465	Call Me	New Lead	Digital	Website	JORDAN
158	30/06/2025	Fenliung	Tulush Fernando alvaro	tulushfernando83@gmail.com	Jakarta Timur	+6281298066972	Tiktok	New Lead	Digital	TikTok Ads	JORDAN
    """

    headers = ws.row_values(1)
    
    rows_to_append = []
    lines = raw_data.strip().split('\n')
    
    for line in lines:
        parts = line.split('\t')
        if len(parts) < 12: continue
        
        full_date = parts[1].split(' ')[0] 
        date_dm = "/".join(full_date.split('/')[:2]) 
        
        name = parts[3]
        phone = parts[6]
        
        # WE BUILD THE ROW EXACTLY AS REQUESTED (HARDCODED COLS)
        # Col A (0): FALSE
        # Col B (1): Phone Number
        # Col C (2): Name
        # Col D (3): Date
        # Col E (4): Status
        # Col F (5): Qualified
        # Col G (6): Lead
        # Col H (7): Source
        # Col I (8): FU Date
        
        row = [""] * len(headers)
        row[0] = "FALSE"
        row[1] = format_phone(phone)
        row[2] = name
        row[3] = date_dm
        row[4] = "Cold"
        row[5] = "Qualified"
        row[6] = "Lead"
        row[7] = "DB Pak Firman"
        row[8] = "20/03/2026"
        
        # Fill rest with FALSE for Close/Close Rate if they exist
        if len(row) > 14: row[14] = "FALSE"
        if len(row) > 15: row[15] = "FALSE"
        
        rows_to_append.append(row)

    if rows_to_append:
        ws.append_rows(rows_to_append, value_input_option="USER_ENTERED")
        print(f"Successfully appended {len(rows_to_append)} leads with EXACT POSITIONAL FORMATTING.")

if __name__ == "__main__":
    append_leads()
