pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            sh 'docker build -t cynthion https://github.com/grvvy/cynthion.git'
        }
    }
    stage('Test Suite') {
        agent{
            docker {
                image 'cynthion'
                reuseNode true
                args '--name cynthion_container --group-add=46 --device-cgroup-rule="c 189:* rmw" --device /dev/bus/usb'
                additionalBuildArgs '--build-arg CACHEBUST=$(date +%s)'
            }
        }
        steps {
            sh './ci/build.sh'
            sh 'hubs all off'
            retry(3) {
                sh './ci/test.sh'
            }
            sh 'hubs all reset'
        }
    }
    post {
        always {
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true)
        }
    }
}
