# CELL 2 — Generate custom dataset and save as book.csv
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# --- Sample log messages per category ---
positive_logs = [
    "System started successfully", "Database connection established",
    "User login successful", "File upload completed",
    "Payment processed successfully", "Backup completed without errors",
    "Service health check passed", "API response time optimal",
    "Cache hit rate improved", "Deployment succeeded",
    "Authentication token valid", "Memory usage within limits",
    "Query executed successfully", "Email notification sent",
    "Session created for user", "Transaction committed",
    "Data sync completed", "Report generated successfully",
    "New user registered", "Scheduled task completed",
]

negative_logs = [
    "ERROR: Database connection failed", "CRITICAL: Disk space exhausted",
    "ERROR: Authentication failed for user", "CRITICAL: Service crashed unexpectedly",
    "ERROR: File not found exception", "WARNING: Memory threshold exceeded",
    "ERROR: Timeout connecting to server", "CRITICAL: Null pointer exception",
    "ERROR: Payment gateway unreachable", "CRITICAL: Data corruption detected",
    "ERROR: API rate limit exceeded", "CRITICAL: Unauthorized access attempt",
    "ERROR: Invalid token received", "CRITICAL: Queue overflow detected",
    "ERROR: SSL certificate expired", "CRITICAL: CPU usage critical",
    "ERROR: Deadlock detected in DB", "CRITICAL: Node failure reported",
    "ERROR: Packet loss detected", "CRITICAL: Service unavailable 503",
]

irrelevant_logs = [
    "User changed display preferences", "Theme updated to dark mode",
    "Timezone set to Asia/Kolkata", "Language preference saved",
    "User viewed help documentation", "Notification settings updated",
    "Profile picture changed", "Password hint updated",
    "User logged idle timeout", "Font size preference saved",
    "Browser fingerprint recorded", "Session heartbeat received",
    "Ping request acknowledged", "Keepalive packet sent",
    "Cookie preferences updated", "Analytics event tracked",
    "User scrolled page bottom", "Tooltip displayed on hover",
    "Search suggestion clicked", "Tab focus changed",
]

levels   = ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]
services = ["auth-service", "db-service", "api-gateway", "payment-service",
            "storage-service", "notification-service", "cache-service", "scheduler"]
hosts    = [f"node-{i:02d}" for i in range(1, 9)]
users    = [f"usr_{random.randint(1000,9999)}" for _ in range(150)]

base_time = datetime(2024, 3, 1, 0, 0, 0)
rows = []

for i in range(150):
    category = i % 3   # 0=positive, 1=negative, 2=irrelevant

    if category == 0:
        message   = random.choice(positive_logs)
        sentiment = "Positive"
        level     = random.choice(["INFO", "DEBUG"])
        response  = random.randint(50, 300)
        cpu       = round(random.uniform(10, 45), 1)
        memory    = round(random.uniform(20, 55), 1)
    elif category == 1:
        message   = random.choice(negative_logs)
        sentiment = "Negative"
        level     = random.choice(["ERROR", "CRITICAL", "WARNING"])
        response  = random.randint(800, 5000)
        cpu       = round(random.uniform(70, 99), 1)
        memory    = round(random.uniform(70, 99), 1)
    else:
        message   = random.choice(irrelevant_logs)
        sentiment = "Irrelevant"
        level     = random.choice(["INFO", "DEBUG"])
        response  = random.randint(20, 200)
        cpu       = round(random.uniform(5, 30), 1)
        memory    = round(random.uniform(10, 40), 1)

    ts = base_time + timedelta(hours=i * 1.5, minutes=random.randint(0, 59), seconds=random.randint(0, 59))

    rows.append({
        "log_id"          : f"LOG{i+1:04d}",
        "timestamp"       : ts.strftime("%Y-%m-%d %H:%M:%S"),
        "level"           : level,
        "service"         : random.choice(services),
        "host"            : random.choice(hosts),
        "user_id"         : users[i],
        "message"         : message,
        "response_time_ms": response,
        "cpu_usage"       : cpu,
        "memory_usage"    : memory,
        "sentiment"       : sentiment
    })

df = pd.DataFrame(rows)
df.to_csv("book.csv", index=False)
print(f"✅ book.csv created — {len(df)} rows × {len(df.columns)} columns")
print(f"\nSentiment distribution:\n{df['sentiment'].value_counts().to_string()}")
df.head(6)
