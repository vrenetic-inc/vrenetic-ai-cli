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
          sh 'conda install -c conda-forge pyopencl'
          sh 'conda install -c anaconda py-opencv'
          sh 'pip install -r requirements.txt'
        }
      }
    }
    stage('Prepare package') {
      steps {
        script {
          sh 'python setup.py sdist bdist_wheel'
        }
      }
    }
  }
}
