PGDMP  +    9                |            EuropaparkPlanerMap    15.6 (Debian 15.6-0+deb12u1)    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16388    EuropaparkPlanerMap    DATABASE     �   CREATE DATABASE "EuropaparkPlanerMap" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
 %   DROP DATABASE "EuropaparkPlanerMap";
                postgres    false            �           0    0    DATABASE "EuropaparkPlanerMap"    ACL     K   GRANT ALL ON DATABASE "EuropaparkPlanerMap" TO "sqlservice.europaparkmap";
                   postgres    false    4003                        2615    16390    map    SCHEMA        CREATE SCHEMA map;
    DROP SCHEMA map;
                postgres    false            �           0    0 
   SCHEMA map    ACL     7   GRANT ALL ON SCHEMA map TO "sqlservice.europaparkmap";
                   postgres    false    6            �            1259    16499    chunks    TABLE     �   CREATE TABLE map.chunks (
    id bigint NOT NULL,
    x bigint NOT NULL,
    y bigint NOT NULL,
    borders_on json,
    runtime integer,
    points integer
);
    DROP TABLE map.chunks;
       map         heap    postgres    false    6            �           0    0    TABLE chunks    ACL     @   GRANT SELECT ON TABLE map.chunks TO "sqlservice.europaparkmap";
          map          postgres    false    216            �            1259    16489    points    TABLE     ^   CREATE TABLE map.points (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);
    DROP TABLE map.points;
       map         heap    postgres    false    6            �           0    0    TABLE points    ACL     @   GRANT SELECT ON TABLE map.points TO "sqlservice.europaparkmap";
          map          postgres    false    215            �          0    16499    chunks 
   TABLE DATA           D   COPY map.chunks (id, x, y, borders_on, runtime, points) FROM stdin;
    map          postgres    false    216   �       �          0    16489    points 
   TABLE DATA           '   COPY map.points (id, name) FROM stdin;
    map          postgres    false    215   �                  2606    16505    chunks chunks_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY map.chunks
    ADD CONSTRAINT chunks_pkey PRIMARY KEY (id);
 9   ALTER TABLE ONLY map.chunks DROP CONSTRAINT chunks_pkey;
       map            postgres    false    216            
           2606    16493    points points_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY map.points
    ADD CONSTRAINT points_pkey PRIMARY KEY (id);
 9   ALTER TABLE ONLY map.points DROP CONSTRAINT points_pkey;
       map            postgres    false    215                       2606    16506    chunks chunks_points_foreign    FK CONSTRAINT     u   ALTER TABLE ONLY map.chunks
    ADD CONSTRAINT chunks_points_foreign FOREIGN KEY (points) REFERENCES map.points(id);
 C   ALTER TABLE ONLY map.chunks DROP CONSTRAINT chunks_points_foreign;
       map          postgres    false    216    3850    215            �   �  x�]UQ�%!��O���ͦ��\����Ka�f�TQ@Sy�������U�Ei��jZ⯑��K����0�����������Ib�^Z�����ď��Z-t@"vsc"uc���*~�z���`[\R�CW�w�q�m��E��LG+��k�k�_Sá��{���s�H�C������
Po��|�t���;6D�"�]>w�)(s/`�EԶ������Yr��2K��[2dc7u�@ 1[�;PE��p�O��G���4�hA�}���Vm���&��@ܳhzu�V���P�3�����;4=��/)8R�G��9���)� 8���!p]���G� �(
A
?� ;�k��A�ށ۶&c���f���� �sM=��!�f${D�h�լA�1.@ZӁJCYD^
�Z�yb�̣@������W�/�GT�d������w	�j�A�PG��AR1�Pd�bX�툧�T�R41'S���RT�"m�B��PJ��l>G����Y�t,�d@��<'yέ���6�ž�
�G:3�01�,5 $�6g9��3#p���B	�$ߙf(ɞ�,G�Aܗ�Z!���5-:YN�� ː{~:��P�9������z䳎-��~�2��N�~{��,�R���Cò�ŗE�TL$�F(��b3:���G�Xs�2����ر�r�&��k>�MGt���#?8�k��Q׹�ı@� 	�+(��z�3wќ����H���r���?^1(��������s      �   2   x�3�t�I,�2�����2�t/:�'�ˈ3(��ːӿ(1/=�+F��� ��T     