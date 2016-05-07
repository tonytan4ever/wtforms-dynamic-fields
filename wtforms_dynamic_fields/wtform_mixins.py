import json

from wtforms.fields import Field, TextField, SelectField


class WTFormDyanmicFieldsMixin(object):

    field_type_mapping = {
        'Text': TextField,
        'Select': SelectField,
        # TODO: Add more field mappings
    }

    @classmethod
    def append_field(cls, name, field):
        if not isinstance(field, Field):
            raise TypeError('Given field is not a valid WTForm Field.')

        setattr(cls, name, field)
        return cls

    @classmethod
    def read_field_config_json(cls, file_path):
        return json.loads(open(file_path).read())

    @classmethod
    def add_fields_from_config_json(cls, fields_config_json):
        """
        # TODO: Add jsonschema validation, make sure fileds_config_json is
        # a list of dicts like this:
        [{
          'field_name': 'a_name'
          'field_type': 'a_type'
        },{
          'field_name': 'b_name'
          'field_type': 'b_type'
        }]
        """
        for field_config in fields_config_json:
            field_name = field_config.pop('field_name')
            field_type = field_config.pop('field_type')
            temp_field = cls.field_type_mapping[field_type](field_config)
            cls.append_field(field_name, temp_field)
