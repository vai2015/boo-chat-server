from dataclasses import dataclass

@dataclass
class User:
    id:int = None
    account_id:int = None
    email:string = None
    name:string = None
    status:string = None