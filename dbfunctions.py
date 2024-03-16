from dbconnection import execute_sql_query, execute_sql_insert
import json

def db_save_path(start, target, path):
    start_id = get_chunk_id(start[0], start[1])
    target_id = get_chunk_id(target[0], target[1])
    route = json.dumps(path)
    query = "INSERT INTO public.\"savedRoute\" (start_id, target_id, route) VALUES ({}, {}, '{}');".format(start_id, target_id, route)
    execute_sql_insert(query)

def get_chunk_id(x, y):
    query = "SELECT id FROM public.\"chunk\" where x = {} and y = {}".format(x, y)
    response  = execute_sql_query(query)
    id = int(response[0][0])
    return id

def db_get_shortest_path(start, target):
    start_id = get_chunk_id(start[0], start[1])
    target_id = get_chunk_id(target[0], target[1])
    query = "SELECT route FROM public.\"savedRoute\" WHERE start_id = {} AND target_id = {};".format(start_id, target_id)
    response  = execute_sql_query(query)

    if response:
        route = response[0][0]
        return route
    else:
        query = "SELECT route FROM public.\"savedRoute\" WHERE start_id = {} AND target_id = {};".format(target_id, start_id)
        response  = execute_sql_query(query)

        if response:
            route = response[0][0]
            return route[::-1]