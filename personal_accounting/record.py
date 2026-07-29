class Record:
    def __init__(self, record_id, record_type, amount, category, description, record_date, created_at):
        self.record_id = record_id
        self.record_type = record_type
        self.amount = amount
        self.category = category
        self.description = description
        self.record_date = record_date
        self.created_at = created_at


    def to_dict(self):
        return {
            'record_id': self.record_id,
            'record_type': self.record_type,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'record_date': self.record_date,
            'created_at': self.created_at,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d['record_id'],
            d['record_type'],
            d['amount'],
            d['category'],
            d['description'],
            d['record_date'],
            d['created_at']
        )

