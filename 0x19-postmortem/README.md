Issue Summary:
Duration: The outage occurred from January 15, 2024, at 10:00 AM to January 16, 2024, at 2:00 AM

Impact: The outage affected the availability and performance of our web application,
resulting in a significant slowdown in response times. Approximately 50% of users experience
degraded service.

Timeline:

10:00 AM - Issue Detected: The issue was initially detected by monitoring alerts.
Actions Taken: The engineering team focused on the database and application server. Assumptions were made that the issue could be related to database or recent code deployments.

Misleading Investigation Paths: Initial investigations was towards potential database connection issues, leading to extensive analysis of query performance and connection limits.

Escalation: After initial attempts failed to identify the root cause, the incident was escalated to the senior engineering team for further analysis.

Resolution: The incident was resolved after extensive debugging revealed a misconfiguration in the load balancer settings, causing uneven distribution of traffic and overload on certain servers. The load balancer configuration was corrected.

Root Cause and Resolution:

- Root Cause: The root cause was a misconfiguration in the load balancer, leading to uneven distribution of traffic and overloading certain servers.

- Resolution: The issue was resolved by correcting the load balancer configuration.

Corrective and Preventative Measures:

Improvements/Fixes:
- Enhance load balancer monitoring and alerting.
- Implement automated testing procedures for load balancer configurations.

Tasks to Address the Issue:
- Update load balancer configuration scripts.
- Implement automated configuration checks.

In conclusion, the web stack outage incident was a valuable learning experience that highlighted the importance of rigorous configuration management and proactive monitoring. By implementing the corrective measures outlined above, we aim to enhance the resilience and stability of our system, minimizing the risk of similar incidents in the future.
