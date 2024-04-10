pipeline {
    agent {
        label 'CarMakerServer' // Label for Windows agent
    }
    environment {
        TEMPLATE_FOLDER_PATH = "${WORKSPACE}\\Data\\TestRun\\Lenkwinkelrampe_Template"
        TEMPLATE_FILE = "${WORKSPACE}\\Template.ts"
        DESTINATION_FOLDER = "${WORKSPACE}\\Data\\TestRun"
        VEHICLE_FOLDER_PATH = "${WORKSPACE}\\Data\\Vehicle"
        OUTPUT_FOLDER = "${WORKSPACE}\\SimOutput\\ENGPMAKNB022"
        LOG_FOLDER = "${WORKSPACE}\\SimOutput\\ENGPMAKNB022\\Log"
        VFF_FOLDER_PATH = "${WORKSPACE}\\Data\\Vehicle"
        DAT_FOLDER_PATH = "${WORKSPACE}\\SimOutput\\ENGPMAKNB022\\log"
        EXCEL_FOLDER_PATH = "${WORKSPACE}\\VehicleInfoExcel"
        BATCH_SCRIPT_PATH = "${WORKSPACE}\\carmakerTestseries.bat"
        TEST_SERIES_FOLDER_PATH = "${WORKSPACE}\\Data\\TestRun"
        FORMAT_FILE_CONFIG_PATH = "${WORKSPACE}\\Data\\Config\\Lenkwinkelrampe_Temp"
    }

    stages {
        stage('wait for 30 seconds') {
            steps {
                script {
                    // Wait for 30 seconds to change the value to ASCII format manually
                    //later this stage can be removed
                    bat "ping 127.0.0.1 -n 31 > nul"
                }
            }
        }

        stage('dat file generation') {
            steps {
                script {
                    // Call the Python script for dat file generation
                    bat "python carmakerdatfilegenerator.py"
                }
            }
        }

        stage('excel file generator') {
            steps {
                script {
                    // Call the Python script for excel file generation
                    bat "python autoexcelfilegenerator.py"
                }
            }
        }

        stage('test series generator') {
            steps {
                script {
                    // Call the Python script for test series generation
                    bat "python testseriesgenerator.py"
                }
            }
        }

        stage('await for 30 seconds') {
            steps {
                script {
                    // Wait for 30 seconds to change the value to ERG format manually
                    // Diagram layout to small manually manually
                    // later this stage can be removed
                    bat "ping 127.0.0.1 -n 31 > nul"
                }
            }
        }
        
        stage('run test manager') {
            steps {
                script {
                    // Call the Python script for running test manager
                    bat "python runtestmanager.py"
                }
            }
        }
    }
}
