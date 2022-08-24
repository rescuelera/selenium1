
node{
    stage("Create folder"){
        sh "echo ${BUILD_ID}"
        sh 'mkdir -p ${BUILD_ID}'
    }
    stage("Run tests"){
        withDockerContainer(args: '-u root', image: 'python:3.9') {
            sh 'pwd'
            sh 'ls -las ${BUILD_ID}'
            sh 'pwd'
            sh 'rm -rf selenium1'
            sh 'git clone https://github.com/rescuelera/selenium1.git ./${BUILD_ID}/selenium1'
            sh 'ls -las ./${BUILD_ID}/selenium1'
            sh 'cd ./${BUILD_ID}/selenium1'
            sh 'pwd'
            sh 'cd ./${BUILD_ID}/selenium1 && pip install -r requirements.txt'
            sh 'cd ./${BUILD_ID}/selenium1 && pytest tests --base-url=${BASE_URL} --browser=${BROWSER} --executor=${EXECUTOR_ADDRESS} --browser_version=${BROWSER_VERSION} --alluredir=allure-results || true'
            sh 'pwd'
            sh 'cd ./${BUILD_ID} && mkdir root_results'
            sh 'cp -r ./${BUILD_ID}/selenium1/allure-results ./${BUILD_ID}/root_results'
            sh 'rm -rf ./${BUILD_ID}/selenium1'
        }

        sh 'pwd'
        sh 'cp -r ./${BUILD_ID}/root_results/allure-results ${BUILD_ID}'
        sh 'ls -las ${BUILD_ID}'

        withDockerContainer(args: '-u root', image: 'python:3.9') {
            //sh 'allure generate --clean allure-results'
            sh 'pwd'
            sh 'rm -rf ./${BUILD_ID}/root_results'
        }
    }
    stage("Publish test report"){
        sh 'pwd'
        sh 'ls -las ${BUILD_ID}/allure-results'

        allure includeProperties: false, jdk: '', results: [[path: '${BUILD_ID}/allure-results']]
    }
    stage("Cleanup"){
        sh 'ls -las ${BUILD_ID}/allure-results'
        sh 'rm -rf ./${BUILD_ID'
        sh 'ls -las .'
    }
}