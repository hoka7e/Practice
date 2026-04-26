
try:
    import psycopg2
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False
    print("psycopg2 not found – leaderboard disabled. Install: pip install psycopg2-binary")

def db_connect():
    if not DB_AVAILABLE:
        return None
    try:
        conn = psycopg2.connect(
            dbname="snake_game",
            user="hoka7e",
            host="localhost",
            port=5432
        )
        return conn
    except Exception as e:
        print(f"DB connection failed: {e}")
        return None


def db_init(conn) -> None:
    if conn is None:
        return
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id       SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS game_sessions (
                id            SERIAL PRIMARY KEY,
                player_id     INTEGER REFERENCES players(id),
                score         INTEGER   NOT NULL,
                level_reached INTEGER   NOT NULL,
                played_at     TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()


def db_get_or_create_player(conn, username: str):
    if conn is None:
        return None
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM players WHERE username = %s", (username,))
        row = cur.fetchone()
        if row:
            return row[0]
        cur.execute(
            "INSERT INTO players (username) VALUES (%s) RETURNING id",
            (username,)
        )
        pid = cur.fetchone()[0]
        conn.commit()
        return pid


def db_save_session(conn, player_id, score, level_reached):
    if conn is None or player_id is None:
        print(f"SAVE SKIPPED: conn={conn}, player_id={player_id}")  
        return
    try:                                                              
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)",
                (player_id, score, level_reached)
            )
            conn.commit()
        print(f"SAVED: player_id={player_id}, score={score}")       
    except Exception as e:                                          
        print(f"SAVE ERROR: {e}")                                     
        conn.rollback()                                               


def db_get_leaderboard(conn) -> list:
    if conn is None:
        return []
    with conn.cursor() as cur:
        cur.execute("""
            SELECT p.username, gs.score, gs.level_reached, gs.played_at
            FROM game_sessions gs
            JOIN players p ON p.id = gs.player_id
            ORDER BY gs.score DESC
            LIMIT 10
        """)
        return cur.fetchall()


def db_get_personal_best(conn, player_id) -> int:
    if conn is None or player_id is None:
        return 0
    with conn.cursor() as cur:
        cur.execute(
            "SELECT COALESCE(MAX(score), 0) FROM game_sessions WHERE player_id = %s",
            (player_id,)
        )
        return cur.fetchone()[0]