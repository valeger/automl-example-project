import os
from time import sleep

if (
  not os.getenv("AWS_ACCESS_KEY_ID")
  and not os.getenv("AWS_SECRET_ACCESS_KEY")
):
  raise RuntimeError("Envs variables were not found")
else:
  sleep(1)
  print("Model_1 is trained successfully")
