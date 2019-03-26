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
         mv app/build/outputs/apk/debug/app-debug.apk ./${JOB_NAME}.apk
         python uploadapk.py ${params.bundleId} ${params.apiToken} "${JOB_NAME}.apk" "${JOB_NAME}" "${BUILD_ID}" "${params.apkversion}"
         
         """
  
  }
  
  
}
