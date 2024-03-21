-- Erstellen der Tabelle chunk
CREATE TABLE IF NOT EXISTS public.chunk
(
    id SERIAL PRIMARY KEY,
    x INTEGER,
    y INTEGER,
    border_on JSONB,
    cost NUMERIC(4,2)
);

-- Erstellen der Tabelle savedRoute
CREATE TABLE IF NOT EXISTS public.savedRoute
(
    id SERIAL PRIMARY KEY,
    start_id INTEGER REFERENCES public.chunk(id),
    target_id INTEGER REFERENCES public.chunk(id),
    route JSONB
);

-- Einfügen der Daten in die Tabelle chunk
INSERT INTO public.chunk (id, x, y, border_on, cost) VALUES
(0, 0, 0, '[]', NULL),
(2, 0, 2, '[]', NULL),
(15, 5, 0, '[]', NULL),
(17, 5, 2, '[]', NULL),
(3, 1, 0, '["6", "4"]', 0.50),
(4, 1, 1, '["1", "3", "5"]', 1.00),
(5, 1, 2, '["4", "8"]', 1.50),
(6, 2, 0, '["3", "7"]', 0.50),
(7, 2, 1, '["6", "10"]', 0.50),
(8, 2, 2, '["5", "11"]', 1.50),
(9, 3, 0, '["10", "12"]', 0.50),
(10, 3, 1, '["9", "7"]', 1.00),
(11, 3, 2, '["8", "14"]', 1.50),
(12, 4, 0, '["9", "13"]', 1.00),
(13, 4, 1, '["12", "14", "16"]', 1.00),
(14, 4, 2, '["11", "13"]', 1.50),
(16, 5, 1, '["13"]', 1.00),
(1, 0, 1, '["4"]', 1.00);
