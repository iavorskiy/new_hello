node {
    def app

    stage('Clone repository') {


        checkout scm
    }

     stage('Build image') {


        app = docker.build("iavorskiy/app_new")
    }



    stage('Push image') {

        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }

     stage('Deploy image'){

         sh "docker pull iavorskiy/app_new"
         sh "/usr/local/bin/docker-compose up -d"
        

    }

    stage('Deploy nginx conf'){

         sh "docker ps > test.txt"
         sh "python nginx_upstream.py"
         sh "docker-compose restart web"

    }



}
