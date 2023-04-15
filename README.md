## Analyzing IoT Libraries for Cryptographic API Misuse

The Internet of Things (IoT) has become an integral part of modern life, with billions of connected
devices employed in various applications. Ensuring the security of how these devices are controlled and interacted
with is crucial, as potential vulnerabilities can lead to severe consequences for both users and the 
broader ecosystem. The primary interface through which IoT devices are managed and controlled are mobile applications.
This study investigates cryptographic API misuse in widely-used IoT libraries in mobile applications, 
as this misuse can potentially result in significant security risks. 
By analyzing 54 popular IoT libraries using static analysis tools such as CryptoGuard and CogniCrypt,
as well as a comprehensive manual analysis, we found that a substantial proportion of the libraries
contain at least one instance of cryptographic API misuse, even affecting libraries developed by major 
IoT platforms like Tuya. Further, we found that some libraries engage in using evasive techniques to 
evade security checks by deliberatily transforming correct and safe instances of cryptographic API usage
to unsafe instances.  
Our study also identifies several key areas for future research and development, including the improvement
of static analysis tools, enhanced developer education on secure usage of cryptographic APIs, 
regular security audits and updates for IoT libraries, and the enforcement of compliance and regulations.
Ultimately, this honors thesis research is the first to demonstrate the prevalence of cryptographic API misuse in IoT libraries, 
emphasizing the need for improved security measures in the IoT domain.