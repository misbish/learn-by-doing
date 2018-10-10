**CLOUD FOUNDRY : FROM ZERO TO HERO**

**1. What is Cloud Foundry?**

What is Cloud Foundry
    
    - Initial release in 2011
    - An open Cloud Native Platform (PaaS)
    - Fast and easy to build, test, deploy & scale apps
    - Works with any language or framework
    - Available as open source, commercial distributions or hosted offerings
    
Where can you get Open Source Cloud Foundry?

    - github.com/cloudfoundry
    - cf-release requires BOSH knowledge
    - BOSH-lite for a local CF deployment
    
Certified Providers 
    
    - Atos Cloud Foundry
    - Cloud.gov
    - Huawei FusionStage
    - IBM Cloud Foundry
    - Pivotal Cloud Foundry
    - SAP Cloud Platform
    - SUSE Cloud Application Platform
    
https://run.pivotal.io/   - Console url running on pivotal web service 

    
**2. Interacting with Cloud Foundry via the CLI**

How do I interact with CF?

    - Command Line Interface (CLI): from terminal / command prompt
    - IDE plugins
    - Vendor specific consoles
    - CI tool integration (e.g Concourse.ci)
    
    cf <some-command> --help
    
    Every application and service is scoped to a space
    
    $ cf spaces
    $ cf space <some-space> # for details
    
    Organisations segregate tenants in a Cloud Foundry installation.
    
    $ cf orgs
    $ cf org pcfdev-org
    
    Quotas provide resource limits to orgs and spaces
    
    $ cf quotas
    
    Run cf target to confirm your org and current space.
    
    $ cf target
    
    Change org and space
    
    $ cf target -o ORG -s SPACE 
    
**3. Pushing Your First App**

    What happens when I cf push?
    
    1. Upload: App files sent to CF
    2. Staging: Executable artifact is created (droplet)
    3. Running: App starts on an app host
    
    Buildpacks create a runnable artifact called a droplet
      App Files + Runtime Dependencies = App Artifact (droplet)
      
    Apps are started on specialized VMs called cells
         If it’s a web process, it binds to a TCP port
    I    Instances are distributed across multiple cells
         Router distributes traffic across instances
         
     $cf push
     $cf push -f <path to manifest>
     $cf apps  #  List the apps
     $cf app web-app   #to see more details of your app:
     
     manifest.yml
     ---
     applications:
     - name: web-app
       random-route: true
     
     
     NOTE: Debug cf commands with CF_TRACE=true    
**4. Buildpacks**

    Buildpack: A Cloud Foundry component that resolves your app’s runtime dependencies 
    
    Types of Buildpacks
        Default buildpacks (included in the platform)
        Community buildpacks: Leverage the community
        Custom buildpacks: Build your own
        
**5. Resilience and Availability**

    I want my app to be resilient, So that random failures won’t take it offline
    
    Embrace failure & run many instances of the same app
    cf scale imperfect-app -i 3
    What happens when instances fail?
       They are automatically recreated by comparing desired state to actual state
    
    Health Management Components:
        nsync: gets message from CC (after cf scale). Writes the DesiredLRP value in BBS.
        Cell Rep Monitors containers to get the ActualLRP value
        BBS: Monitors DesiredLRP vs ActualLRP and kills/launches instances.
        
        
**6. Debugging**

    cf logs  # App logs
    cf events  # App events
    cf ssh       #SSH access to the app container
    
**7. Domains and Routes**

    Domains: provide a namespace from which to create routes
        Shared domain: for all of CF
        Private domain: scoped to an Org
        Requires DNS to be configured
        
    Route: A URL on which an application can be accessed.
    
    Blue/Green Deployments 
        Deploy a new version (GREEN) of your app.
        Map the route to it
        Validate
        Unmap from the old version (BLUE)