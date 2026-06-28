pipeline {
    agent any

    stages {

        stage('Compile Java') {
            steps {
                sh 'javac Palindrome.java'
            }
        }

        stage('Run Java') {
            steps {
                sh 'java Palindrome'
            }
        }

    }
}
