pipeline {
    agent {
        label 'CarMakerServer' // Label for Windows agent
    }
    environment {
        TEMPLATE_FOLDER_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\Data\\TestRun\\Lenkwinkelrampe_Template"
        TEMPLATE_FILE = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\Template.ts"
	DESTINATION_FOLDER = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\Data\\TestRun"
	VEHICLE_FOLDER_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\Data\\Vehicle"
        OUTPUT_FOLDER = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\SimOutput\\ENGPMAKNB022"
        LOG_FOLDER = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\SimOutput\\ENGPMAKNB022\\Log"
        VFF_FOLDER_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\Data\\Vehicle"
        DAT_FOLDER_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\SimOutput\\ENGPMAKNB022\\log"
        EXCEL_FOLDER_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\VehicleInfoExcel"
        BATCH_SCRIPT_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\carmakerTestseries.bat"
        TEST_SERIES_FOLDER_PATH = "C:\\CM_Test\\Frg-Bedatung_Cayenne_E4_CM12\\Data\\TestRun"
    }

    stages {
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
