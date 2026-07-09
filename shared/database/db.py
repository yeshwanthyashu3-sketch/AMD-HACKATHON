import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "navigator.db")

class Database:
    @staticmethod
    def get_connection():
        """Returns a connection to the SQLite database."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def init_db(cls):
        """Initializes the database schema if tables do not exist."""
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with cls.get_connection() as conn:
            cursor = conn.cursor()
            
            # Table for multi-agent event logs
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    agent_name TEXT NOT NULL,
                    step_name TEXT NOT NULL,
                    message TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)
            
            # Table for security scans history
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS security_scans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    scanned_at TEXT NOT NULL,
                    file_count INTEGER NOT NULL,
                    secrets_found INTEGER NOT NULL,
                    vulnerabilities_found INTEGER NOT NULL,
                    safety_score INTEGER NOT NULL
                )
            """)
            
            # Table for compiled reports
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS compiled_reports (
                    report_id TEXT PRIMARY KEY,
                    report_type TEXT NOT NULL,
                    filepath TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            
            conn.commit()

    @classmethod
    def log_step(cls, agent_name: str, step_name: str, message: str, status: str = "SUCCESS"):
        """Logs a single processing step in the database."""
        timestamp = datetime.now().isoformat()
        with cls.get_connection() as conn:
            conn.execute(
                "INSERT INTO audit_logs (timestamp, agent_name, step_name, message, status) VALUES (?, ?, ?, ?, ?)",
                (timestamp, agent_name, step_name, message, status)
            )
            conn.commit()

    @classmethod
    def save_security_scan(cls, file_count: int, secrets_found: int, vulnerabilities_found: int, safety_score: int):
        """Saves a summary of a security audit run."""
        timestamp = datetime.now().isoformat()
        with cls.get_connection() as conn:
            conn.execute(
                "INSERT INTO security_scans (scanned_at, file_count, secrets_found, vulnerabilities_found, safety_score) VALUES (?, ?, ?, ?, ?)",
                (timestamp, file_count, secrets_found, vulnerabilities_found, safety_score)
            )
            conn.commit()

    @classmethod
    def save_compiled_report(cls, report_id: str, report_type: str, filepath: str):
        """Registers a compiled report artifact in the system."""
        timestamp = datetime.now().isoformat()
        with cls.get_connection() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO compiled_reports (report_id, report_type, filepath, created_at) VALUES (?, ?, ?, ?)",
                (report_id, report_type, filepath, timestamp)
            )
            conn.commit()

    @classmethod
    def get_audit_logs(cls, limit: int = 100):
        """Retrieves a list of recent audit logs."""
        with cls.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM audit_logs ORDER BY id DESC LIMIT ?", (limit,))
            return [dict(row) for row in cursor.fetchall()]

    @classmethod
    def get_security_scans(cls, limit: int = 50):
        """Retrieves a list of recent security scan summaries."""
        with cls.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM security_scans ORDER BY id DESC LIMIT ?", (limit,))
            return [dict(row) for row in cursor.fetchall()]

    @classmethod
    def get_compiled_reports(cls):
        """Retrieves all registered compiled reports."""
        with cls.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM compiled_reports ORDER BY created_at DESC")
            return [dict(row) for row in cursor.fetchall()]

# Auto-initialize database schema when db module is imported
Database.init_db()
