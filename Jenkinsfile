/**
* Android Jenkinsfile
*/
node("master"){
  stage("Checkout"){
    checkout scm
  }

  stage("Build"){
    sh 'chmod +x ./gradlew '
   
    
    if (params.BUILD_CONFIG == 'release') {
      sh './gradlew clean assembleRelease' // builds app/build/outputs/apk/app-release.apk file
    } else {
      sh './gradlew clean assembleDebug' // builds app/build/outputs/apk/app-debug.apk
    }
  }

 stage("Archive"){
    if (params.BUILD_CONFIG == 'release') {
        archiveArtifacts artifacts: 'app/build/outputs/apk/**/app-release.apk', excludes: 'app/build/outputs/apk/*-unaligned.apk'
    } else {
        archiveArtifacts artifacts: 'app/build/outputs/apk/**/app-debug.apk', excludes: 'app/build/outputs/apk/*-unaligned.apk'
    }
  }
}
