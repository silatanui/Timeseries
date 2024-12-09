from pymongo import MongoClient
from datetime import datetime
from sensor_data import SensorData

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sensor_data']
    
    sensor = SensorData(db)
    
    # Step 1: Create the timeseries collection
    # sensor.create_timeseries_collection()
    # print("#" * 80)
    # print("Time series collection 'sensor_readings' created.")
    # print("#" * 80)
    
    # Step 2: Insert data into the timeseries database
    # now = datetime.now()
    # sensor_data = [
    #     {'timestamp': now, 'location': 'Location A', 'temperature': 25.5},
    #     {'timestamp': now, 'location': 'Location B', 'temperature': 24.8},
    #     {'timestamp': now, 'location': 'Location C', 'temperature': 25.2},
    #     {'timestamp': now, 'location': 'Location D', 'temperature': 25.3},
    # ]
    
    # sensor.insert_data(sensor_data)
    print("#" * 80)
    print("Inserted sensor data into the MongoDB database.")
    print("#" * 80)
    
    # Step 3: Display the sensor data
    sensor.display()

# Call the main function
if __name__ == '__main__':
    main()
