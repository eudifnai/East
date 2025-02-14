pipeline {
    agent any  // 在任何可用节点上运行

    stages {
        // 阶段 1：从 Git 拉取代码
        stage('Checkout') {
            steps {
                echo "test Checkout..."
                }
            }
        }

        // 阶段 2：执行打包构建（以 Maven 为例）
        stage('Build') {
            steps {
                script {
                    echo "开始执行打包构建..."
                    // 如果是 Maven 项目：
                    // sh 'mvn clean package'  // 执行 Maven 打包命令

                    // 如果是 Gradle 项目：
                    // sh './gradlew build'

                    // 如果是 npm 项目：
                    // sh 'npm install && npm run build'

                    // 如果是自定义脚本：
                    // sh './your-build-script.sh'
                    sh 'echo "build"'
                }
            }
        }
    }

    // 可选：构建后操作（如清理、通知等）
    post {
        success {
            echo "构建成功！"
            // 例如：存档构建产物
            // archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
        }
        failure {
            echo "构建失败！"
            // 例如：发送邮件通知
            // emailext subject: '构建失败', body: '请检查构建日志：${BUILD_URL}', to: 'team@example.com'
        }
        always {
            echo "清理工作空间..."
            cleanWs()  // 清理工作空间
        }
    }
}
