


class Post:
    
    id: int
    title: str
    
    
    def __init__(self) -> None:
        pass
    
    def convert_structure(self, d_post: dict, d_data: dict):
        """_summary_
        
        Input: 2 dict (dict from row of pandas, dict data get from ID post)
        Process:
            + get key of 2 dict -> value -> attribute of post that requirements
            + Not found key in data -> try...except of each key
        Args:
            d_data (dict): _description_
        """
        try:
            self.title = d_post['title']
        except:
            pass
        
        try:
            self.id = d_post['id']
        except:
            pass
        
        