pipeline {
    agent carMakerHost

    parameters {
        // Define parameters for scenario names and output directories
        string(name: 'HIGHWAY_SCENARIO', defaultValue: 'Highway Scenario', description: 'Name of the highway scenario')
        string(name: 'URBAN_SCENARIO', defaultValue: 'Urban Scenario', description: 'Name of the urban scenario')
        string(name: 'LANE_CHANGE_SCENARIO', defaultValue: 'Lane Change Scenario', description: 'Name of the lane change scenario')
    }

    stages {

        stage('Prepare Environment') {
            steps {
                // Configure CarMaker environment variables
                echo 'Configuring CarMaker environment...'
                withEnv(["CARMAKER_HOME=C:\\path\\to\\carmaker"]) {
                    // Set the CarMaker installation directory
                    // This environment variable might be needed by the CarMaker simulation script
                    echo 'CarMaker installation directory set to: C:\\path\\to\\carmaker'
                }

                // Copy CarMaker license file
                echo 'Copying CarMaker license file...'
                bat 'copy /Y carmaker_license.dat %CARMAKER_HOME%'

                // Additional setup tasks as needed
                // For example, setting up CarMaker project files or configuring simulation parameters

            }
        }

        stage('Run Simulations') {
            steps {
                // Run simulations for each scenario
                script {
                    // Define scenarios and output directories
                    def scenarios = [
                            env.HIGHWAY_SCENARIO: '/path/to/highway_scenario_output',
                            env.URBAN_SCENARIO: '/path/to/urban_scenario_output',
                            env.LANE_CHANGE_SCENARIO: '/path/to/lane_change_scenario_output'
                    ]

                    // Loop through each scenario and run simulation
                    scenarios.each { scenario, outputDir ->
                        echo "Running simulation for ${scenario}..."
                        // Execute batch command to run CarMaker simulation for the scenario
                        bat "python run_carmaker_simulation.py --scenario '${scenario}' --output-dir '${outputDir}'"
                    }
                }
            }
        }

        stage('Validate Results') {
            steps {
                // Validate simulation results
                echo 'Validating simulation results...'

                // Define thresholds for validation
                def minSpeedThreshold = 50  // Minimum speed threshold in km/h
                def maxDistanceThreshold = 100  // Maximum distance threshold in meters

                // Check results for each scenario
                script {
                    def scenarios = [
                            env.HIGHWAY_SCENARIO: 'C:\\path\\to\\highway_scenario_output\\results.txt',
                            env.URBAN_SCENARIO: 'C:\\path\\to\\urban_scenario_output\\results.txt',
                            env.LANE_CHANGE_SCENARIO: 'C:\\path\\to\\lane_change_scenario_output\\results.txt'
                    ]

                    scenarios.each { scenario, resultFile ->
                        echo "Validating results for ${scenario}..."

                        // Read simulation results from file
                        def results = readFile(file: resultFile).trim().split('\n')

                        // Parse and validate results
                        results.each { result ->
                            // Split result line into speed and distance
                            def (speed, distance) = result.split(',')

                            // Check if speed is below minimum threshold
                            if (Integer.parseInt(speed) < minSpeedThreshold) {
                                error "Speed below minimum threshold (${minSpeedThreshold} km/h) in ${scenario}: ${speed} km/h"
                            }

                            // Check if distance is above maximum threshold
                            if (Integer.parseInt(distance) > maxDistanceThreshold) {
                                error "Distance above maximum threshold (${maxDistanceThreshold} meters) in ${scenario}: ${distance} meters"
                            }
                        }
                    }
                }
            }
        }

        stage('Generate Reports') {
            steps {
                // Generate reports summarizing the simulation results
                echo 'Generating reports...'

                // Define paths to simulation result files
                def highwayResultFile = 'C:\\path\\to\\highway_scenario_output\\results.txt'
                def urbanResultFile = 'C:\\path\\to\\urban_scenario_output\\results.txt'
                def laneChangeResultFile = 'C:\\path\\to\\lane_change_scenario_output\\results.txt'

                // Read simulation results from files
                def highwayResults = readFile(file: highwayResultFile).trim().split('\n')
                def urbanResults = readFile(file: urbanResultFile).trim().split('\n')
                def laneChangeResults = readFile(file: laneChangeResultFile).trim().split('\n')

                // Generate summary report
                def report = """
                    <h1>Scenario-based Testing Report</h1>
                    <h2>Highway Scenario</h2>
                    <p>Results:</p>
                    <ul>
                        ${generateReportList(highwayResults)}
                    </ul>
                    <h2>Urban Scenario</h2>
                    <p>Results:</p>
                    <ul>
                        ${generateReportList(urbanResults)}
                    </ul>
                    <h2>Lane Change Scenario</h2>
                    <p>Results:</p>
                    <ul>
                        ${generateReportList(laneChangeResults)}
                    </ul>
                """

                // Write report to file
                writeFile file: 'scenario_testing_report.html', text: report
            }
        }

        stage('Cleanup') {
            steps {
                // Clean up any temporary files or resources
                echo 'Cleaning up...'

                // Delete temporary files or directories
                deleteDir() // deletes the current workspace directory

                // Additional cleanup steps as needed
                // For example, deleting specific files or directories
                bat 'del C:\\path\\to\\temporary_file.txt'
            }
        }

    }

    post {
        always {
            // Clean up after the pipeline execution
            // This post-build step will always run, regardless of the pipeline result
            echo 'Pipeline execution completed.'
        }
    }
}

// Helper function to generate HTML list from results
def generateReportList(results) {
    def listItems = ''
    results.each { result ->
        listItems += "<li>${result}</li>"
    }
    return listItems
}
