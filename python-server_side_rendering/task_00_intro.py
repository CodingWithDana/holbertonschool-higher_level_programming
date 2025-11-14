import logging # used to log errors and info messages
import os # allows working with the file system (check, create, etc..)

def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        logging.error('invalid type.')
        return
    
    if not template:
        logging.error('Template is empty, no output files generated.')
        return
    
    if not attendees:
        logging.error('No data provided, no output files generated.')
        return
    
    for i, value in enumerate(attendees, 1):
        if not isinstance(value, dict):
            # logging.error(f'{i}: N/A.')
            logging.error(f'N/A')
            continue
        
        output = template
        output = output.replace('{name}', str(value.get('name') or 'N/A'))
        output = output.replace('{event_title}', str(value.get('event_title') or 'N/A'))
        output = output.replace('{event_date}', str(value.get('event_date') or 'N/A'))
        output = output.replace('{event_location}', str(value.get('event_location') or 'N/A'))
        
        filename = f'output_{i}.txt'
        
        if os.path.exists(filename):
            continue
        
        try:
            with open(filename, 'w') as f:
                f.write(output)
        except IOError as e:
            logging.error(f"Error writing to file {filename}: {e}")
# Hints:
# Use Python’s string replace method to substitute placeholders with actual values.
# Use os.path.exists to check if a file already exists before writing.
# Use try and except blocks to handle potential errors gracefully.