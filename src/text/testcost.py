import boto3
import datetime

# Initialize Cost Explorer client
client = boto3.client('ce', region_name='us-east-1')

# Get today's date in YYYY-MM-DD format
today = datetime.date.today()
start = today.strftime('%Y-%m-%d')
end = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Get today's cost
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start,
        'End': end
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost']
)

# Extract and print cost
cost_amount = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
unit = response['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']
print(f"Today's AWS cost: ${cost_amount} {unit}")
