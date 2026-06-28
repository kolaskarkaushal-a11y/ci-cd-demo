pipeline {

    agent any

    stages {

        stage('Detect Language') {

            steps {

                script {

                    if (fileExists('*.java')) {

                        env.LANGUAGE = "JAVA"

                    } 
                    else if (fileExists('*.py')) {

                        env.LANGUAGE = "PYTHON"

                    }
                    else if (fileExists('*.cpp')) {

                        env.LANGUAGE = "CPP"

                    }
                    else {

                        error "No supported language found"

                    }


                    echo "Detected language: ${env.LANGUAGE}"

                }

            }

        }


        stage('Build and Run') {

            steps {

                script {


                    if(env.LANGUAGE == "JAVA") {


                        sh '''
                        javac Palindrome.java
                        java PalindromeNumber
                        '''

                    }


                    else if(env.LANGUAGE == "PYTHON") {


                        sh '''
                        python3 Even.py
                        '''

                    }


                    else if(env.LANGUAGE == "CPP") {


                        sh '''
                        g++ Main.cpp -o app
                        ./app
                        '''

                    }


                }

            }

        }

    }

}
