Issue Summary
Duration of Outage:
Start: May 21, 2024, 13:00 UTC
End: May 21, 2024, 16:30 UTC (3 hours 30 minutes)

Impact:
The flight and train booking website was completely down, affecting all users. Users were unable to search for, book, or modify any travel plans. Approximately 100% of users experienced downtime, including several frustrated travelers trying to book last-minute trips.

Root Cause:
A misconfiguration in the load balancer led to a failure in distributing traffic across the web servers, causing the entire site to go offline. (Note to self: Never let the intern configure critical infrastructure without supervision. Again.)

Timeline
13:00 UTC: Issue detected via automated monitoring alert indicating the website was unreachable. Our Slack channel lit up like a Christmas tree.
13:05 UTC: Engineers confirmed the issue after receiving multiple alerts and customer complaints. We knew it was serious when even the intern stopped streaming Netflix.
13:10 UTC: Initial investigation started with checking the web servers' status. Everything seemed okay, which made us suspicious – like a plot twist in a tech thriller.
13:20 UTC: Web servers found to be operational; attention shifted to the network infrastructure. Maybe the router was on a coffee break?
13:30 UTC: Misleading assumption that a DDoS attack was the cause, leading to the activation of DDoS protection measures. We were prepared for battle, but there was no enemy.
13:45 UTC: Network team escalated the issue to the DevOps team after DDoS measures failed to resolve the problem. "It's not us, it's you," said the Network team.
14:00 UTC: DevOps team identified that the load balancer was not distributing traffic correctly. The load balancer was playing favorites, and nobody was happy.
14:15 UTC: Misconfiguration in the load balancer settings was discovered. Who knew one checkbox could cause so much trouble?
14:30 UTC: Correct load balancer configuration applied and traffic distribution restored. It was like flipping the switch back on.
15:00 UTC: System tests conducted to ensure stability and functionality. We crossed our fingers, toes, and wires.
16:30 UTC: Full functionality restored and monitoring confirmed stability. The website was back, and so was our sanity.
Root Cause and Resolution
Root Cause:
The load balancer was configured with incorrect settings, causing it to fail in distributing incoming traffic to the web servers. This resulted in all incoming traffic being directed to a non-responsive server, effectively taking the entire site offline. Turns out, the load balancer was letting no one in.

Resolution:
The load balancer configuration was reviewed and corrected. Specifically, the server pool configuration was updated to ensure proper traffic distribution across all available web servers. After applying the correct settings, normal traffic flow was restored. Comprehensive testing was conducted to confirm that the load balancer was functioning as expected. We also double-checked that the intern had not touched anything else.

Corrective and Preventative Measures
Improvements and Fixes:

Implement additional monitoring on the load balancer to detect misconfigurations immediately.
Enhance alert systems to differentiate between network and server issues.
Conduct regular audits of network and load balancer configurations to prevent similar issues.
Include a "Do Not Let Interns Near This" sign on critical infrastructure.
Tasks:

Task 1: Patch load balancer software to the latest version.
Task 2: Add monitoring scripts to check load balancer health and configuration status.
Task 3: Update incident response protocols to include specific steps for load balancer issues.
Task 4: Schedule bi-weekly configuration audits for the load balancer and related network components.
Task 5: Train engineering and DevOps teams on identifying and troubleshooting load balancer issues.
Task 6: Buy the intern a book on load balancers. And coffee. Lots of coffee.
