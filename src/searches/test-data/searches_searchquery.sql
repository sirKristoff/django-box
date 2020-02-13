BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "searches_searchquery" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"path"	varchar(64) NOT NULL,
	"query"	varchar(220) NOT NULL,
	"timestamp"	datetime NOT NULL,
	"user_id"	integer,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);

DELETE FROM "searches_searchquery";

INSERT INTO "searches_searchquery" ("id","path","query","timestamp","user_id") VALUES
 (1,'/item/','Trans','2019-12-30 16:43:18.051928',1),
 (2,'/item/','diode','2019-12-30 16:44:36.055534',1),
 (3,'/item/','diode','2019-12-30 16:57:45.082726',NULL),
 (5,'/item/','capacitor','2019-12-30 17:01:18.460572',NULL),
 (6,'/item/','Capacitor','2019-12-30 17:02:01.681994',NULL),
 (7,'/item/','electr','2020-02-13 14:34:39.209326',1);

CREATE INDEX IF NOT EXISTS "searches_searchquery_user_id_5bdf4d1f"
ON "searches_searchquery"("user_id");

COMMIT;
