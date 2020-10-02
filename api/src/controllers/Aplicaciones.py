from flask import jsonify, request
from db.db import cnx


class Aplicacion:
    # global cur

    @staticmethod
    def getAll():
        cur = cnx.cursor()
        aplicaciones = []
        cur.execute('SELECT * FROM evergreen.aplicaciones;')
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            dato = zip(columns, row)
            json = dict(dato)
            aplicaciones.append(json)
        cnx.commit()
        cur.close()
        return jsonify(aplicaciones)

    @staticmethod
    def post(body):
        if('nombre' not in body):
            return {"message": "Parametros imcompletos: Nombre no enviado"}, 400
        if('puerto' not in body):
            return {"message": "Parametros imcompletos: Puerto no enviado"}, 400
        if('tipo' not in body):
            return {"message": "Parametros imcompletos: Tipo no enviado"}, 400
        if('lenguaje' not in body):
            return {"message": "Parametros imcompletos: Lenguaje no enviado"}, 400
        else:
            cur = cnx.cursor()
            data = []
            sql = "INSERT INTO aplicaciones SET "
            sql, data = Aplicacion.formatData(body, sql)
            cur.execute(sql, data)
            cnx.commit()
            cur.close()
            return {"message": "Aplicacion agregada"}, 201

    @staticmethod
    def put(idApp, body):
        cur = cnx.cursor()
        data = []

        sql = "UPDATE aplicaciones SET "
        sql, data = Aplicacion.formatData(body, sql)
        sql += " WHERE id=%s"
        data.append(int(idApp))

        cur.execute(sql, data)
        cnx.commit()
        cur.close()
        return {"message": "Aplicacion actualizada"}, 200

    @staticmethod
    def delete(idApp):
        cur = cnx.cursor()
        sql = "DELETE FROM aplicaciones WHERE id = %s;"
        cur.execute(sql, [idApp])
        cnx.commit()
        cur.close()
        return {"message": "Aplicacion Eliminada"}, 200

    @staticmethod
    def formatData(body, sql):
        data = []
        keys = list(body.keys())
        query = sql

        countKeys = len(keys)
        for i in range(countKeys):
            parametro = keys[i]
            data.append(body[parametro])
            if i < countKeys-1:
                query += parametro + "=%s, "
            else:
                query += parametro + "=%s "

        return query, data
