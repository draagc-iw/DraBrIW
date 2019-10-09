from App.Storage import DBConnectionManager
from App.User import User
from App.Orders import Round

from App.Utils.Mappers import RoundMapper


class RoundService:
    def __init__(self):
        self._db = DBConnectionManager()

    def new_round(self, initiator: User):
        create_q = """ 
        INSERT INTO rounds (initiator_id)
        VALUES (?);
        """
        cursor = self._db.cursor_prepared
        cursor.execute(create_q, (initiator.uid,))
        self._db.commit()

    def add_person(self, round_id, person_id, drink_id):
        add_q = """
        INSERT INTO rounds_users(round_id, person_id, drinks_id)
        VALUES (?, ?, ?);
        """
        cursor = self._db.cursor_prepared
        cursor.execute(add_q, (round_id, person_id, drink_id))
        self._db.commit()

    def close_round(self, round_id):
        close_q = """
        UPDATE rounds SET active=0
        WHERE rounds.id = ?;
        """

        cursor = self._db.cursor_prepared
        cursor.execute(close_q, (round_id,))

    def get_with_id(self, id: int):
        get_id_q = f"""SELECT r.id               AS round_id,
       r.active     AS round_active,
       p.id               AS initiator_id,
       p.first_name       AS initiator_first_name,
       p.last_name        AS initiator_last_name,
       ru_link.person_id  AS person_id,
       ru_link.first_name AS person_first_name,
       ru_link.last_name  AS person_last_name,
       ru_link.drink_name AS drink_name,
       ru_link.drink_id   AS drink_id
FROM rounds r
         INNER JOIN person p ON r.initiator_id = p.id
         LEFT JOIN
     (SELECT ru.round_id, p2.first_name, p2.last_name, p2.id AS person_id, d.name AS drink_name, d.id AS drink_id
      FROM rounds_users AS ru
               LEFT JOIN person p2 on ru.person_id = p2.id
               LEFT JOIN drinks d on ru.drinks_id = d.id)
         AS ru_link
     ON ru_link.round_id = r.id
WHERE r.id = {id};
        """
        cursor = self._db.cursor_named
        cursor.execute(get_id_q)
        res = RoundMapper.from_db(cursor.fetchall())
        # print(res[0].orders)
        return res[0] if len(res) > 0 else None

    def get_all(self):
        get_all_q = """
        SELECT r.id         AS round_id,
               r.active     AS round_active,
               p.id         AS initiator_id,
               p.first_name AS initiator_first_name,
               p.last_name  AS initiator_last_name,
               ru_link.person_id AS person_id,
               ru_link.first_name AS person_first_name,
               ru_link.last_name AS person_last_name,
               ru_link.drink_name AS drink_name,
               ru_link.drink_id AS drink_id
        FROM rounds r
                 INNER JOIN person p ON r.initiator_id = p.id
                 LEFT JOIN
             (SELECT ru.round_id, p2.first_name, p2.last_name, p2.id AS person_id, d.name AS drink_name, d.id AS drink_id
              FROM rounds_users AS ru
                       INNER JOIN person p2 on ru.person_id = p2.id
                       INNER JOIN drinks d on ru.drinks_id = d.id)
                 AS ru_link
             ON ru_link.round_id = r.id
             ORDER BY r.id;
             
        """

        cursor = self._db.cursor_named
        cursor.execute(get_all_q)
        return RoundMapper.from_db(cursor.fetchall())


