class SensorData:
    def __init__(self, db):
        self.db = db
        
    # Create a timeseries collection
    # def create_timeseries_collection(self):
    #     self.db.create_collection(
    #         'sensor_readings',
    #         timeseries={
    #             'timeField': 'timestamp',  # Timestamp field
    #             'metaField': 'location',  # Metadata field (optional)
    #         }
    #     )
        
    # # Insert data into the timeseries collection
    # def insert_data(self, sensor_data):
    #     self.db['sensor_readings'].insert_many(sensor_data)
        
    # Display the temperature information
    def display(self):
        results = self.db.sensor_readings.find()
        for record in results:
            print(f"Temperature at {record['timestamp']} in {record['location']} is {record['temperature']}°C")
