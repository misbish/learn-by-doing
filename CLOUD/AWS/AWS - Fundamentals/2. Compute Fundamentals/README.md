**AWS Compute Fundamentals**



1) Choose AMI
Step 1: Choose an Amazon Machine Image (AMI) 


An AMI is a template that contains the software configuration (operating system, application server, and applications) required to launch your instance. You can select an AMI provided by AWS, our user community, or the AWS Marketplace; or you can select one of your own AMIs.
2)  Choose Instance Type 
Step 2: Choose an Instance Type
Amazon EC2 provides a wide selection of instance types optimized to fit different use cases
    Instances are virtual servers that can run applications.
They have varying combinations of CPU, memory, storage, and networking capacity, and give you the flexibility to choose the appropriate mix of resources for your applications. Learn more about instance types and how they can meet your computing needs.
Step 3: Configure Instance Details 
Configure the instance to suit your requirements. You can launch multiple instances from the same AMI, request Spot instances to take advantage of the lower pricing, assign an access management role to the instance, and more.

Step 4: Add Storage 
Your instance will be launched with the following storage device settings. You can attach additional EBS volumes and instance store volumes to your instance, or edit the settings of the root volume. You can also attach additional EBS volumes after launching an instance, but not instance store volumes. Learn more about storage options in Amazon EC2.
    
    Step 5: Add Tags 
    Cancel Previous Review and Launch Next: Configure Security Group 
    A tag consists of a case-sensitive key-value pair. For example, you could define a tag with key = Name and value = Webserver.
    A copy of a tag can be applied to volumes, instances or both.
    Tags will be applied to all instances and volumes. Learn more about tagging your Amazon EC2 resources.
    
    Step 6: Configure Security Group 
    Cancel Previous Review and Launch 
    A security group is a set of firewall rules that control the traffic for your instance. On this page, you can add rules to allow specific traffic to reach your instance. For example, if you want to set up a web server and allow Internet traffic to reach your instance, add rules that allow unrestricted access to the HTTP and HTTPS ports. You can create a new security group or select from an existing one below. Learn more about Amazon EC2 security groups.
    Step 7: Review Instance Launch 
    Cancel Previous Launch 
    Please review your instance launch details. You can go back to edit changes for each section. Click Launch to assign a key pair to your instance and complete the launch process.
    