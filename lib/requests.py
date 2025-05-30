class Request:
    def __init__(self, id, status='unseen', date_submitted=None, home_id=None, user_id=None, start_date=None, end_date=None):
        self.id = id 
        self.status = status
        self.date_submitted = date_submitted
        self.home_id = home_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
    
    def __eq__(self, other):
            return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Request({self.id}, {self.status}, {self.date_submitted}, {self.home_id}, {self.user_id}, {self.start_date}, {self.end_date})"
    
    def confirm_request(self):
        self.status = 'confirmed'
