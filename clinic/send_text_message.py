# account_sid="ACfc9a122f123c033fa186be36f781493f"
# Token="b0a2639fe1c7237984ffb56557d5d453"



import os
from twilio.rest import Client


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918593028701",
    from_="+17372508034",
    body="Booked Successfully",
)

print(message.sid)