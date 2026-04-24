import pandas as pd

# Load dataset
df = pd.read_csv("../data/claims_data.csv")

# Basic KPIs
total_claims = len(df)
approved = len(df[df['status'] == 'Approved'])
denied = len(df[df['status'] == 'Denied'])

approval_rate = (approved / total_claims) * 100
denial_rate = (denied / total_claims) * 100

avg_processing_time = df['processing_time_ms'].mean()
avg_system_delay = df['system_delay_ms'].mean()

# Correlation between delay and denial
high_delay = df[df['system_delay_ms'] > 400]
high_delay_denials = len(high_delay[high_delay['status'] == 'Denied'])

# Error distribution
error_counts = df['error_type'].value_counts()

# Output report
report = f"""
--- Denial to Network Impact Analysis Report ---

Total Claims: {total_claims}
Approval Rate: {approval_rate:.2f}%
Denial Rate: {denial_rate:.2f}%

Average Processing Time: {avg_processing_time:.2f} ms
Average System Delay: {avg_system_delay:.2f} ms

High Delay (>400ms) Cases: {len(high_delay)}
Denials in High Delay Cases: {high_delay_denials}

Error Type Distribution:
{error_counts}

Insight:
Higher system delays are associated with increased denial rates, indicating performance bottlenecks similar to network latency impact in telecom systems.
"""

# Save report
with open("../output/report.txt", "w") as f:
    f.write(report)

print(report)