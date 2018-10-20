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

    def createDomainsTable(self):
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


    def createTablesTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$tables (
               id integer primary key autoincrement default(null),
               schema_id integer default(null),      -- идетификатор схемы (dbd$schemas)
               name varchar unique,                  -- имя таблицы
               description varchar default(null),    -- описание
               can_add boolean default(null),        -- разрешено ли добавление в таблицу
               can_edit boolean default(null),       -- разрешено ли редактирование  таблице?
               can_delete boolean default(null),     -- разрешено ли удаление в таблице
               temporal_mode varchar default(null),  -- временная таблица или нет? Если временная, то какого типа?
               means varchar default(null),          -- шаблон описания записи таблицы
               uuid varchar unique not null COLLATE NOCASE  -- уникальный идентификатор таблицы
            );
            create index "idx.GCOFIBEBJ" on dbd$tables(name);
            create index "idx.2J02T9LQ7" on dbd$tables(uuid);"""
        )
        cursor.close()

    def createFieldsTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$fields (
               id integer primary key autoincrement default(null),
               table_id integer not null,             -- идентификатор таблицы (dbd$tables)
               position integer not null,             -- номер поля в таблице (для упорядочивания полей)
               name varchar not null,                 -- латинское имя поля (будет использовано в схеме Oracle)
               russian_short_name varchar not null,   -- русское имя поля для отображения пользователю в интерактивных режимах
               description varchar default(null),     -- описание
               domain_id integer not null,            -- идентификатор типа поля (dbd$domains)
               can_input boolean default(null),       -- разрешено ли пользователю вводить значение в поле?
               can_edit boolean default(null),        -- разрешено ли пользователю изменять значение в поле?
               show_in_grid boolean default(null),    -- следует ли отображать значение поля в браузере таблицы?
               show_in_details boolean default(null), -- следует ли отображать значение поля в полной информации о записи таблицы?
               is_mean boolean default(null),         -- является ли поле элементом описания записи таблицы?
               autocalculated boolean default(null),  -- признак того, что значение в поле вычисляется программным кодом
               required boolean default(null),        -- признак того, что поле дорлжно быть заполнено
               uuid varchar unique not null COLLATE NOCASE -- уникальный идентификатор поля
           );
           create index "idx.7UAKR6FT7" on dbd$fields(table_id);
           create index "idx.7HJ6KZXJF" on dbd$fields(position);
           create index "idx.74RSETF9N" on dbd$fields(name);
           create index "idx.6S0E8MWZV" on dbd$fields(domain_id);
           create index "idx.88KWRBHA7" on dbd$fields(uuid);"""
        )
        cursor.close()

    def createSettingsTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$settings (
               key varchar primary key not null,
               value varchar,
               valueb BLOB
           );"""
        )
        cursor.close()

    def createConstraintsTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$constraints (
               id integer primary key autoincrement default (null),
               table_id integer not null,                           -- идентификатор таблицы (dbd$tables)
               name varchar default(null),                          -- имя ограничения
               constraint_type char default(null),                  -- вид ограничения
               reference integer default(null),        -- идентификатор таблицы (dbd$tables), на которую ссылается внешний ключ
               unique_key_id integer default(null),    -- (опционально) идентификатор ограничения (dbd$constraints) таблицы, на которую ссылается внешний ключ (*1*)
               has_value_edit boolean default(null),   -- признак наличия поля ввода ключа
               cascading_delete boolean default(null), -- признак каскадного удаления для внешнего ключа
               expression varchar default(null),       -- выражение для контрольного ограничения
               uuid varchar unique not null COLLATE NOCASE -- уникальный идентификатор ограничения
           );
           create index "idx.6F902GEQ3" on dbd$constraints(table_id);
           create index "idx.6SRYJ35AJ" on dbd$constraints(name);
           create index "idx.62HLW9WGB" on dbd$constraints(constraint_type);
           create index "idx.5PQ7Q3E6J" on dbd$constraints(reference);
           create index "idx.92GH38TZ4" on dbd$constraints(unique_key_id);
           create index "idx.6IOUMJINZ" on dbd$constraints(uuid);"""
        )
        cursor.close()

    def createConstraintDetailsTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """create table dbd$constraint_details (
               id integer primary key autoincrement default(null),
               constraint_id integer not null,          -- идентификатор ограничения (dbd$constraints)
               position integer not null,               -- номер элемента ограничения
               field_id integer not null default(null)  -- идентификатор поля (dbd$fields) в таблице, для которой определено ограничение
           );
           create index "idx.5CYTJWVWR" on dbd$constraint_details(constraint_id);
           create index "idx.507FDQDMZ" on dbd$constraint_details(position);
           create index "idx.4NG17JVD7" on dbd$constraint_details(field_id);"""
        )
        cursor.close()

    #TODO:
    def insertSchemas(self):
        cursor = self.connection.cursor()
        cursor.executemany(
            """insert into """
        )
        cursor.close()


