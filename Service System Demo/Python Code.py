### MINIMALISTIC SIMULATION MODEL ###

# Model name: Service System Demo
# Model can be found at: https://cloud.anylogic.com/models

# Load anylogiccloudclient library
from anylogiccloudclient.client.cloud_client import CloudClient

# Creat a CloudClient object, given the API key
client = CloudClient("e05a6efa-ea5f-4adf-b090-ae0ca7d16c20")

# Obtain latest model version of "Service System Demo" model
version = client.get_latest_model_version("Service System Demo")

# Create an Inputs object with the default input values
inputs = client.create_inputs_from_experiment(version, "Baseline")

# Change the "Server Capacity" parameter value
inputs.set_input("Server capacity", 8)

# Creat a simulation object with the inputs
simulation = client.create_simulation(inputs)

# Obtain the simulaiton outputs
outputs = simulation.get_outputs_and_run_if_absent()

# Print the simulaiton model outcome values
print("Raw outputs = " + str(outputs.get_raw_outputs()))
print("For Server Capacity = " + str(inputs.get_input("Server capacity")))
print("Mean queue size = " + str(outputs.value("Mean queue size|Mean queue size")))
print("Server utilization = " + str(outputs.value("Utilization|Server utilization")))
