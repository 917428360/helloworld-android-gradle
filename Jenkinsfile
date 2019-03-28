/**
* Android Jenkinsfile
*/
node("master"){
  stage("Checkout"){
      steps {
        slackSend baseUrl: "https://alstru.slack.com/services/hooks/jenkins-ci/",
          tokenCredentialId: "Xq9oMDPRlDNCB97uwbAqLqCL",
          message: "Packaging ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
          checkout scm
      }
  }

  
  stage("Build"){
    slackSend baseUrl: "https://alstru.slack.com/services/hooks/jenkins-ci/",
    tokenCredentialId: "Xq9oMDPRlDNCB97uwbAqLqCL",
    message: "Publishing ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    sh 'chmod +x ./gradlew '
    sh " ${params.buildShell} "
  }
  
  stage("Upload"){
    slackSend baseUrl: "https://alstru.slack.com/services/hooks/jenkins-ci/",
    tokenCredentialId: "Xq9oMDPRlDNCB97uwbAqLqCL",
    message: "Publishing ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
      /*sh """ 
         mv app/build/outputs/apk/debug/app-debug.apk ./${params.apkName}.apk
         python uploadapk.py ${params.bundleId} \
         ${params.apiToken} "${params.apkName}.apk" \
         "${params.apkName}" "${BUILD_ID}" \
         "${params.apkVersion}" "${params.appPlatform}"
         
         
         """*/
      sh "mv app/build/outputs/apk/debug/app-debug.apk ./${params.apkName}.apk"
      def result 
      result = sh returnStdout: true, script: """python uploadapk.py ${params.bundleId} \
                                                 ${params.apiToken} "${params.apkName}.apk" \
                                                 "${params.apkName}" "${BUILD_ID}" \
                                                 "${params.apkVersion}" "${params.appPlatform}" """
       
      result = result - "\n"
      println(result)
    currentBuild.description="<img src=${result}>"
  }
  
  
}
