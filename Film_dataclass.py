from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True, slots=True)
class Livre:
    titre:str 
    realisateur:str
    annee:int
    note:float

    def est_classique(self):
        if self.annee < 2000 : return True
        return False 
    
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
    
livre = Livre("1984", "George Orwell", 1949, 9.90)
print(livre.to_json())