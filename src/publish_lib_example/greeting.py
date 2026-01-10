class Greeting:
    """A simple greeting class that provides greeting functionality."""
    
    def __init__(self):
        """Initialize the Greeting class."""
        pass

    def say_hello(self, name: str) -> str:
        """Say hello to someone.
        
        Args:
            name (str): The name of the person to greet.
            
        Returns:
            str: A greeting message.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        
        message = f"Hello, {name}!"
        return message
    
    def say_goodbye(self, name: str) -> str:
        """Say goodbye to someone.
        
        Args:
            name (str): The name of the person to say goodbye to.
            
        Returns:
            str: A goodbye message.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
            
        message = f"Goodbye, {name}!"
        return message
    
    def get_greeting_with_time(self, name: str, time_of_day: str) -> str:
        """Get a time-specific greeting.
        
        Args:
            name (str): The name of the person to greet.
            time_of_day (str): Time of day ('morning', 'afternoon', 'evening').
            
        Returns:
            str: A time-specific greeting message.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
            
        valid_times = ['morning', 'afternoon', 'evening']
        if time_of_day.lower() not in valid_times:
            raise ValueError(f"Time of day must be one of: {', '.join(valid_times)}")
        
        greetings = {
            'morning': f"Good morning, {name}!",
            'afternoon': f"Good afternoon, {name}!", 
            'evening': f"Good evening, {name}!"
        }
        
        return greetings[time_of_day.lower()]