# admin_control_lockdown.py

import logging

# Configure logging for status visibility
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

def check_command_source(source_name: str) -> bool:
    """
    Determines if incoming commands should be accepted based on source.
    Args:
        source_name (str): The name of the source issuing commands (e.g., 'replit', 'github')
    Returns:
        bool: True if commands from source are accepted, False otherwise.
    """
    # Lockdown: reject all commands from 'replit' for now
    if source_name.lower() == 'replit':
        logging.warning("ADMIN LOCKDOWN: Rejecting all commands from Replit until further notice.")
        return False
    # Accept commands only from GitHub during this period
    if source_name.lower() == 'github':
        logging.info("Accepting commands from GitHub repository.")
        return True
    # Reject commands from any other sources by default
    logging.warning(f"Rejecting commands from unknown source: {source_name}")
    return False

def process_incoming_command(command: dict, source_name: str):
    """
    Process commands if source is allowed.
    Args:
        command (dict): The incoming command payload.
        source_name (str): The source of the command.
    """
    if check_command_source(source_name):
        logging.info(f"Processing command from {source_name}: {command}")
        # Insert actual command execution logic here
        # For example: execute_command(command)
    else:
        logging.error(f"Command rejected from {source_name}: {command}")

# Example usage
if __name__ == "__main__":
    # Simulated incoming commands from different sources
    commands_to_test = [
        {"action": "update_code", "details": "Patch security vulnerability"},
        {"action": "restart_service", "details": "Apply configuration changes"},
    ]

    sources = ["replit", "github", "unknown_source"]

    for source in sources:
        for cmd in commands_to_test:
            process_incoming_command(cmd, source)
