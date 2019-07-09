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
          sh 'pip install -r requirements.txt'
        }
      }
    }
    stage('Prepare package') {
      steps {
        script {
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
