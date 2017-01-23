/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     07/12/2016 9:15:11                           */
/*==============================================================*/


drop table if exists BAHAN;

drop table if exists BENTO;

drop table if exists HISTORY_PEMESANAN;

drop table if exists KOMPOSISI;

drop table if exists MAKANAN;

drop table if exists MAKANAN_SIAP_CATERING;

drop table if exists MAKANAN_SIAP_MAKAN;

drop table if exists PELANGGAN;

drop table if exists PEMBAYARAN;

drop table if exists PEMBELIAN_POIN;

drop table if exists PEMESANAN;

drop table if exists POIN;

drop table if exists SIAP_CATERING;

drop table if exists SIAP_MAKAN;

drop table if exists SIAP_MASAK;

drop table if exists SIAP_SAJI;

drop table if exists TRACKING;

/*==============================================================*/
/* Table: BAHAN                                                 */
/*==============================================================*/
create table BAHAN
(
   ID_BAHAN             char(10) not null,
   HARGA_BAHAN          int not null,
   JUMLAH_BAHAN         int not null,
   NAMA_BAHAN           varchar(20) not null,
   primary key (ID_BAHAN)
);

/*==============================================================*/
/* Table: BENTO                                                 */
/*==============================================================*/
create table BENTO
(
   ID_MAKANAN           char(10) not null,
   NAMA_MAKANAN         varchar(15) not null,
   RATING               int not null,
   ENERGI               varchar(10) not null,
   PROTEIN              varchar(10) not null,
   DESKRIPSI            varchar(100) not null,
   STOK_MAKANAN         int not null,
   LEMAK                varchar(10) not null,
   HARGA                int not null,
   primary key (ID_MAKANAN)
);

/*==============================================================*/
/* Table: HISTORY_PEMESANAN                                     */
/*==============================================================*/
create table HISTORY_PEMESANAN
(
   TANGGAL_PEMESANAN    datetime not null,
   ID_PESANAN           char(10) not null,
   primary key (TANGGAL_PEMESANAN)
);

/*==============================================================*/
/* Table: KOMPOSISI                                             */
/*==============================================================*/
create table KOMPOSISI
(
   ID_BAHAN             char(10) not null,
   ID_MAKANAN           char(10) not null,
   primary key (ID_BAHAN)
);

/*==============================================================*/
/* Table: MAKANAN                                               */
/*==============================================================*/
create table MAKANAN
(
   ID_MAKANAN           char(10) not null,
   NAMA_MAKANAN         varchar(15) not null,
   RATING               int not null,
   ENERGI               varchar(10) not null,
   PROTEIN              varchar(10) not null,
   DESKRIPSI            varchar(100) not null,
   STOK_MAKANAN         int not null,
   LEMAK                varchar(10) not null,
   primary key (ID_MAKANAN)
);

/*==============================================================*/
/* Table: MAKANAN_SIAP_CATERING                                 */
/*==============================================================*/
create table MAKANAN_SIAP_CATERING
(
   ID_MAKANAN           char(10) not null,
   NAMA_MAKANAN         varchar(15) not null,
   RATING               int not null,
   ENERGI               varchar(10) not null,
   PROTEIN              varchar(10) not null,
   DESKRIPSI            varchar(100) not null,
   STOK_MAKANAN         int not null,
   LEMAK                varchar(10) not null,
   POIN                 int not null,
   primary key (ID_MAKANAN)
);

/*==============================================================*/
/* Table: MAKANAN_SIAP_MAKAN                                    */
/*==============================================================*/
create table MAKANAN_SIAP_MAKAN
(
   ID_MAKANAN           char(10) not null,
   NAMA_MAKANAN         varchar(15) not null,
   RATING               int not null,
   ENERGI               varchar(10) not null,
   PROTEIN              varchar(10) not null,
   DESKRIPSI            varchar(100) not null,
   STOK_MAKANAN         int not null,
   LEMAK                varchar(10) not null,
   HARGA                int not null,
   primary key (ID_MAKANAN)
);

/*==============================================================*/
/* Table: PELANGGAN                                             */
/*==============================================================*/
create table PELANGGAN
(
   ID_PELANGGAN         char(10) not null,
   NAMA                 varchar(25) not null,
   ALAMAT               varchar(50) not null,
   EMAIL                varchar(30) not null,
   PASSWORD             varchar(25) not null,
   NO_HP                int,
   TOTAL_POIN           int not null,
   primary key (ID_PELANGGAN)
);

/*==============================================================*/
/* Table: PEMBAYARAN                                            */
/*==============================================================*/
create table PEMBAYARAN
(
   ID_PEMBAYARAN        char(10) not null,
   ID_PELANGGAN         char(10) not null,
   ID_PESANAN           char(10) not null,
   STATUS_PEMBAYARAN    bool not null,
   primary key (ID_PEMBAYARAN)
);

/*==============================================================*/
/* Table: PEMBELIAN_POIN                                        */
/*==============================================================*/
create table PEMBELIAN_POIN
(
   JUMLAH_PEMBELIAN_POIN int not null,
   TANGGAL_PEMBELIAN    datetime not null,
   ID_POIN              char(10) not null,
   ID_PELANGGAN         char(10) not null,
   primary key (TANGGAL_PEMBELIAN)
);

/*==============================================================*/
/* Table: PEMESANAN                                             */
/*==============================================================*/
create table PEMESANAN
(
   ID_PESANAN           char(10) not null,
   ID_PELANGGAN         char(10) not null,
   ID_MAKANAN           char(10) not null,
   JUMLAH_PESANAN       int not null,
   TANGGAL_PENGIRIMAN   datetime not null,
   primary key (ID_PESANAN)
);

/*==============================================================*/
/* Table: POIN                                                  */
/*==============================================================*/
create table POIN
(
   ID_POIN              char(10) not null,
   HARGA_POIN           int not null,
   primary key (ID_POIN)
);

/*==============================================================*/
/* Table: SIAP_CATERING                                         */
/*==============================================================*/
create table SIAP_CATERING
(
   ID_PESANAN           char(10) not null,
   ID_PELANGGAN         char(10),
   ID_MAKANAN           char(10),
   JUMLAH_PESANAN       int not null,
   TANGGAL_PENGIRIMAN   datetime not null,
   TOTAL_POIN           int not null,
   primary key (ID_PESANAN)
);

/*==============================================================*/
/* Table: SIAP_MAKAN                                            */
/*==============================================================*/
create table SIAP_MAKAN
(
   ID_PESANAN           char(10) not null,
   ID_PELANGGAN         char(10),
   ID_MAKANAN           char(10),
   JUMLAH_PESANAN       int not null,
   TANGGAL_PENGIRIMAN   datetime not null,
   TOTAL_HARGA          int not null,
   primary key (ID_PESANAN)
);

/*==============================================================*/
/* Table: SIAP_MASAK                                            */
/*==============================================================*/
create table SIAP_MASAK
(
   ID_PESANAN           char(10) not null,
   ID_PELANGGAN         char(10),
   ID_MAKANAN           char(10),
   JUMLAH_PESANAN       int not null,
   TANGGAL_PENGIRIMAN   datetime not null,
   TOTAL_HARGA          int not null,
   primary key (ID_PESANAN)
);

/*==============================================================*/
/* Table: SIAP_SAJI                                             */
/*==============================================================*/
create table SIAP_SAJI
(
   ID_MAKANAN           char(10) not null,
   KOMPOSISI            varchar(50) not null,
   NAMA_MAKANAN         varchar(15) not null,
   RATING               int not null,
   ENERGI               varchar(10) not null,
   PROTEIN              varchar(10) not null,
   DESKRIPSI            varchar(100) not null,
   STOK_MAKANAN         int not null,
   LEMAK                varchar(10) not null,
   HARGA                int not null,
   primary key (ID_MAKANAN)
);

/*==============================================================*/
/* Table: TRACKING                                              */
/*==============================================================*/
create table TRACKING
(
   ID_TRACKING          char(10) not null,
   ID_PEMBAYARAN        char(10) not null,
   STATUS_TRACKING      bool not null,
   primary key (ID_TRACKING)
);

alter table BENTO add constraint FK_INHERITANCE_8 foreign key (ID_MAKANAN)
      references MAKANAN_SIAP_MAKAN (ID_MAKANAN) on delete restrict on update restrict;

alter table HISTORY_PEMESANAN add constraint FK_RELATIONSHIP_12 foreign key (ID_PESANAN)
      references PEMESANAN (ID_PESANAN) on delete restrict on update restrict;

alter table KOMPOSISI add constraint FK_RELATIONSHIP_10 foreign key (ID_MAKANAN)
      references SIAP_SAJI (ID_MAKANAN) on delete restrict on update restrict;

alter table KOMPOSISI add constraint FK_RELATIONSHIP_13 foreign key (ID_BAHAN)
      references BAHAN (ID_BAHAN) on delete restrict on update restrict;

alter table MAKANAN_SIAP_CATERING add constraint FK_INHERITANCE_7 foreign key (ID_MAKANAN)
      references MAKANAN (ID_MAKANAN) on delete restrict on update restrict;

alter table MAKANAN_SIAP_MAKAN add constraint FK_INHERITANCE_6 foreign key (ID_MAKANAN)
      references MAKANAN (ID_MAKANAN) on delete restrict on update restrict;

alter table PEMBAYARAN add constraint FK_RELATIONSHIP_2 foreign key (ID_PELANGGAN)
      references PELANGGAN (ID_PELANGGAN) on delete restrict on update restrict;

alter table PEMBAYARAN add constraint FK_RELATIONSHIP_3 foreign key (ID_PESANAN)
      references PEMESANAN (ID_PESANAN) on delete restrict on update restrict;

alter table PEMBELIAN_POIN add constraint FK_RELATIONSHIP_11 foreign key (ID_PELANGGAN)
      references PELANGGAN (ID_PELANGGAN) on delete restrict on update restrict;

alter table PEMBELIAN_POIN add constraint FK_RELATIONSHIP_7 foreign key (ID_POIN)
      references POIN (ID_POIN) on delete restrict on update restrict;

alter table PEMESANAN add constraint FK_RELATIONSHIP_1 foreign key (ID_PELANGGAN)
      references PELANGGAN (ID_PELANGGAN) on delete restrict on update restrict;

alter table PEMESANAN add constraint FK_RELATIONSHIP_5 foreign key (ID_MAKANAN)
      references MAKANAN (ID_MAKANAN) on delete restrict on update restrict;

alter table SIAP_CATERING add constraint FK_INHERITANCE_3 foreign key (ID_PESANAN)
      references PEMESANAN (ID_PESANAN) on delete restrict on update restrict;

alter table SIAP_MAKAN add constraint FK_INHERITANCE_5 foreign key (ID_PESANAN)
      references PEMESANAN (ID_PESANAN) on delete restrict on update restrict;

alter table SIAP_MASAK add constraint FK_INHERITANCE_4 foreign key (ID_PESANAN)
      references PEMESANAN (ID_PESANAN) on delete restrict on update restrict;

alter table SIAP_SAJI add constraint FK_INHERITANCE_9 foreign key (ID_MAKANAN)
      references MAKANAN_SIAP_MAKAN (ID_MAKANAN) on delete restrict on update restrict;

alter table TRACKING add constraint FK_RELATIONSHIP_8 foreign key (ID_PEMBAYARAN)
      references PEMBAYARAN (ID_PEMBAYARAN) on delete restrict on update restrict;

