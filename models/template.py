from bson import ObjectId

class Template:
    def __init__(self, name, category, image_url, latex_code, system_instruction, example_prompt=None, _id=None):
        self.name = name
        self.category = category
        self.image_url = image_url
        self.latex_code = latex_code
        self.system_instruction = system_instruction
        self.example_prompt = example_prompt
        self._id = _id

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            category=data.get('category'),
            image_url=data.get('image_url'),
            latex_code=data.get('latex_code'),
            system_instruction=data.get('system_instruction'),
            example_prompt=data.get('exampleprompt'),
            _id=data.get('_id')
        )

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "image_url": self.image_url,
            "latex_code": self.latex_code,
            "system_instruction": self.system_instruction,
            "exampleprompt": self.example_prompt
        }

    def to_json(self):
        data = self.to_dict()
        if self._id:
            data['id'] = str(self._id)
        return data
