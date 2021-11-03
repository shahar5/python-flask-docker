# Implementation of CI process including tests

### Python app
Basic Python Flask app in Docker which prints the hostname and IP of the container

### prerequisites
- Webhook configuration between GitHub and Jenkins

### CI Process
1. Jenkins pull Jenkinsfile from this repo
2. Pulls repo changes
3. Sends email notifies pipline has started
4. Build new container
5. Running tests
6. Eventually sends email with build ID + state (success/fail), path to console will be added to email if build failed
