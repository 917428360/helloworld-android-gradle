/**
* Android Jenkinsfile
*/
node("master"){
  stage("Checkout"){
    checkout scm
  }

  stage("Build"){
    sh 'chmod +x ./gradlew '
    sh " ${params.buildShell} "
  }
  
  stage("Upload"){
      sh """  
         mv app/build/outputs/apk/debug/app-debug.apk ./${params.apkName}.apk
         python uploadapk.py ${params.bundleId} \
         ${params.apiToken} "${params.apkName}.apk" \
         "${params.apkName}" "${BUILD_ID}" \
         "${params.apkVersion}" "${params.appPlatform}"
         
         """
  
  }
  
  
}
