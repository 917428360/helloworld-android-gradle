/**
* Android Jenkinsfile
*/
node("master"){
  stage("Checkout"){
    slackSend baseUrl: "https://alstru.slack.com/services/hooks/jenkins-ci/",
    tokenCredentialId: "1a1578e7-7732-4de1-94f4-d9a436252e6c",
    message: "Packaging ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    checkout scm
  }

  
  stage("Build"){
    slackSend baseUrl: "https://alstru.slack.com/services/hooks/jenkins-ci/",
    tokenCredentialId: "1a1578e7-7732-4de1-94f4-d9a436252e6c",
    message: "Packaging ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    sh 'chmod +x ./gradlew '
    sh " ${params.buildShell} "
  }
  
  stage("Upload"){
      /*sh """ 
         mv app/build/outputs/apk/debug/app-debug.apk ./${params.apkName}.apk
         python uploadapk.py ${params.bundleId} \
         ${params.apiToken} "${params.apkName}.apk" \
         "${params.apkName}" "${BUILD_ID}" \
         "${params.apkVersion}" "${params.appPlatform}"
         
         
         """*/
      slackSend baseUrl: "https://alstru.slack.com/services/hooks/jenkins-ci/",
      tokenCredentialId: "1a1578e7-7732-4de1-94f4-d9a436252e6c",
      message: "Packaging ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
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
