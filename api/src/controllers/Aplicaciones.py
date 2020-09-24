from flask import jsonify, request
from db.db import cnx


class Aplicacion:
    # global cur

    @staticmethod
    def listarAplicaciones():
        cur = cnx.cursor()
        aplicaciones = []
        cur.execute('SELECT id,nombre,puerto,estado,tipo,lenguaje,servidor,version,date_format(fecha_creacion, "%Y-%m-%d") as fecha_creacion, date_format(fecha_actualizacion, "%Y-%m-%d") as fecha_actualizacion FROM evergreen.aplicaciones;')
        filas = cur.fetchall()
        columnas = [i[0] for i in cur.description]
        for fila in filas:
            dato = zip(columnas, fila)
            json = dict(dato)
            aplicaciones.append(json)
        cnx.commit()
        return jsonify(aplicaciones)

    @staticmethod
    def crearAplicacion(body):
        cur = cnx.cursor()
        data = []

        sql = "INSERT INTO aplicaciones SET "
        sql, data = Aplicacion.formatData(body, sql)
        cur.execute(sql, data)
        cnx.commit()
        return {"message": "Aplicacion agregada"}, 201

    @staticmethod
    def actualizarAplicacion(idAplicacion, body):
        cur = cnx.cursor()
        data = []

        sql = "UPDATE aplicaciones SET "
        sql, data = Aplicacion.formatData(body, sql)
        sql += " WHERE id=%s"
        data.append(int(idAplicacion))

        cur.execute(sql, data)
        cnx.commit()
        return {"message": "Aplicacion actualizada"}, 200

    @staticmethod
    def eliminarAplicacion(idAplicacion):
        cur = cnx.cursor()
        sql = "DELETE FROM aplicaciones WHERE id = %s;"
        cur.execute(sql, [idAplicacion])
        cnx.commit()
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
