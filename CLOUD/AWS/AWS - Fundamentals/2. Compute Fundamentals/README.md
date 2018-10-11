**AWS Compute Fundamentals**

`What is compute in AWS`

     Compute resources can be considered the brains and processing power required by applications and systems to carry out computational abilities via a series of instructions.
        - central processing units - CPU's 
        - random access memory - RAM
     
     So a physcial server within a data center will be considered as a Compute Resource.
     
     In AWS , diferent services provide compute resource
        - Amazon EC2 Elastic Compute Cloud
        - Amazon ECS EC2 Container Service 
        - AWS EBS Elastic Beanstalk 
        - AWS Lambda
        - AWS Batch 
        - AWS Lightsail
        
        - Elastic Load balancing & Auto Scaling ( This is not a compute resource,it allows you to control and manage the amount of compute resource used by other services)

`Amazon ECS`

    This service allows you to run Docker enabled applications packaged as containers across a cluster of EC2 instances. 
    
    -   ECS removes the need for you to manage your own cluster management system.
    -   There is no need to install any management/monitoring software for your cluster
    -   Monitoring is taken care of through the use of AWS CloudWatch
    
    The cluster is dynamically scalable in a single region.
    Multiple instance types can be used within the cluster if required
    Amazon ECS is region specific. So it can span multiple availability zones but it cannot span multiple regions. 
    The instances within the Amazon ECS Cluster also have a Docker daemon and an ECS Agent installed. These agents communicate with each other, allowing Amazon ECS commands to be translated into Docker commands.
    
`AWS Elastic Beanstalk`

    Meant for only web applications 
    AWS Elastic Beanstalk is an AWS managed service, that will take your uploaded web application code and automatically provision and deploy the appropriate and necessary resources within AWS to make the web application operational.
    These resources can include other AWS services and features,
             - EC2 Auto Scaling,
             - application health-monitoring
             - Elastic Load Balancing.
    

    -   Perfect for engineers unfamiliar with AWS
    -   Simple , Effecttive and Quick Solution
    -   Free to use , Charging only for resoures, not for EBS 
    
    Architecture
    
    Applications : Collection of environments , environmment Configurations, application versions
    Application Version : Reference to deployable code, typically points to S3 ( in S3 the deployable code will reside)
    Environment : Refer to an application version deployed on AWS resources
    Environemnt Configuration : Collection of parameters that dictate the resources behaviour  with in the environment
    Configuration Template : baseline for creating a new unique environment configuration
    
    AWS EBS Environment 2 type 1) Worker Environment
                               2) Web Server Environment 
                            
    Web Server Environment - Typically for standard web apps over Http 
                           - Used resources are - Route S3 and DNS
                                                - Elastic Load Balancing 
                                                - Auto Scaling 
                                                - EC2
                                                - Secutiry Group
    Worker Environment     - For applications with back-end processing task interacting with SQS
                           - Used resources are - SQS
                                                - EC2 
                                                - IAM Roles 
                                                - Auto Scaling
                               
    
    
     

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
    