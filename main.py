from julep import Client
import time
import yaml
import os
from dotenv import load_dotenv

load_dotenv()

# Load env vars
JULEP_API_KEY = os.getenv("JULEP_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

client = Client(api_key=JULEP_API_KEY)

# Create the agent
agent = client.agents.create(
    name="Food Tour Planner Agent",
    about="Plans detailed food tours for cities using local cuisine, restaurants and weather info."
)

print(f"Agent Created: {agent.id}")

# Replace env vars in YAML
with open("food_tour_task.yaml", "r") as f:
    yaml_template = f.read()

yaml_filled = (
    yaml_template
    .replace("${GOOGLE_API_KEY}", GOOGLE_API_KEY)
    .replace("${OPENWEATHER_API_KEY}", OPENWEATHER_API_KEY)
)

task_definition = yaml.safe_load(yaml_filled)

# Create task
task = client.tasks.create(
    agent_id=agent.id,
    **task_definition
)

print(f"Task Created: {task.id}")

# Create execution
execution = client.executions.create(
    task_id=task.id,
    input={
        "locations": ["New York", "Paris", "Tokyo"]
    }
)

print(f"Execution Started: {execution.id}")

# Poll status
while (result := client.executions.get(execution.id)).status not in ["succeeded", "failed", "cancelled"]:
    print(f"Status: {result.status}")
    time.sleep(2)

# Output result
if result.status == "succeeded":
    print("Execution Succeeded:")
    print(result.output)
else:
    print("Execution Failed:")
    print(result.error)
