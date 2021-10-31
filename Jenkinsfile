// Triggered by WebHook from repo https://github.com/shahar5/python-flask-docker/
properties([pipelineTriggers([githubPush()])])

MY_AGENT = "agent-01"

node(MY_AGENT){
    try {
        git url: 'https://github.com/shahar5/python-flask-docker.git', branch: 'dev'

        NotifyStarted()

        stage("Clean-env"){
            bat "docker stop my-container"
            bat "docker rm my-container"
        }

        stage("Build"){
            dir("c:\\temp\\workspace\\Tikal_Assignment"){
                bat "docker build -t lvthillo/python-flask-docker ."
                bat "docker run --name my-container -d -p 9090:8080 lvthillo/python-flask-docker"
            }
        }

        stage("Test"){
        dir("c:\\temp\\workspace\\Tikal_Assignment"){
                // app tests
                bat "Testing.py"
            }
        }
    
        stage("Result"){
            NotifySuccessful()
        }
    } catch (e){
        currentBuild.result = "FAILED"
        NotifyFailed()
        throw e
    }
}

    def NotifyStarted(){
        // Notifies Pipeline has started
    mail (
        to: "jenkins.tikal@gmail.com",
        subject: "STARTED: ${env.JOB_NAME} - Build # [${env.BUILD_NUMBER}]'",
        body: "STARTED: Job ${env.JOB_NAME} [${env.BUILD_NUMBER}]"
        )
    }

    def NotifySuccessful(){
        // Notifies pipeline finished successful build
        mail (
            to: "jenkins.tikal@gmail.com",
            subject: "SUCCESSFUL: ${env.JOB_NAME} - Build # [${env.BUILD_NUMBER}]'",
            body: "SUCCESSFUL: Job ${env.JOB_NAME} [${env.BUILD_NUMBER}]"
        )
    }

    def NotifyFailed(){
        // Notifies Pipeline has failed
        mail (
            to: "jenkins.tikal@gmail.com",
            subject: "Failed: ${env.JOB_NAME} - Build # [${env.BUILD_NUMBER}]'",
            body: "Check result at: ${env.BUILD_URL}/console"
        )
    }