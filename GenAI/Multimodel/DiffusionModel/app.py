import streamlit as st
import yaml
import time

# Title
st.title("Azure DevOps Pipeline YAML Simulator")

# Input for YAML pipeline configuration
yaml_input = st.text_area("Paste your Azure DevOps pipeline YAML here:", height=300)

# Function to validate YAML syntax
def validate_yaml(yaml_text):
    try:
        parsed_yaml = yaml.safe_load(yaml_text)
        return True, parsed_yaml
    except yaml.YAMLError as e:
        return False, str(e)

# Button to validate YAML
if st.button("Validate YAML"):
    if yaml_input.strip():
        is_valid, result = validate_yaml(yaml_input)
        if is_valid:
            st.success("YAML syntax is valid!")
        else:
            st.error(f"Invalid YAML syntax:\n{result}")
    else:
        st.warning("Please paste your YAML configuration.")

# Enhanced simulation of pipeline stages with dependencies and conditions
def enhanced_execute_pipeline(parsed_yaml):
    stages = parsed_yaml.get("stages", [])
    if not stages:
        st.warning("No stages found in the pipeline.")
        return

    stage_results = {}

    for stage in stages:
        stage_name = stage.get("stage", "Unnamed Stage")
        depends_on = stage.get("dependsOn", [])
        condition = stage.get("condition", None)

        # Check dependencies
        if depends_on:
            dependencies_satisfied = True
            for dependency in depends_on:
                if stage_results.get(dependency) != "success":
                    st.write(f"Skipping stage {stage_name} due to failed dependency: {dependency}.")
                    stage_results[stage_name] = "skipped"
                    dependencies_satisfied = False
                    break
            if not dependencies_satisfied:
                continue

        # Check conditions
        if condition:
            if "failed" in condition:
                dependent_stage = condition.split("(")[1].split(")")[0]
                if stage_results.get(dependent_stage) != "failed":
                    st.write(f"Skipping stage {stage_name} due to condition: {condition}.")
                    stage_results[stage_name] = "skipped"
                    continue

        # Execute the stage
        st.write(f"Starting stage: {stage_name}...")
        time.sleep(2)  # Simulate execution time
        jobs = stage.get("jobs", [])
        for job in jobs:
            job_name = job.get("job", "Unnamed Job")
            st.write(f"Executing job: {job_name}...")
            time.sleep(2)  # Simulate execution time
            steps = job.get("steps", [])
            for step in steps:
                step_display = step.get("displayName", "Unnamed Step")
                st.write(f"Running step: {step_display}...")
                time.sleep(2)  # Simulate execution time

        st.success(f"Stage {stage_name} completed successfully.")
        stage_results[stage_name] = "success"

    # Log final stage results for debugging
    st.write("Final Stage Results:")
    st.json(stage_results)

# Button to run the enhanced pipeline
if st.button("Run Enhanced Pipeline"):
    if yaml_input.strip():
        is_valid, result = validate_yaml(yaml_input)
        if is_valid:
            st.info("Executing enhanced pipeline...")
            enhanced_execute_pipeline(result)
        else:
            st.error("Invalid YAML. Cannot execute pipeline.")
    else:
        st.warning("Please paste your YAML configuration.")

# Instructions for users
st.sidebar.title("Instructions")
st.sidebar.write("1. Paste your Azure DevOps YAML pipeline configuration into the text area.")
st.sidebar.write("2. Click 'Validate YAML' to check for syntax errors.")
st.sidebar.write("3. Click 'Run Enhanced Pipeline' to simulate the pipeline execution with dependencies and conditions.")
st.sidebar.write("4. View the progress of each stage, job, and step in real-time, including skipped stages due to dependencies or conditions.")
