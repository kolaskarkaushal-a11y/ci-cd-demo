pipeline {

    agent any

    stages {

        stage('Detect Language') {

            steps {

                script {


                    if (fileExists('Largest.java')) {

                        env.LANGUAGE = "JAVA"

                    } 
                    else if (fileExists('Even.py')) {

                        env.LANGUAGE = "PYTHON"

                    }
                    else if (fileExists('Main.cpp')) {

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
                        /* javac Largest.java
                        java Largest
                        '''*/

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
