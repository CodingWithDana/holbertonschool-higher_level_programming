Learning Objectives:
Articulate the differences and similarities between marshaling and serialization.

Implement serialization in a practical programming task.

Understand how serialized data can be used in web applications, databases, and network communications.

Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.


    TASK 0: Basic Serialisation - Execution Output Example:
    #!/usr/bin/env python3
    from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)


    Data serialized and saved to 'data.json'.
    Deserialized Data:
    {'name': 'John Doe', 'age': 30, 'city': 'New York'}





    TASK 1: Pickle - Sample Test:
    #!/usr/bin/env python3
    from task_01_pickle import CustomObject

    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()


    Output:

    Original Object:
    Name: John
    Age: 25
    Is Student: True

    Deserialized Object:
    Name: John
    Age: 25
    Is Student: True






    TASK 2: Converting CSV Data to JSON Format - Testing Your Code:
    #!/usr/bin/env python3
    from task_02_csv import convert_csv_to_json

    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")


    $ python3 main_02_csv.py 
    Data from data.csv has been converted to data.json





    TASK 3: Serializing and Deserializing with XML - Sample Tests:
    #!/usr/bin/env python3
    from task_03_xml import serialize_to_xml, deserialize_from_xml

    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        serialize_to_xml(sample_dict, xml_file)
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)

    if __name__ == "__main__":
        main()


