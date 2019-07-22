pipeline {
  agent {
      label 'jenkins-slave-misc-operations'
  }
  stages {
    stage('Bootstrap') {
      steps {
        script {
            sh 'conda create --name vrenetic-ai'
            sh 'conda install pip'
        }
      }
    }
    stage('Installation') {
      steps {
        script {
          sh 'conda install -y -c conda-forge pyopencl'
          sh 'conda install -y -c anaconda py-opencv'
          sh 'conda install -y -c pytorch pytorch'
          sh 'pip install -r requirements.txt'
        }
      }
    }
    stage('Prepare dev') {
      when { 
          not {
            branch 'master'
          }
      }
      steps {
        script {
          sh 'python setup.py sdist bdist_wheel'
          sh 'twine check dist/*'
        }
      }
    }
    stage('Prepare and tag master') {
      when { 
          branch 'master'
      }
      steps {
        script {
          def version = sh(returnStdout: true, script: """grep '__version__ =' src/vrenetic/ai.py |awk '{print \$3}'|tr -d '\"'""").trim()
          def tag = sh(returnStdout: true, script: "git tag --contains | head -1").trim()
          echo "version: ${version}\ntag ${tag}"
          if(version != tag){
            sh("git config user.name 'jenkins'")
            sh("git config user.email 'jenkins@vrenetic.io'")
            sh "git tag ${version}"
            withCredentials([usernamePassword(credentialsId: 'vrenetic_bot_github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
              sh "git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/vrenetic-inc/vrenetic-ai-cli ${version}"
            }
          }
          sh 'python setup.py sdist bdist_wheel'
          sh 'twine check dist/*'
        }
      }
    }    
    stage('Push to nexus') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'nexus_credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
            sh 'twine upload dist/* --repository-url https://nexus.core.vrenetic.io/repository/pypi-hosted/ -u $USER -p $PASS --verbose'
          }
        }
      }
    }    
  }
}
