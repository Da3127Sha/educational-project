import sqlite3
from __future__ import unicode_literals


class RAMToDBDConverter:

    CURRENT_DBD_VERSION = '3.1'

    fileName = None
    connection = None

    def __init__(self, fileName):
        self.fileName = fileName
        self.connection = sqlite3.connect(self.fileName)

    #TODO:
    def init(self):
        self.cursor.execute("pragma foreign_keys=on;")
        self.cursor.execute("begin transaction;")
        self.createSchemasTable()

    def createSchemasTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$schemas (
            id integer primary key autoincrement not null,
            name varchar not null);"""
        )
        cursor.close()

    def createSchemasTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$domains (
            id  integer primary key autoincrement default(null),
            name varchar unique default(null),  -- имя домена
            description varchar default(null),  -- описание
            data_type_id integer not null,      -- идентификатор типа (dbd$data_types)
            length integer default(null),       -- длина
            char_length integer default(null),  -- длина в символах
            precision integer default(null),    -- точность
             scale integer default(null),        -- количество знаков после запятой
             width integer default(null),        -- ширина визуализации в символах
             align char default(null),           -- признак выравнивания
             show_null boolean default(null),    -- нужно показывать нулевое значение?
             show_lead_nulls boolean default(null),      -- следует ли показывать лидирующие нули?
             thousands_separator boolean default(null),  -- нужен ли разделитель тысяч?
             summable boolean default(null),             -- признак того, что поле является суммируемым
             case_sensitive boolean default(null),       -- признак необходимости регистронезависимого поиска для поля
             uuid varchar unique not null COLLATE NOCASE -- уникальный идентификатор домена
             );
             create index "idx.FZX832TFV" on dbd$domains(data_type_id);
             create index "idx.4AF9IY0XR" on dbd$domains(uuid);"""
        )
        cursor.close()

    #TODO:
    def insertSchemas(self):
        cursor = self.connection.cursor()
        cursor.executemany(
            """insert into """
        )
        cursor.close()


