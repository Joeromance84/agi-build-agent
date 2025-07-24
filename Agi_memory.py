# agi_memory.py
from tinydb import TinyDB, Query
from datetime import datetime
from typing import Any, Dict, List, Optional

# Initialize TinyDB for AGI's local memory
# The AGI would manage the path and potentially multiple databases autonomously.
DB_PATH = '/mnt/data/agi_memory.json'
db = TinyDB(DB_PATH)
Event = Query() # Define a Query object for easier querying

def store_event(event_type: str, data: Dict[str, Any]):
    """
    Stores an event in the AGI's local memory.
    The AGI would autonomously decide what to log and how to structure it.
    """
    event_record = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "data": data
    }
    db.insert(event_record)
    print(f"AGI Memory: Stored event '{event_type}'")

def get_recent_events(limit: int = 10, correlation_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Retrieves recent events from the AGI's memory.
    The AGI would have far more sophisticated query capabilities.
    """
    if correlation_id:
        # Filter by correlation_id if provided
        results = db.search(Event.data.correlation_id == correlation_id)
    else:
        # Get all events and sort by timestamp (TinyDB doesn't auto-sort)
        results = db.all()

    # Sort by timestamp in descending order to get most recent
    sorted_results = sorted(results, key=lambda x: x.get("timestamp", ""), reverse=True)
    return sorted_results[:limit]

def retrieve_context(query_data: Dict[str, Any], limit: int = 1) -> List[Dict[str, Any]]:
    """
    Illustrative function for AGI to retrieve specific context from memory.
    The AGI's actual context retrieval would involve semantic search,
    vector embeddings, and complex graph traversal.
    """
    # Example: Simple keyword-based search for demonstration
    search_query = Query()
    conditions = []
    for key, value in query_data.items():
        conditions.append(search_query.data[key] == value)

    if conditions:
        # Combine conditions with AND
        combined_condition = conditions[0]
        for i in range(1, len(conditions)):
            combined_condition &= conditions[i]
        results = db.search(combined_condition)
    else:
        results = []

    return results[:limit]

