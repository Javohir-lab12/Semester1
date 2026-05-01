from dataclasses import dataclass, field
from contextlib import contextmanager

class LogError(Exception):
    pass

@dataclass
class LogEntry:
    timestamp: str
    level: str
    message: str
    response_time: int
    _status: str = field(init=False, default="PENDING")
    def __post_init__(self):
        valid_levels = ("INFO", "WARNING", "ERROR", "CRITICAL")
        if self.level not in valid_levels:
            raise LogError(f"Unknown level: {self.level}")
        if self.response_time < 0:
            raise LogError(f"Negative response time: {self.response_time}")
    @property
    def is_slow(self):
        return self.response_time > 500
    def __str__(self):
        return f"{self.timestamp} [{self.level}] {self.message} ({self.response_time}ms) -> {self._status}"
    def __gt__(self, other):
        return self.response_time > other.response_time
    
class LogScanner:
    def __init__(self, entries, max_ms):
        self.entries = entries
        self.max_ms = max_ms
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter >= len(self.entries):
            raise StopIteration
        current = self.entries[self.counter]
        self.counter += 1
        current._status =  "OK" if current.response_time <= self.max_ms else "ALERT"
        return current
    
def scan_report(scanner):
    ok_s = 0
    alerts = 0
    for entry in scanner:
        if entry._status == "OK":
            ok_s += 1
        else:
            alerts += 1
        yield str(entry)
    yield f"Result: {ok_s} ok, {alerts} alerts"

@contextmanager
def monitoring_session(name):
    print(f"[START] {name}")
    entries = []
    try:
        yield entries
    except LogError as e:
        print(f"[FAIL] {e}")
    print(f"[END] {name} ({len(entries)} entries)")


with monitoring_session("Web Server") as logs:
    logs.append(LogEntry("10:00:01", "INFO", "GET /home", 120))
    logs.append(LogEntry("10:00:02", "WARNING", "GET /api", 850))
    logs.append(LogEntry("10:00:03", "ERROR", "POST /login", 1500))

    for line in scan_report(LogScanner(logs, 1000)):
        print(line)

    print(logs[1] > logs[0])

print()

with monitoring_session("DB Server") as logs:
    logs.append(LogEntry("11:00:01", "DEBUG", "Query", 50))