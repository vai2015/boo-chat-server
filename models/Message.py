from dataclasses import dataclass

@dataclass
class Message:
    id:int = None
    sender_id:int = None
    receiver_id:int = None
    room_code:string = None
    sender_name:string = None
    receiver_name:string = None
    message:string = None
    is_read:bool = False
    created_date:Date = None
    read_date:Date = None
    
