# -*- coding: utf-8 -*-
from dbconnection import execute_sql_query, execute_sql_insert
import json

def db_save_path(start, target, path, cost):
    start_id = get_chunk_id(start[0], start[1])
    target_id = get_chunk_id(target[0], target[1])
    route = json.dumps(path)
    query = "INSERT INTO public.\"savedRoute\" (start_id, target_id, route, cost) VALUES ({}, {}, '{}', {});".format(start_id, target_id, route, cost)
    execute_sql_insert(query)

def get_chunk_id(x, y):
    query = "SELECT id FROM public.\"chunk\" where x = {} and y = {}".format(x, y)
    response  = execute_sql_query(query)
    id = int(response[0][0])
    return id

def get_coordinate_from_id(id):
    query = "SELECT x, y FROM public.\"chunk\" WHERE id = {};".format(id)
    response  = execute_sql_query(query)
    if response:
        return tuple(response)[0]
    return False

def db_clear_table(name):
    query = "DELETE FROM public.\"{}\";".format(name)
    execute_sql_insert(query)

def db_get_shortest_path(start, target):
    start_id = get_chunk_id(start[0], start[1])
    target_id = get_chunk_id(target[0], target[1])
    query = "SELECT route, cost FROM public.\"savedRoute\" WHERE start_id = {} AND target_id = {};".format(start_id, target_id)
    response  = execute_sql_query(query)
    if response:
        route = response[0][0]
        cost= response[0][1]
        print(route)
        print(cost)
        return route, cost
    else:
        query = "SELECT route, cost FROM public.\"savedRoute\" WHERE start_id = {} AND target_id = {};".format(target_id, start_id)
        response  = execute_sql_query(query)

        if response:
            route = response[0][0]
            cost= response[0][1]
            return route[::-1], cost
        
def db_get_costs(id):
    query = "SELECT cost FROM public.\"chunk\" WHERE id = {};".format(id)
    response  = execute_sql_query(query)
    if response[0][0]:
        print(response[0][0])
        return response[0][0]
    else: return False