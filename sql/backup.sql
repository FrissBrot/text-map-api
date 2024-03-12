--
-- PostgreSQL database dump
--

-- Dumped from database version 15.6 (Debian 15.6-0+deb12u1)
-- Dumped by pg_dump version 15.6 (Debian 15.6-0+deb12u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: map; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA map;


ALTER SCHEMA map OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: chunks; Type: TABLE; Schema: map; Owner: postgres
--

CREATE TABLE map.chunks (
    id bigint NOT NULL,
    x bigint NOT NULL,
    y bigint NOT NULL,
    borders_on json,
    runtime integer,
    points integer
);


ALTER TABLE map.chunks OWNER TO postgres;

--
-- Name: points; Type: TABLE; Schema: map; Owner: postgres
--

CREATE TABLE map.points (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE map.points OWNER TO postgres;

--
-- Data for Name: chunks; Type: TABLE DATA; Schema: map; Owner: postgres
--

COPY map.chunks (id, x, y, borders_on, runtime, points) FROM stdin;
1	0	0	[]	0	\N
2	0	1	[]	0	\N
3	0	2	[]	0	\N
7	0	6	[]	0	\N
8	0	7	["9"]	3	\N
9	0	8	["8", "10", "20"]	5	\N
10	0	9	["9", "11"]	3	\N
11	0	10	["10"]	1	\N
12	1	0	[]	0	\N
13	1	1	[]	0	\N
18	1	6	["17", "30"]	3	2
19	1	7	[]	1	\N
20	1	8	["9", "30"]	3	\N
21	1	9	[]	0	\N
22	1	10	[]	0	\N
23	2	0	[]	0	\N
24	2	1	["25", "35"]	2	\N
28	2	5	[]	0	\N
29	2	6	[]	0	\N
30	2	7	["18", "20", "41", "31"]	4	\N
31	2	8	["30", "44"]	3	\N
32	2	9	[]	0	\N
33	2	10	[]	0	\N
34	3	0	["46", "35"]	1	\N
35	3	1	["34", "24"]	2	\N
40	3	5	["51", "41"]	2	\N
41	3	6	["30", "40"]	3	\N
42	3	7	[]	0	\N
43	3	8	[]	0	\N
44	3	9	["45"]	3	\N
45	3	10	["44", "55"]	1	\N
46	4	0	["34", "57"]	3	\N
47	4	1	["48"]	2	\N
48	4	2	["36"]	1	\N
49	4	3	[]	0	\N
51	4	5	["40", "50"]	1	\N
52	4	6	[]	0	\N
53	4	7	["53", "64"]	1	\N
54	4	8	["53", "55"]	2	\N
55	4	9	["45", "54"]	3	\N
56	4	10	[]	0	\N
59	5	2	[]	0	\N
60	5	3	[]	0	\N
61	5	4	["50", "62"]	1	\N
62	5	5	["61", "73", "63"]	3	\N
63	5	6	["62", "64"]	3	4
64	5	7	["53", "63"]	2	\N
65	5	8	[]	0	\N
66	5	9	[]	0	\N
67	5	10	["77"]	0	\N
68	6	0	[]	0	\N
70	6	2	["69", "80", "81"]	2	\N
71	6	3	["72", "82"]	2	\N
72	6	4	["71", "73"]	3	\N
73	6	5	["72", "62", "84"]	3	\N
74	6	6	[]	0	\N
75	6	7	[]	1	\N
76	6	8	["86", "77"]	3	\N
77	6	9	["67", "76", "88"]	3	\N
78	6	10	[]	0	\N
79	7	0	[]	0	\N
80	7	1	["70", "81"]	2	\N
81	7	2	["70", "80", "92", "82"]	2	3
82	7	3	["71", "81", "93"]	1	\N
83	7	4	[]	0	\N
84	7	5	["73", "85", "95", "96"]	2	\N
85	7	6	["84", "86"]	3	\N
86	7	7	["76", "85", "97"]	2	\N
87	7	8	[]	0	\N
88	7	9	["77", "99"]	3	\N
89	7	10	[]	0	\N
90	8	0	[]	0	\N
91	8	1	[]	0	\N
92	8	2	["81", "93"]	3	\N
93	8	3	["92", "82", "94"]	3	\N
94	8	4	["93", "95"]	4	\N
95	8	5	["84", "94"]	2	\N
96	8	6	["84"]	2	\N
97	8	7	["86"]	1	\N
98	8	8	[]	1	\N
99	8	9	["88"]	1	\N
100	8	10	[]	0	\N
16	1	4	["17","27"]	1	\N
27	2	4	["16", "26"]	4	\N
6	0	5	["17","5","17"]	3	\N
57	5	0	["46", "58"]	3	\N
58	5	1	["57","69"]	0	\N
69	6	1	["70", "58"]	3	\N
25	2	2	["24", "14", "36"]	3	\N
36	3	2	["48", "37", "25"]	3	\N
37	3	3	["36", "26", "39"]	1	\N
39	3	4	["37", "50"]	1	\N
50	4	4	["39", "51", "61"]	4	\N
26	2	3	["27", "37"]	1	\N
5	0	4	["4", "6"]	3	\N
17	1	5	["6", "18", "16"]	4	\N
4	0	3	["15", "5"]	5	\N
14	1	2	["15", "25"]	3	1
15	1	3	["4", "14"]	1	\N
\.


--
-- Data for Name: points; Type: TABLE DATA; Schema: map; Owner: postgres
--

COPY map.points (id, name) FROM stdin;
5	Blau
4	Pink
3	Grün
2	Rot
1	Orange
\.


--
-- Name: chunks chunks_pkey; Type: CONSTRAINT; Schema: map; Owner: postgres
--

ALTER TABLE ONLY map.chunks
    ADD CONSTRAINT chunks_pkey PRIMARY KEY (id);


--
-- Name: points points_pkey; Type: CONSTRAINT; Schema: map; Owner: postgres
--

ALTER TABLE ONLY map.points
    ADD CONSTRAINT points_pkey PRIMARY KEY (id);


--
-- Name: chunks chunks_points_foreign; Type: FK CONSTRAINT; Schema: map; Owner: postgres
--

ALTER TABLE ONLY map.chunks
    ADD CONSTRAINT chunks_points_foreign FOREIGN KEY (points) REFERENCES map.points(id);


--
-- Name: SCHEMA map; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA map TO "sqlservice.europaparkmap";


--
-- Name: TABLE chunks; Type: ACL; Schema: map; Owner: postgres
--

GRANT SELECT ON TABLE map.chunks TO "sqlservice.europaparkmap";


--
-- Name: TABLE points; Type: ACL; Schema: map; Owner: postgres
--

GRANT SELECT ON TABLE map.points TO "sqlservice.europaparkmap";


--
-- PostgreSQL database dump complete
--

